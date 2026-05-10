from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():


    return LaunchDescription([

        Node(
            package='turtle_chain',
            executable='follower',
            name='follower_2',
            parameters=[{
                'follower': 'turtle2',
                'target': 'turtle1'
            }]
        ),

        Node(
            package='turtle_chain',
            executable='follower',
            name='follower_3',
            parameters=[{
                'follower': 'turtle3',
                'target': 'turtle2'
            }]
        ),

        Node(
            package='turtle_chain',
            executable='follower',
            name='follower_4',
            parameters=[{
                'follower': 'turtle4',
                'target': 'turtle3'
            }]
        )

    ])
