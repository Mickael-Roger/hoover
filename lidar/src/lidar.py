#!/usr/bin/python3
import PyLidar3
import rospy
from std_msgs.msg import String



class Lidar():

    def __init__(self):
        #Link from /dev/ttyUSB0 to /dev/ydlidar previously made
        self.lidar = PyLidar3.YdLidarX4("/dev/ydlidar") 

        if not self.lidar.Connect():
            rospy.loginfo("Error connecting to the Lidar")
            raise ValueError("Error connecting to the Lidar")

        try:
            self.pub = rospy.Publisher('lidar', String, queue_size=100)
            rospy.init_node('lidar', anonymous=True)
        except:
            raise ValueError("Could not start ROS msg queue")


    def __del__(self):
        self.stop()
        self.lidar.Disconnect()


    def start(self):
        mesurements = self.lidar.StartScanning()
        while True:
            self.pub.publish(str(mesurements))


    def stop(self):
        self.lidar.StopScanning()


if __name__ == '__main__':
    try:
        lidar=Lidar()
        lidar.start()
    except rospy.ROSInterruptException:
        del lidar
        pass
