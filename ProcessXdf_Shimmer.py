
import random
import pyxdf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re
import copy
from pathlib import Path
from pylsl import local_clock
import time

#Calculate difference between LSL clock and computer clock
t1 = local_clock()
t2 = time.time()
difference = t2 - t1


dataPath  = Path('./data/')

for f in dataPath.glob('*.xdf'):
    print(f)
    #Load xdf files
    if len(re.findall(".xdf", f.name))>0:
        file = f

        task = re.findall("(?<=T[0-9]{2}_).+(?=\.xdf)", file.name)[0]
        subject =  re.findall(".+(?=_S[0-9]{1})", file.name)[0]
        session =  int(re.findall("(?<=_S)[0-9]{1}(?=_T)", file.name)[0])
        trial =  int(re.findall("(?<=_T)[0-9]{2}(?=_)", file.name)[0])

        dstPath1 = Path('./data-processed/') / "{:}_S{:d}_T{:d}_{:}_shimmer_ppg.txt".format(subject,session, trial,task)

        data, header = pyxdf.load_xdf(file)

        #Get data and experiment markers
        for stream in data:
            if stream['info']['name'][0] == 'ExperimentMarkers':
                markers = stream['time_series']
                markersTime = stream['time_stamps']
            elif stream['info']['name'][0] == 'Shimmer_ppg' :
                if stream['footer']['info']['first_timestamp'][0] != '0':
                    eegData = stream['time_series']
                    eegInfo = stream['info']
                    eegTime = stream['time_stamps']
            # elif stream['info']['name'][0] == 'NB-2015.10.15':
            #     if stream['footer']['info']['first_timestamp'][0] != '0':
            #         eegData = stream['time_series']
            #         eegInfo = stream['info']
            #         eegTime = stream['time_stamps']

        # #Get EEG headers
        # columns = []
        # listOfChannels = eegInfo['desc'][0]['channels'][0]['channel']
        # for ch in listOfChannels:
        #     columns.append(ch['label'][0])
        #
        # columns = [x.upper() for x in columns]
        # eegChannels = copy.deepcopy(columns)
        #eegChannels.remove("COUNTER")

        #Create data frame
        # data = np.hstack((eegTime.reshape(-1,1), eegData))
        df =  pd.DataFrame(data=eegData, index=None, columns=['raw'])

        #Add label and time stamps
        df['COMPUTER_TIME'] = eegTime

        #Label
        if task == "Baseline" or task == 'BASELINE': #Baseline
            df['label'] = 0
        elif task == "Normal" or task == "Easy" or task == 'Low' or task == 'LOW': #Low Workload
            df['label'] = 5
        elif task == "Inv" or task == "High" or task == 'HIGH': # high Workload
            df['label'] = 10

        #Remove data before start and after finish
        df = df.loc[(df['COMPUTER_TIME'] > markersTime[0]) & (df['COMPUTER_TIME'] < markersTime[1]) ]

        #Update timestamps to computer time
        df['COMPUTER_TIME'] = df['COMPUTER_TIME'] + difference

        #Save to CSV

        df.to_csv(dstPath1,index=None)

