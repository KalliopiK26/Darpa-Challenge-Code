import rclpy
from rclpy.node import Node
import math
from geometry_msgs.msg import Point
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        # Create a subscription to the Point topic
        self.subscription = self.create_subscription(
            Point,
            'topic',
            self.listener_callback,
            10)
        # Create a publisher for the String messages
        self.publisher_ = self.create_publisher(String, 'distance_topic', 10)
        self.subscription  # prevent unused variable warning
        
    def distance(self, x, y, z):
        return math.sqrt(x**2 + y**2 + z**2)

    def listener_callback(self, msg):
        self.get_logger().info('Starting Call Back')
        dist = self.distance(msg.x, msg.y, msg.z)
        self.get_logger().info('Distance calculated')
       
        # Create and populate the String message
        output = String()
        output.data = f'{dist}'
        
        # Log the distance
        self.get_logger().info(f'Distance: "{output.data}"')
        
        # Publish the String message
        self.publisher_.publish(output)
        
def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
