# ROSCOnJP 2019

## Dependencies

* Gazebo 9
* ROS 2 Dashing
* [SimSlides](https://github.com/chapulina/simslides)
* [Dolly](https://github.com/chapulina/dolly)

## Build

1. Install ROS Dashing as instructed [here](https://index.ros.org/doc/ros2/Installation/Linux-Install-Debians/).

1. Install `gazebo_ros_pkgs`, which also installs Gazebo:

       sudo apt install ros-dashing-gazebo-ros-pkgs

1. Build this package together with Dolly and SimSlides:

       mkdir -p ws/src
       cd ws/src
       git clone https://github.com/chapulina/simslides -b master
       git clone https://github.com/chapulina/dolly -b master
       git clone https://github.com/chapulina/rosconjp_2019 -b master
       cd ..
       colcon build

## Run

    . /usr/share/gazebo/setup.sh
    . ~/ws/install/setup.sh
    ros2 launch rosconjp_2019 rosconjp.launch.py

