#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import rospy
from turtlesim.srv import Spawn

def turtle_spawn():
    rospy.init_node('turtle_spawn')
    rospy.wait_for_service('/spawn')
    try:
        add_turtle = rospy.ServiceProxy('/spawn', Spawn)

        response = add_turtle(2.0, 2.0, 0.0, "turtle2")
        return response.name
    except rospy.ServiceException as e:
        # print("Service call failed: %s" % e)
        print(f"Service call failed:{e}")

if __name__ == '__main__':
    # print("Spawn turtle sucessfully [name:%s]" % (turtle_spawn()))
    print(f"Spawn turtle sucessfully [name:{turtle_spawn()}]")