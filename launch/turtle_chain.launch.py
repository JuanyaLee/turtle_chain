from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():

    return LaunchDescription([

        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim'
        ),

        Node(
            package='chain_follow',
            executable='follower_node',
            name='follower'
        ),

        Node(
            package='chain_follow',
            executable='chain_manager',
            name='manager'
        )
    ])