import pyautogui as auto

codePath = r"C:\Users\yangj\OneDrive\Desktop\IU-Project\realtime_project_code\~JuanInstallations\eeg_project_recording_scripts"

autoPath = r"C:\Users\yangj\OneDrive\Desktop\IU-Project\realtime_project_code\~JuanInstallations\eeg_project_recording_scripts\automaticLaunch"
gtecLslPath = r"C:\Users\yangj\OneDrive\Desktop\IU-Project\realtime_project_code\~JuanInstallations\LSL_adds"
LabRecorderpath = r"C:/Users/yangj/OneDrive/Desktop/IU-Project/realtime_project_code/~JuanInstallations/LSL_adds/LabRecorder"
expSettingsPath = r"C:/Users/yangj/OneDrive/Desktop/IU-Project/realtime_project_code/~JuanInstallations/eeg_project_recording_scripts/exp-4-settings.cfg"
#"C:\\Users\\asus\\Documents\\CurrentStudy\\Realtime-Project-Exp2\\exp-2-settings.cfg"
model = r"C:/Users/yangj/OneDrive/Desktop/IU-Project/realtime_project_code/eeg_project_real_time_interface-master/gnautilus_interface"
expControllerPath = r"C:\Users\yangj\OneDrive\Desktop\IU-Project\realtime_project_code\~JuanInstallations\eeg_project_recording_scripts\OddBallTask"

mouseRecorderPath = r"C:\Users\yangj\OneDrive\Desktop\IU-Project\realtime_project_code\~JuanInstallations\LSL_adds\LabRecorder"

# commands
goToPath = "cd " + codePath
lab = 'cd ' + LabRecorderpath
activateEnv = "conda activate sensor_env_py37"


def setupTab(additionalCommand=None, arg=None, goto_code_base=True):
    if goto_code_base:
        auto.write(goToPath, interval=interval_writing)
        auto.press('enter')

    auto.write(activateEnv, interval=interval_writing)
    auto.press('enter')

    # goto command
    if additionalCommand == 'goto' and arg is not None:
        auto.write("cd " + arg, interval=interval_writing)
        auto.press('enter')
    # Write
    if additionalCommand == 'write' and arg is not None:
        auto.write(arg, interval=interval_writing)
def setupTabLab(additionalCommand=None, arg=None, goto_code_base=True):
    if goto_code_base:
        auto.write(lab, interval=interval_writing)
        auto.press('enter')

    auto.write(activateEnv, interval=interval_writing)
    auto.press('enter')

    # goto command
    if additionalCommand == 'goto' and arg is not None:
        auto.write("cd " + arg, interval=interval_writing)
        auto.press('enter')
    # Write
    if additionalCommand == 'write' and arg is not None:
        auto.write(arg, interval=interval_writing)

if __name__ == '__main__':
    interval_writing = 0.018
    print(codePath)
    auto.sleep(0.5)

    # Get Active terminal
    fw = auto.getActiveWindow()
    fw.maximize()

    auto.hotkey('alt', 'shift', '-', interval=interval_writing)
    auto.hotkey('alt', 'shift', '-', interval=interval_writing)

    auto.hotkey('alt', 'up', interval=interval_writing)
    auto.hotkey('alt', 'up', interval=interval_writing)

    auto.hotkey('alt', 'shift', '-', interval=interval_writing)
    auto.hotkey('alt', 'up', interval=interval_writing)

    auto.hotkey('alt', 'shift', '+', interval=interval_writing)
    auto.hotkey('alt', 'down', interval=interval_writing)
    auto.hotkey('alt', 'shift', '+', interval=interval_writing)

    auto.hotkey('alt', 'up', interval=interval_writing)
    setupTab(additionalCommand="goto", arg=mouseRecorderPath, goto_code_base=False)
    setupTab(additionalCommand="write", arg=".\mouse.exe",goto_code_base=False)

    auto.hotkey('alt', 'right', interval=interval_writing)
    setupTab(additionalCommand="goto", arg=model)
    auto.write("python ControllerCombinedSensors.py")
    auto.hotkey('alt', 'down', interval=interval_writing)
    setupTab(additionalCommand="write", arg="python SendGnautilusAlternative.py")


    auto.hotkey('alt', 'right', interval=interval_writing)
    setupTab(additionalCommand="write", arg="python SendEyeTracking.p")

    auto.hotkey('alt', 'down', interval=interval_writing)
    setupTabLab(additionalCommand="write", arg=".\LabRecorder.exe -c " + expSettingsPath)
    # setupTab(additionalCommand="goto", arg=LabRecorderpath, goto_code_base=False)
    # setupTab(additionalCommand="write", arg="LabRecorder.exe",goto_code_base=False)
    
    auto.hotkey('alt', 'down', interval=interval_writing)
    setupTab(additionalCommand="goto", arg=expControllerPath)
    setupTab(additionalCommand="write", arg="python ExperimentController.py 180", goto_code_base=False)

