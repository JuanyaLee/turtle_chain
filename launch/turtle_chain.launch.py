from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        Node(
            package='turtle_chain',
            executable='chain_manager',
            name='chain_manager',
            output='screen'
        )

    ])
