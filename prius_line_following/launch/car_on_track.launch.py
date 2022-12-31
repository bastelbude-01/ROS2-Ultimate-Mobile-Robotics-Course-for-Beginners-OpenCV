from launch import LaunchDescription
from launch.actions import  ExecuteProcess


def generate_launch_description():
 
  return LaunchDescription([
   
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '/home/ros2/udemy_ws/src/ROS2-Ultimate-Mobile-Robotics-Course-for-Beginners-OpenCV/prius_line_following/world/prius_on_track.world'],
            output='screen'),
  
  ])