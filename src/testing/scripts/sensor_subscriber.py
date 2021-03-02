#!/usr/bin/env python3

import rospy
from testing.msg import sensor_info


class Subscriber:
        
    def Callback(self,data):
        self.distance = data.distance
        self.objectName = data.objectName
        # rospy.loginfo('Distance reading from the %s is: %s'%(data.objectName, data.distance))
    
    def readData(self):
        rospy.init_node('Sensof_info_Subscriber', anonymous=False)
        rospy.Subscriber('sensor_info', sensor_info, self.Callback)
        # rospy.spin()
        rospy.sleep(0.5)
        return [self.distance, self.objectName]

if __name__ == '__main__':
    sn = Subscriber()
    while True:
        try:
            d, n = sn.readData()

            print("Distance from %s is %s"%(n,d))
            break
        except AttributeError:
            print("Attribute Error")