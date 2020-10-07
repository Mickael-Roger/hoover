#!/usr/bin/python3
import PyLidar3
#import rospy
#from std_msgs.msg import String



class Lidar():

    def __init__(self):
        #Link from /dev/ttyUSB0 to /dev/ydlidar previously made
        self.lidar = PyLidar3.YdLidarX4("/dev/ttyUSB0") 

        if not self.lidar.Connect():
            print("Error connecting to the Lidar")
            raise ValueError("Error connecting to the Lidar")



    def __del__(self):
        self.stop()
        self.lidar.Disconnect()


    def start(self):
        mesurements = self.lidar.StartScanning()
        while True:
            print(str(next(mesurements)))


    def stop(self):
        self.lidar.StopScanning()


if __name__ == '__main__':
    try:
        lidar=Lidar()
        lidar.start()
    except:
        del lidar
        pass
