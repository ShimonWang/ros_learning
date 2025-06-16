#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 该例程将发布/person_info话题，自定义消息类型learning_topic::Person

import rospy
from learning_topic.msg import Person


def person_publisher():
    rospy.init_node('person_publisher', anonymous=True)

    person_info_pub = rospy.Publisher('/person_info', Person, queue_size=10)

    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        
        person_msg = Person()
        person_msg.name = "Tom"
        person_msg.age = 18
        person_msg.sex = Person.male

        person_info_pub.publish(person_msg)
        rospy.loginfo("Publish person message[%s, %d %d]",
                   person_msg.name, person_msg.age, person_msg.sex)
        
        rate.sleep()


if __name__ == '__main__':
    try:
        person_publisher()
    except rospy.ROSInterruptException:
        pass