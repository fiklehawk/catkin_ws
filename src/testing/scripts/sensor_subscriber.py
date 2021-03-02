#!/usr/bin/env python3

import rospy
from testing.msg import sensor_info


class Subscriber:
    def __init__(self):
        self.Listener()

    def Callback(self,data):
        self.distance = data.distance
        self.objectName = data.objectName
        rospy.loginfo('Distance reading from the %s is: %s'%(data.objectName, data.distance))

    def Listener(self):
        rospy.init_node('Sensof_info_Subscriber', anonymous=False)
        rospy.Subscriber('sensor_info', sensor_info, self.Callback)
        rospy.spin()

if __name__ == '__main__':
    a = Subscriber()