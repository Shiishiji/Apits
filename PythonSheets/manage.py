import os
import sys
import datetime

file_name = 'PythonSheets/spreadsheet.py'
now = datetime.datetime.now()

try:
    print("{0} Running: {1}".format(now, file_name))
    os.system("python " + file_name)
except Exception as e:
    print("Exception while trying to execute: {0}\n{1}".format(file_name, e))