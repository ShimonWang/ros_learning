#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 该例程将订阅/person_info话题，自定义消息类型learning_topic::Person

import rospy
from learning_topic.msg import Person

def personInfoCallback(msg):
    rospy.loginfo("Publish person message[%s, %d %d]",
            msg.name, msg.age, msg.sex)
    
def person_publisher():
    rospy.init_node('person_subscriber', anonymous=True)

    rospy.Subscriber('/person_info', Person, personInfoCallback)

    rospy.spin()


if __name__ == '__main__':
    person_publisher()