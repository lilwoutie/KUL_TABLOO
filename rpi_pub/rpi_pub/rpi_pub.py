import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class RPIPublisher(Node):
    def __init__(self):
        super().__init__('rpi_manual_publisher')
        
        # Create a publisher for the 'rpi_topic'
        self.publisher_ = self.create_publisher(String, 'rpitopic', 10)

    def publish_message(self, message):
        """Publishes a manually entered message to the 'rpi_topic'"""
        msg = String()
        msg.data = message
        self.publisher_.publish(msg)
        self.get_logger().info(f'Published: {msg.data}')


def main():
    rclpy.init()
    node = RPIPublisher()
    
    try:
        while rclpy.ok():
            message = input("Enter message to publish: ")
            if message.lower() == "exit":
                break
            node.publish_message(message)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
