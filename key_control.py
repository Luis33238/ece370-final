import rospy
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties

msg_topic = '/gazebo/apply_joint_effort'
joint_front_left = 'dd_robot::front_left_wheel_hinge'
joint_front_right = 'dd_robot::front_right_wheel_hinge'
joint_back_left = 'dd_robot::back_left_wheel_hinge'
joint_back_right = 'dd_robot::back_right_wheel_hinge'

start_time = rospy.Time(0.0)
end_time = rospy.Time(3.77)

startpause = rospy.Time(0.0)
endpause = rospy.Time(1.0)

startturn = rospy.Time(0.0)
endturn = rospy.Time(10)

startreturn = rospy.Time(0.0)
endreturn = rospy.Time(1.0)

end_time = rospy.Time(3.765)
rospy.init_node('dd_ctrl', anonymous=True)
pub = rospy.ServiceProxy(msg_topic,ApplyJointEffort)
msg_topic_feedback = '/gazebo/get_joint_properties'

pub_feeback = rospy.ServiceProxy(msg_topic_feedback, GetJointProperties)

while True:
    data = raw_input("Input robot control: ")
    print data
    if(data == "w"):
        pub(joint_front_left, 2, start_time, end_time)
        pub(joint_front_right, 2, start_time, end_time)
        pub(joint_back_left, 2, start_time, end_time)
        pub(joint_back_right, 2, start_time, end_time)
    elif(data == "s"):
        pub(joint_front_left, -2, startpause, endpause)
        pub(joint_front_right, -2, startpause, endpause)
        pub(joint_back_left, -2, startpause, endpause)
        pub(joint_back_right, -2, startpause, endpause)
    elif(data == "a"):
        pub(joint_front_left, 1, startreturn, endreturn)
        pub(joint_front_right, 1, startreturn, endreturn)
        pub(joint_back_left, 1, startreturn, endreturn)
        pub(joint_back_right, 1, startreturn, endreturn)
    elif(data == "t"):
        pub(joint_front_left, -5, startpause, endpause)
        pub(joint_front_right, -5, startpause, endpause)
        pub(joint_back_left, -5, startpause, endpause)
        pub(joint_back_right, -5, startpause, endpause)
    else:
        pub(joint_front_left, 2.5, start_time, end_time)
        pub(joint_front_right, -2.5, start_time, end_time)
        pub(joint_back_left, 2.5, start_time, end_time)
        pub(joint_back_right, -2.5, start_time, end_time)
