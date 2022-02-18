import datetime
import time
while True:
    date = datetime.datetime.now()
    time.sleep(0.5)
    print("{:02d}:{:02d}:{:02d}".format(date.time().hour-12,date.time().minute,date.time().second) ,end='\r')

