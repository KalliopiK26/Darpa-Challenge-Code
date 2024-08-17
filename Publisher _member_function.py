import rclpy
import random
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Point

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Point()
        
        msg.x = random.uniform(0,100)
        msg.y = random.uniform(0,100)
        msg.z = random.uniform(0,100)
        
        output = String()
        output.data = f'x={msg.x}, y={msg.y}, z={msg.z}'
        
        self.publisher_.publish(output)
        self.get_logger().info('Publishing: "%s"' % output.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)  # Keeps the node running and processing events
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
