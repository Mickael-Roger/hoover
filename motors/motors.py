import RPi.GPIO as GPIO   
import time

in1 = 33
in2 = 40
ena = 35

in3 = 38
in4 = 36
enb = 37

GPIO.setmode(GPIO.BOARD)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)

GPIO.setup(ena,GPIO.OUT)
GPIO.setup(enb,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

p=GPIO.PWM(ena,1000)
p=GPIO.PWM(enb,1000)

p.start(50)

GPIO.output(in1,GPIO.HIGH)
GPIO.output(in2,GPIO.LOW)

time.sleep(10)

GPIO.cleanup()
