import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ChainManager(Node):

    def __init__(self):
        super().__init__('chain_manager')

        self.chain = []

        self.subscription = self.create_subscription(
            String,
            '/caught_turtle',
            self.caught_callback,
            10
        )

    def caught_callback(self, msg):
        turtle_name = msg.data

        self.chain.append(turtle_name)

        self.get_logger().info(
            f'{turtle_name} added to chain.'
        )
        
def main(args=None):
    rclpy.init(args=args)

    node = ChainManager()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()