from datetime import datetime
import time
startTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(startTime)
time.sleep(10)
endTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
print(endTime)
