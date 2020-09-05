#!/usr/bin/python3
import rospy
from std_msgs.msg import String
import numpy as np
import math


class Mapping():

    def __init__(self):
        rospy.init_node('mapping', anonymous=True)
        self.position = [1000., 1000.]
        self.map = np.zeros((2000, 2000))


    def start(self):
        # Listen to Lidar
        rospy.Subscriber("lidar", String, self.lidarMessage)
        rospy.spin()


    def lidarMessage(self, data):
        mesure = self.parseMsg(data.data)
        self.updateMap(mesure)
        
        
    def updateMap(self, mesures):
        
        for mesure in mesures:
            distance = int(mesures[mesure])/10
            x = round(self.position[0] + distance)
            y = round(self.position[1] + math.tan(math.degrees(int(mesure))) * distance)
            self.map[x][y] = 1
            
        print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in self.map]))
        print("------------------------------------")
            
        
    def parseMsg(self, msg):
        msg=msg.translate({ord(' '): None, ord('{'): None, ord('}'): None, ord('\n'): None})
        res={}

        for mesure in msg.split(','):
            val=mesure.split(':')
            res[val[0]] = int(val[1]) 

        return res
        
        

if __name__ == '__main__':
    try:
        mapping = Mapping()
        mapping.start()
    except rospy.ROSInterruptException:
        del listen
        pass
