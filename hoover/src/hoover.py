import rospy
from std_msgs.msg import String


class Hoover():

    def __init__(self):
        rospy.init_node('hoover', anonymous=True)


    def start(self):
        # Listen to Lidar
        rospy.Subscriber("lidar", String, self.lidarMessage)
        rospy.spin()

    def lidarMessage(self, data):
        rospy.loginfo(rospy.get_caller_id() + "%s", data.data)


if __name__ == '__main__':
    try:
        hoover = Hoover()
        hoover.start()
    except rospy.ROSInterruptException:
        del listen
        pass

