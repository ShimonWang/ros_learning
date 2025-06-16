#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import roslib
roslib.load_manifest('learning_tf')
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
    
if __name__ == '__main__':
    # 初始化ROS节点
    rospy.init_node('turtle_tf_listener')
      # rospy.init_node(name, anonymous=False):name:节点名称，anonymous:不记名的，这样可以运行很多不关心名称的节点

    rospy.loginfo("turtle_tf_listener started, spawning turtle2 and listening tf...")  # 写入日志消息

    # 创建TF监听器
    listener = tf.TransformListener()

    rospy.wait_for_service('spawn')  # 阻塞直到服务可用
    # rospy.wait_for_service(service, timeout=None) 等待服务可用
    spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
    # rospy.ServiceProxy(name, service_class, persistent=False, headers=None)
    # 创建一个可用的服务代理 name:服务名字，service_class:服务类，persistent:持久连接，headers:服务连接头信息
    spawner(4, 2, 0, 'turtle2')

    turtle_vel = rospy.Publisher('/turtle2/cmd_vel', geometry_msgs.msg.Twist, queue_size=1)
    # pub = rospy.Publisher('topic_name', std_msgs.msg.String, queue_size=10) 主题名称，Message类，队列大小

    rate = rospy.Rate(10.0)
    # rospy 提供了一个方便的类，该类尽力保持循环的特定速率。
    while not rospy.is_shutdown():
    # ROS 中测试关闭的最常见用法模式是：
    # spin() 代码简单地休眠，直到 is_shutdown() 标志被 True 。它主要用于防止你的 Python 主线程退出。
        try:
            (trans, rot) = listener.lookupTransform('/turtle2', '/turtle1', rospy.Time(0))
            # transform from frame /turtle1 to frame /turtle2 坐标系/turtle1变换到/turtle2
            # ros::Time(0) 将只获取最新的可用变换
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            # LookupException:当 tf 方法尝试访问一个坐标系，但该坐标系不在图中时引发
            # ConnectivityException:当请求的坐标系与固定坐标系未连接时引发
            # ExtrapolationException:当 tf 方法需要超出当前限制进行外推时引发
            continue
        angular = 4 * math.atan2(trans[1], trans[0])
        linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
        cmd = geometry_msgs.msg.Twist()
        cmd.linear.x = linear
        cmd.angular.z = angular
        turtle_vel.publish(cmd)

        rate.sleep()
        # rospy.sleep(duration) 会睡眠指定的时间