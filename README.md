# Didi-Udacity-Challenge

#![Alt text](didi_challenge_dataset.gif?raw=true "Optional Title")

TESTED ON UBUNTU 16.04 and ROS KINETIC


Install ROS http://www.ros.org/ 

Create a catkin workspace http://wiki.ros.org/catkin/Tutorials/create_a_workspace

Be sure to have your build-essential "sudo apt-get update && sudo apt-get install build-essential"

enter in your catkin worspace and in your src folder "cd catkin_ws/src" and git clone this repository

be sure to have all the rosdep "rosdep install --from-paths src --ignore-src --rosdistro kinetic"

catkin_make

Launch the roslaunch comand and specify the pat on your rosbag folder: 
"roslaunch launchPKG display_rosbag_rviz.launch rosbag_file:=/path/to/your/rosbag" 



