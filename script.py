import win32api, win32print
import subprocess
import time

subprocess.call("TASKKILL /F /IM Acrobat.exe", shell=True)