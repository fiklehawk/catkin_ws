#!/usr/bin/env python3

import rospy
from testing.msg import sensor_info


def Publisher():
    si_publisher = rospy.Publisher('sensor_info', sensor_info, queue_size = 10)
    rospy.init_node('Sensor_Publisher', anonymous=False)
    rate = rospy.Rate(1)

    # Create a new SensorInformation object and fill in its contents.
    Sensor_Data= sensor_info()
    Sensor_Data.distance = 4.5
    Sensor_Data.objectName = "Ball"
    while not rospy.is_shutdown():
        # Publish the sensor information on the /sensor_info topic.
        si_publisher.publish(Sensor_Data)
        # Print log message if all went well.
        rospy.loginfo("All went well. Publishing topic")
        rate.sleep()

if __name__ == '__main__':
    try:
        Publisher()
    except rospy.ROSInterruptException:
        pass