#!/bin/bash

mydir=`pwd`

source /opt/ros/melodic/setup.bash

if [ -d ~/catkin_ws ]
then
	echo "Catkin workspace already exists. Backing it up"
	mv ~/catkin_ws ~/catkin_ws.`date +%s`
fi

mkdir -p ~/catkin_ws/src/hoover/srv
cd ~/catkin_ws

catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
source devel/setup.bash

cd ~/catkin_ws/src
catkin_create_pkg hoover std_msgs rospy message_generation message_runtime

cp -rf $mydir/obstacle/src/* ~/catkin_ws/src/hoover/src/
cp -rf $mydir/lidar/src/* ~/catkin_ws/src/hoover/src/
cp -rf $mydir/motors/src/* ~/catkin_ws/src/hoover/src/
cp -rf $mydir/hoover/src/* ~/catkin_ws/src/hoover/src/
cp -rf $mydir/mapping/src/* ~/catkin_ws/src/hoover/src/
chmod +x ~/catkin_ws/src/hoover/src/*.py

mkdir -p ~/catkin_ws/src/hoover/srv/
cp -rf $mydir/srv/Motion.srv ~/catkin_ws/src/hoover/srv/

echo "add_service_files(
   FILES
   Motion.srv
 )" >> ~/catkin_ws/src/hoover/CMakeLists.txt

