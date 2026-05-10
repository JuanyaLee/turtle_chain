import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from turtle_chain.follower import Follower


class ChainManager(Node):

    def __init__(self):
        super().__init__('chain_manager')

        # master turtle
        self.chain = ['turtle1']

        # 保存 follower nodes
        self.followers = []

        # 监听新抓到的 turtle
        self.subscription = self.create_subscription(
            String,
            '/caught_turtle',
            self.caught_callback,
            10
        )

        self.get_logger().info(
            'Chain Manager Started'
        )

    def caught_callback(self, msg):

        new_turtle = msg.data

        # 防止重复加入
        if new_turtle in self.chain:
            return

        # 前一个 turtle
        target_turtle = self.chain[-1]

        self.get_logger().info(
            f'{new_turtle} will follow {target_turtle}'
        )

        # 创建 follower
        follower_node = Follower(
            follower_name=new_turtle,
            target_name=target_turtle
        )

        # 保存 follower
        self.followers.append(follower_node)

        # 加入 chain
        self.chain.append(new_turtle)

        self.get_logger().info(
            f'Current Chain: {self.chain}'
        )


def main(args=None):

    rclpy.init(args=args)

    manager = ChainManager()

    executor = rclpy.executors.MultiThreadedExecutor()

    executor.add_node(manager)

    # 所有 follower nodes 也加入 executor
    try:
        while rclpy.ok():

            for follower in manager.followers:
                executor.add_node(follower)

            executor.spin_once(timeout_sec=0.1)

    except KeyboardInterrupt:
        pass

    finally:

        manager.destroy_node()

        for follower in manager.followers:
            follower.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()
