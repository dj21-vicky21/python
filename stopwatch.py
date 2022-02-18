import time
hr =0
min =0
sec =0

while True:
    time.sleep(1)
    print('{:02d}:{:02d}:{:02d}'.format(hr,min,sec),end='\r')
    sec+=1
    if sec>60:
        min+=1
        sec=0
    if min>60:
        hr+=1
        min=0

