/**
 * 该历程将发布turtle/cmd_vel话题，消息类型geometry_msgs::Twist
 */

#include <ros/ros.h>                // 包含ROS库头文件
#include <geometry_msgs/Twist.h>    // 包含geometry_msgs::Twist消息类型

int main(int argc, char *argv[])
// argc:整数,用来统计你运行程序时送给main函数的命令行参数的个数
// * argv[ ]: 指针数组，用来存放指向你的字符串参数的指针，每一个元素指向一个参数
{
    // ROS节点初始化
    ros::init(argc, argv, "velocity_publisher");
    //ros::init(argc, argv, "my_node_name", ros::init_options::AnonymousName);
    //node_name:将分配的节点名称；opotions:这是一个可选参数，允许您指定某些选项来改变 roscpp 的行为。

    // 创建节点句柄
    ros::NodeHandle n;

    // 创建一个Publisher，发布为/turtle1/cmd_vel的topic，消息类型为geometry_msgs::Twist，队伍长度10
    ros::Publisher turtle_vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    //ros::Publisher advertise(const std::string& topic, uint32_t queue_size, bool latch = false);
    //topic:要发布的主题；queue_size:出站消息的大小

    // 设置循环的频率
    ros::Rate loop_rate(10);  // ros::Rate:该类尽力维持一个特定的循环速率

    int count = 0;  // 计数器，暂时未使用

    while(ros::ok())
    {
        // 初始化geometry_msgs::Twist类型的消息
        geometry_msgs::Twist vel_msg;
        vel_msg.linear.x = 0.5;
        vel_msg.angular.z = 0.2;

        // 发布消息
        turtle_vel_pub.publish(vel_msg);
        //void ros::Publisher::publish(const M & message) const:发布与此 Publisher 关联的主题上的消息。
        //ros::Publisher::publish ros::Publisher类的一个成员函数，用于将消息发送到与该发布者关联的话题。
        //M是一个模板类型，表示消息的类型。M &message 表示函数参数 message 是消息的引用，& 表示这是一个引用，避免了消息的复制，提高了效率。
        //const 表示该参数是常量引用，意味着 publish() 函数内部不能修改传入的消息内容。
        ROS_INFO("Publish turtle velocity command[%0.2f m/s, %0.2f rad/s]",
                    vel_msg.linear.x, vel_msg.angular.z);

        // 设置循环频率延时
        loop_rate.sleep();
    }

    return 0;  // 程序正常结束
}
