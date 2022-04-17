import rospy
from std_msgs.msg import String

def callback(data):
    
    mega = data.data
    rospy.loginfo(rospy.get_caller_id() + 'I heard and reversed %s', mega[::-1] )
    rospy.Publisher('/naayihba_maet', String, queue_size=10).publish(mega[::-1])
    rospy.loginfo(mega[::-1])
    rate = rospy.Rate(10)
    rate.sleep()
    

def listener():
    rospy.init_node('modder', anonymous=True)

    rospy.Subscriber('/team_abhiyaan', String, callback)

    rospy.spin()
    
import rospy
from std_msgs.msg import String



if __name__ == '__main__':
    while not rospy.is_shutdown():
        listener()

