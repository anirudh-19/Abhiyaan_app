#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic

import rospy
import os
import sys
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


def callback(pose):
    pos1x=pose.x
    pos1y=pose.y
        
def callback1(pose):
    pos2x=pose.x
    pos2y=pose.y

def talker():



    rospy.init_node('turtle', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    vel1=Twist()
    vel2=Twist()
    
        
    pos1x = int(input("X coordinate of turtle1: "))
    pos1y = int(input("Y coordinate of turtle1: "))
    
    lvx1 = int(input("X velocity of turtle1: "))
    lvy1 = int(input("Y velocity of turtle1: "))
    
    lvx2 = int(input("X velocity of turtle 2: "))
    lvy2 = int(input("Y velocity of turtle 2: "))
 
        
    pos2x = int(input("X coordinate of turtle2: "))
    pos2y = int(input("Y coordinate of turtle2: "))
    
    pub2 = rospy.Publisher('/turtle2/cmd_vel',Twist, queue_size=10)
    pub3 = rospy.Publisher('/turtle3/cmd_vel',Twist, queue_size=10)
    

   
        
    
    os.system(" ".join(("rosservice call /spawn",str(pos1x),str(pos1y),"0","turtle2")))
    os.system(" ".join(("rosservice call /spawn",str(pos2x),str(pos2y),"0","turtle3")))
    os.system(" ".join(("rosservice call /kill", '"turtle1"')))
    
    
    
    while not rospy.is_shutdown():
    
       
        
        rospy.Subscriber('/turtle2/pose', Pose, callback)
        rospy.Subscriber('/turtle3/pose', Pose, callback1)
        
        vel1.linear.x = lvx1
        vel1.linear.y = lvy1
        vel1.linear.z = 0
        
        vel1.angular.x = 0
        vel1.angular.y = 0
        vel1.angular.z = 0   
        
        vel2.linear.x = lvx2
        vel2.linear.y = lvy2
        vel2.linear.z = 0
        
        vel2.angular.x = 0
        vel2.angular.y = 0
        vel2.angular.z = 0  
        
        a= pos2x-pos1x
        b= pos2y-pos1y
        
        
        c=(a**2 + b**2)**0.5
        
        
        r = (a)**2 + (b)**2
        
        p= (-1)*(40/r) #taking G*m as 20, some arbitary value
        
        if pos2y>pos1y:
            p= (-1)*p #attractive force.
        
        a2x= p*(a/c) #cos theta
        a2y= p*(b/c) #sin theta
        
        a1x= -1*(a2x) 
        a1y= -1*(a2y)
        
        lvx1+= a1x*0.1
        lvx2+= a2x*0.1
        
        lvy1+= a1y*0.1
        lvy2+= a2y*0.1
        
        pub2.publish(vel1)
        pub3.publish(vel2)
        
        rate.sleep()
        
        
 

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
        

