#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 该例程将发布一个turtle/cmd_vel话题，消息类型为geometry_msgs::Twist

import rospy
from geometry_msgs.msg import Twist


def shutdown_hook():
    rospy.loginfo("用户中断退出")

def velocity_publisher():
    # ROS节点初始化
    rospy.init_node('velocity_publisher', anonymous=True)
    #rospy.init_node(name, anonymous=False):name:节点名称，anonymous:不记名的，这样可以运行很多不关心名称的节点

    # 创建一个Publisher，发布名为/turtle1/cmd_vel的topic，消息类型为geometry_msg::Twist，队列长度10
    turtle_vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    #pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10) 主题名称，Message类，队列大小

    # 设置循环的频率
    rate = rospy.Rate(10)  # rospy 提供了一个方便的类，该类尽力保持循环的特定速率。

    while not rospy.is_shutdown():
    #ROS 中测试关闭的最常见用法模式是：
    #spin() 代码简单地休眠，直到 is_shutdown() 标志被 True 。它主要用于防止你的 Python 主线程退出。
        # 初始化geometry_msgs::Twist类型的消息
        vel_msg = Twist()
        vel_msg.linear.x = 0.5
        vel_msg.angular.z = 0.2

        # 发布消息
        turtle_vel_pub.publish(vel_msg)
        rospy.loginfo("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                   vel_msg.linear.x, vel_msg.angular.z)  # 写入日志消息
        # rospy.loginfo("已经修改过代码")

        # 按照循环频率延时
        rate.sleep()  # rospy.sleep(duration) 会睡眠指定的时间



if __name__ == '__main__':
    try:
        rospy.on_shutdown(shutdown_hook)  # 在节点关闭时调用shutdown_hook
        velocity_publisher()
    except rospy.ROSInterruptException:  # ROSInterruptException:用于中断操作的异常
        pass
