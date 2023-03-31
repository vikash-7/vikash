import RPi.GPIO as rg
import time
rg.setmode(rg.BCM)
trig=2
echo=3
rg.setup(trig,rg.OUT)
rg.setup(echo,rg.IN)

while True:
    rg.output(trig,rg.HIGH)
    time.sleep(0.00001)
    rg.output(trig,rg.LOW)
    
    while  rg.input(echo)==0:
        pulse_start=time.time()
        
    while rg.input(echo)==1:
        pulse_end=time.time()
        
        pulse_duration=pulse_end-pulse_start
        distance=pulse_duration*34300/2
        distance=round(distance,2)
        print("distance=",distance,"cm")
        time.sleep(1)
        
