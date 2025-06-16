#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import rospy
from std_srvs.srv import Empty

def parameter_config():
    rospy.init_node('parameter_config', anonymous=True)

    red = rospy.get_param('/turtlesim/background_r')
    green = rospy.get_param('/turtlesim/background_g')
    blue = rospy.get_param('/turtlesim/background_b')

    rospy.loginfo("Get Background Color[%d, %d, %d]", red, green, blue)

    red = rospy.set_param('/turtlesim/background_r', 255)
    green = rospy.set_param('/turtlesim/background_g', 255)
    blue = rospy.set_param('/turtlesim/background_b', 255)

    rospy.loginfo("Set Background Color[255, 255, 255]")

    red = rospy.get_param('/turtlesim/background_r')
    green = rospy.get_param('/turtlesim/background_g')
    blue = rospy.get_param('/turtlesim/background_b')

    rospy.loginfo("Get Background Color[%d, %d, %d]", red, green, blue)

    rospy.wait_for_service('clear')
    try:
        clear_background = rospy.ServiceProxy('clear', Empty)
        
        response = clear_background()
        return response
    except rospy.ServiceException as e:
        print("Service call failed:%s" %e)

if __name__ == "__main__":
    parameter_config()
