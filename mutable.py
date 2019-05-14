from datetime import datetime
import time
execTime = "start time: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
time.sleep(10)
execTime = "end time: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
