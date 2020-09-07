#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String


GPIO.setmode(GPIO.BCM)


class Obstacle():

    def __init__(self):
                
        self.leftTrigger = 11
        self.leftEcho = 13
        self.rightTrigger = 29
        self.rightEcho = 31
        
        GPIO.setup(self.leftTrigger, GPIO.OUT)
        GPIO.setup(self.rightTrigger, GPIO.OUT)
        GPIO.setup(self.leftEcho, GPIO.IN)
        GPIO.setup(self.rightEcho, GPIO.IN)


        try:
            self.pub = rospy.Publisher('obstacle', String, queue_size=100)
            rospy.init_node('obstacle', anonymous=True)
        except:
            raise ValueError("Could not start ROS msg queue")

        print("Init OK")
            
            

    def distance(self):
    
        mesure = {}
        print("Distance")
        
        for side in [(self.leftTrigger, self.leftEcho, "left"), (self.rightTrigger, self.rightEcho, "right")]:
            print("Side : " + str(side))
            trigger=side[0]
            echo=side[1]
            
            GPIO.output(trigger, True)
            time.sleep(0.00001)
            GPIO.output(trigger, False)
 
            StartTime = time.time()
            StopTime = time.time()
 

            while GPIO.input(echo) == 0:
                StartTime = time.time()
 
            while GPIO.input(echo) == 1:
                StopTime = time.time()
 
            TimeElapsed = StopTime - StartTime

            distance = (TimeElapsed * 34300) / 2
        
            mesure[side[2]] = distance
            print("Mesure" + str(side[2]) + " " + str(distance))
 
        return mesure


    def start(self):
        print("Start")
        while True:
            mesures = self.distance()
            print("Mesure : " + str(mesures))
            self.pub.publish(str(mesures))
            time.sleep(1)


    def __del__(self):
        GPIO.cleanup()
            

if __name__ == '__main__':
    try:
        obstacle=Obstacle()
        obstacle.start()
    except rospy.ROSInterruptException:
        del obstacle
        pass
