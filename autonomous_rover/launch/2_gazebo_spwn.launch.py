import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    # robot state publisher
    
    urdf_file_name = 'rrbot.urdf'
    urdf_file = os.path.join(
        get_package_share_directory('autonomous_rover'),
        urdf_file_name)

    doc = xacro.parse(open(urdf_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}
    #rviz_config_file=os.path.join(get_package_share_directory('autonomous_rover'), 'view.rviz')
    controllers_file = os.path.join(  get_package_share_directory('autonomous_rover'),  'controllers',  'control_me.yaml')
    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                get_package_share_directory('gazebo_ros'), 'launch'), '/gazebo.launch.py']),
             )

    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'rrbot'],
                        output='screen')
    joint_state_publisher = Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            
            parameters=[robot_description])
    
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description]
    )
    rviz2= Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        #arguments=['-d',rviz_config_file],
        output='screen')

    controller_manager = Node(
    package="controller_manager",
    executable="ros2_control_node",
    parameters=[
        robot_description,
        controllers_file
    ],
    output='screen'
    )
    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity,
        joint_state_publisher,
        controller_manager,
        #rviz2,
    ])