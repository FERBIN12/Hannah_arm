import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class simplesubscriber(Node):
    def __init__(self):
        super().__init__("Simple_Subscriber")
        self.sub=self.create_subscription(String,"Chatter",self.msgcallback,10)


    def msgcallback(self,msg):
        self.get_logger().info("I heard: %s" % msg.data)


def main():
    rclpy.init()
    Simple_subscriber = simplesubscriber()
    rclpy.spin(Simple_subscriber)
    Simple_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
        



