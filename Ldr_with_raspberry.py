import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

LDR = 24
LED = 23

GPIO.setup(LDR,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED,GPIO.OUT)

while True:
    LDR_status = GPIO.input(LDR)
    print(LDR_status)
    sleep(0.1)
    if LDR_status == 1:
        GPIO.output(LED,GPIO.LOW)
    else:
        GPIO.output(LED,GPIO.HIGH)