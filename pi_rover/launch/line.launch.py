import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    package_share_dir = get_package_share_directory("pi_rover")
    urdf_file_path = os.path.join(package_share_dir, "urdf","udemy_bot_lf.urdf")
    world_file_path = os.path.join(package_share_dir, "worlds","kreislauf.world")
    urdf = open(urdf_file_path).read()


    return LaunchDescription(
        [
            ExecuteProcess(
                cmd=["gazebo","--verbose",world_file_path,"-s","libgazebo_ros_factory.so",],
                output="screen",
            ),
            Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='jsp_node',
            ),

            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                parameters=[{'robot_description': urdf}],
            ),
            Node(
                package="gazebo_ros",
                executable="spawn_entity.py",
                arguments=["-topic","robot_description",
                           "-entity","udemy_bot","-Y","1.57"],
                output= 'screen'
            ),
        ]
    )