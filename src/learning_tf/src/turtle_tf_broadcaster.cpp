#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <turtlesim/Pose.h>

std::string turtle_name;  // std::string: c++中字符串类

void poseCallback(const turtlesim::PoseConstPtr& msg)
{
    // 创建tf的广播器
    static tf::TransformBroadcaster br;

    // 初始化tf数据
    tf::Transform transform;
    transform.setOrigin(tf::Vector3(msg->x, msg->y, 0.0));
    tf::Quaternion q;
    q.setRPY(0, 0, msg->theta);
    transform.setRotation(q);

    // 广播world与海龟坐标系之间的tf数据
    br.sendTransform(tf::StampedTransform(transform, ros::Time::now(), "world", turtle_name));
}

// int main(int argc, char *argv[])
int main(int argc, char** argv)
// argc:整数,用来统计你运行程序时送给main函数的命令行参数的个数
// * argv[ ]: 指针数组，用来存放指向你的字符串参数的指针，每一个元素指向一个参数
{
    // 初始化ROS节点
    ros::init(argc, argv, "my_tf_broadcaster");

    // 输入参数作为海龟的节点
    if(argc!=2)
    {
        ROS_ERROR("need turtle name as argument");
        return -1;
    }
    
    turtle_name = argv[1];

    // 订阅海龟的位姿话题
    ros::NodeHandle node;
    ros::Subscriber sub = node.subscribe(turtle_name+"/pose", 10, &poseCallback);

    // 循环等待回调函数
    ros::spin();

    return 0;
}
