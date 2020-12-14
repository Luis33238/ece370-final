rosservice call gazebo/delete_model dd_robot
rosrun gazebo_ros spawn_model -file models_robot.sdf -sdf -model dd_robot -y 0 -x 0 -z 0
