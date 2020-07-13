#!/bin/bash

mydir=`pwd`

if [ -d ~/catkin_ws ]
then
	echo "Catkin workspace already exists. Backing it up"
	mv ~/catkin_ws ~/catkin_ws.`date +%s`
fi

mkdir -p ~/catkin_ws/src
cd ~/catkin_ws

catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
source devel/setup.bash

cd ~/catkin_ws/src
catkin_create_pkg lidar std_msgs rospy

cp -rf $mydir/lidar/src/* ~/catkin_ws/src/lidar/src/
