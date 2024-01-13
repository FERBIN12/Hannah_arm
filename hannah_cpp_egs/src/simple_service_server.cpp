#include <rclcpp/rclcpp.hpp>


class SimpleServiceServer : public rclcpp :: Node
{
public:
    SimpleServiceServer() : Node("simple_service_server")
    {

    }
private:
    rclcpp::Service<>::SharedPtr service_;



};