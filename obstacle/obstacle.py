#!/usr/bin/python3
import ime
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import String


GPIO.setmode(GPIO.BCM)


class Obstacle():

    def __init__(self():
                
        self.leftTrigger = 18
        self.rightTrigger = 24
        self.leftEcho = 18
        self.rightEcho = 24
        
        GPIO.setup(self.leftTrigger, GPIO.OUT)
        GPIO.setup(self.rightTrigger, GPIO.OUT)
        GPIO.setup(self.leftEcho, GPIO.IN)
        GPIO.setup(self.rightEcho, GPIO.IN)


        try:
            self.pub = rospy.Publisher('obstacle', String, queue_size=100)
            rospy.init_node('obstacle', anonymous=True)
        except:
            raise ValueError("Could not start ROS msg queue")
            
            

    def distance(self):
    
        mesure = {}
        
        for side in [(self.leftTrigger, self.leftEcho, "left"), (self.rightTrigger, self.rightEcho, "right")]:
            trigger=side[0]
            echo=side[1]
            
            GPIO.output(trigger, True)
            time.sleep(0.00001)
            GPIO.output(trigger, False)
 
        StartTime = time.time()
        StopTime = time.time()
 

        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()
 
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()
 
        TimeElapsed = StopTime - StartTime

        distance = (TimeElapsed * 34300) / 2
        
        mesure[side[2]] = distance
 
        return mesure


    def start(self):
        mesures = self.distance()
        while True:
            self.pub.publish(str(next(mesures)))


    def __del__(self):
        GPIO.cleanup()
            

if __name__ == '__main__':
    try:
        obstacle=Obstacle()
        obstacle.start()
    except rospy.ROSInterruptException:
        del obstacle
        pass
