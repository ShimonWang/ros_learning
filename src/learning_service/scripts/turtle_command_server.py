#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 该例程将执行/turtle_command服务，服务数据类型std_srvs/Trigger

import rospy
import threading, time, _thread
from geometry_msgs.msg import Twist
from std_srvs.srv import Trigger, TriggerResponse

pubCommand = False
turtle_vel_pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)

def command_thread():
    while True:
        if pubCommand:
            vel_msg = Twist()
            vel_msg.linear.x = 0.5
            vel_msg.angular.z = 0.2
            turtle_vel_pub.publish(vel_msg)

        time.sleep(0.1)

def commandCallback(req):
    global pubCommand
    pubCommand = not pubCommand

    # 显示请求数据
    rospy.loginfo(f"Publish turtle velocity command![{pubCommand}]")

    # 反馈数据
    return TriggerResponse(success=True, message="python, Change turtle command state!")

def turtle_command_server():
    # ROS节点初始化
    rospy.init_node('turtle_command_server')
    
    # 创建一个名为/turtle_command的server，注册回调函数commandCallback
    s = rospy.Service('/turtle_command', Trigger, commandCallback)  # rospy.Service(name, service_class, handler, buff_size=65536)
    
    # 循环等待回调函数
    print("Ready to receive turtle command.")

    _thread.start_new_thread(command_thread, ())  # 多线程
    # threading.Thread(target=command_thread, daemon=True).start()
    rospy.spin()

if __name__ == "__main__":
    turtle_command_server()