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
catkin_create_pkg hoover std_msgs rospy
catkin_create_pkg mapping std_msgs rospy

cp -rf $mydir/lidar/src/* ~/catkin_ws/src/lidar/src/
cp -rf $mydir/hoover/src/* ~/catkin_ws/src/hoover/src/
cp -rf $mydir/mapping/src/* ~/catkin_ws/src/mapping/src/
chmod +x ~/catkin_ws/src/lidar/src/lidar.py ~/catkin_ws/src/hoover/src/hoover.py ~/catkin_ws/src/mapping/src/mapping.py
