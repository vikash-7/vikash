import RPi.GPIO as Ben
import time
Ben. setmode (Ben.BCM)

while True:
    Ben.setup(26,Ben.OUT)
    for blink in range (0,10):
        Ben.output(26,Ben.HIGH)
        time.sleep(1)
        Ben.output(26,Ben.LOW)
        time.sleep(1)