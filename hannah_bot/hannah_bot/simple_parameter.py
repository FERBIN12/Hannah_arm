import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rcl_interfaces.msg import SetParametersResult
from rclpy.parameter import Parameter

class SimpleParameter(Node):
    def __init__(self):
        super().__init__("SimplePublisher")
        self.declare_parameter("simple_int_param", 28)
        self.declare_parameter("simple_string_param", "Ferbin")
        self.add_on_set_parameters_callback(self.paramchange_callback)

    def paramchange_callback(self, params):
        result = SetParametersResult(successful=True)  # Initialize result as successful.

        for param in params:
            if param.name == "simple_int_param" and param.type_ == Parameter.Type.INTEGER:
                self.get_logger().info("Simple int parameter changed! with name set to %d" % param.value)
                # Use param.value to access the parameter value.
                result.successful = True

            if param.name == "simple_string_param" and param.type_ == Parameter.Type.STRING:
                self.get_logger().info("Simple string parameter changed! with name %s set to %s" % (param.name, param.value))
                # Use param.name and param.value to access the parameter name and value.
                result.successful = True

        return result

def main():
    rclpy.init()  # Instantiate the communication with ROS
    simple_parameter = SimpleParameter()
    rclpy.spin(simple_parameter)
    simple_parameter.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
