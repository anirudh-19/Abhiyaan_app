#this also is just a source citation that i modified to get the output. 

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('/team_abhiyaan', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Team Abhiyaan Rocks: %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
