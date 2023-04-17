from water2 import simulator
import time
i=0
x=400
y=600
run=True
timer=0
while run:
    if timer == 1:
        run=False
    simulator(x,y)
    timer+=1
    time.sleep(5)
    