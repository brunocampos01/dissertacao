import rclpy
from rclpy.node import Node


# template
class MyNode(Node):

    def __init__(self):
        super().__init__('py_test')
        self.counter = 0
        self.get_logger().info('hello world')
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.counter += 1
        self.get_logger().info(f'test {self.counter}')


def main(args=None):
    rclpy.init(args=args)  # initialyze comunication
    node = MyNode()  # create a node
    rclpy.spin(node)  # Execute work a context associated how a loop: while
    rclpy.shutdown()  # end communication


if __name__ == '__main__':
    main()
