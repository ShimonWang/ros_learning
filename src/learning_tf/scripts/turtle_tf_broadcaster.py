#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import roslib
roslib.load_manifest('learning_tf')
import tf.transformations
import rospy

import tf
import turtlesim.msg

def handle_turtle_pose(msg, turtlename):
    br = tf.TransformBroadcaster()  # 创建tf.TransformBroadcaster()实例
    # 处理函数针对turtle的位置信息广播平移和旋转，作为变换，从“world”坐标系到“turtleX”坐标系进行发布
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")
    
if __name__ == '__main__':
    # 初始化ROS节点
    rospy.init_node('turtle_tf_broadcaster')  # anonymous=True:表示每个节点具有唯一名称
    turtlename = rospy.get_param('~turtle')  # rospy.get_param(param_name):从参数服务器获取值
    # 此节点接受一个名为“turtle”的单个参数
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)  # rospy.Subscriber("chatter", String, callback)
    rospy.spin()  # 阻塞，直到 ROS 节点关闭。将活动让给其他线程。