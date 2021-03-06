#!/usr/bin/python3
import RPi.GPIO as GPIO   
import rospy
import time

from Motion.srv import Motion 

class Motors:
    
    def __init__(self):

        self.ena = 33
        self.in1 = 35
        self.in2 = 37
        
        self.enb = 36
        self.in3 = 38    
        self.in4 = 40


        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.in1,GPIO.OUT)
        GPIO.setup(self.in2,GPIO.OUT)
        GPIO.setup(self.in3,GPIO.OUT)
        GPIO.setup(self.in4,GPIO.OUT)
        GPIO.setup(self.ena,GPIO.OUT)
        GPIO.setup(self.enb,GPIO.OUT)

        self.stop()
        
        self.pa=GPIO.PWM(self.ena,1000)
        self.pb=GPIO.PWM(self.enb,1000)
        
        self.speed(1)


    def speed(self, speed):     # Speed between 1 and 4
        if speed > 4:
            speed=4
        if speed < 1:
            speed=1

        self.pa.start(round(speed*25))
        self.pb.start(round(speed*25))
            

        
    def stop(self):        
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.LOW)
        
        
    def backward(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)


    def forward(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)


    def right(self):
        GPIO.output(self.in1,GPIO.LOW)
        GPIO.output(self.in2,GPIO.HIGH)
        GPIO.output(self.in3,GPIO.LOW)
        GPIO.output(self.in4,GPIO.HIGH)


    def left(self):
        GPIO.output(self.in1,GPIO.HIGH)
        GPIO.output(self.in2,GPIO.LOW)
        GPIO.output(self.in3,GPIO.HIGH)
        GPIO.output(self.in4,GPIO.LOW)
    
    
    def __del__(self):
        GPIO.cleanup()


    def move(self, action):
        actionTable = {'forward': self.forward,
                       'backward': self.backward,
                       'right': self.right,
                       'left': self.left,
                       'stop': self.stop}

        try:
            self.speed(int(action.speed))
            actionTable[action.action]
            return "OK"
        except:
            return "KO"


if __name__ == "main":
    
    try:
        robot = Motors()
        svc = rospy.Service('Motion', Motion, robot.move)
    except rospy.ROSInterruptException:
        del robot
        pass

