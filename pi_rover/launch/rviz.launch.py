
from webbrowser import get
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    package_share_dir = get_package_share_directory("pi_rover")
    urdf_file_path = os.path.join(package_share_dir, "urdf", "udemy_bot.urdf")
    return LaunchDescription([
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='jsp_node',
        ), 
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='rsp_node',
            arguments=[urdf_file_path]
        ),               
        Node(
            package='rviz2',
            executable='rviz2',
            name='simulation_in_rviz'
        ),
        
        
    ])