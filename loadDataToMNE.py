import numpy as np
import mne
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

# file = Path('./data-processed/juan_S3_T5_epoc.txt')
# file = Path('./data-processed/U05_S1_T01_pegNormal.txt')
# file = Path('./data-processed/Karuna_S3_T2_Inv.txt')
# file = Path('./data-processed/EX1U07_S1_T01_Baseline.txt')
# file = Path('./data-processed/EX1U07_S1_T01_pegNormal.txt')
file = Path('./data-processed/U06_S1_T4_sutureNormal_raw.txt')

EEG_channels = ["FP1","FP2","AF3","AF4","F7","F3","FZ","F4",
                "F8","FC5","FC1","FC2","FC6","T7","C3","CZ",
                "C4","T8","CP5","CP1","CP2","CP6","P7","P3",
                "PZ","P4","P8","PO7","PO3","PO4","PO8","OZ"]

sfreq = 250

df = pd.read_csv(file)
data = df[EEG_channels].values.transpose()

time_vector = df['COMPUTER_TIME'].values
sample_time = [time_vector[x+1] - time_vector[x] for x in range(time_vector.shape[0] - 1 )]

#Convert from uv to v
data = data / 1e6
ch_names = EEG_channels
ch_types = ["eeg"] * len(ch_names)

# It is also possible to use info from another raw object.
info = mne.create_info(ch_names=ch_names, sfreq=sfreq, ch_types=ch_types)
raw = mne.io.RawArray(data, info)

# filtered = raw.filter(0.5,30)

scalings = {'eeg': 0.00003}  # Could also pass a dictionary with some value == 'auto'

raw.plot(n_channels=32, scalings=scalings, title='Auto-scaled Data from arrays',
         show=True, block=True)