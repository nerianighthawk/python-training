from datetime import datetime
import time
execTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
time.sleep(10)
execTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(execTime)
