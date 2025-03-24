import os
import launch
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from moveit_configs_utils import MoveItConfigsBuilder
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    is_sim_arg = DeclareLaunchArgument(
        "is_sim",
        default_value="True"
    )

    is_python_arg =  DeclareLaunchArgument(
        "use_python",
        default_value="False"
    )

    is_sim = LaunchConfiguration("is_sim")
    use_python = LaunchConfiguration("use_python")

    moveit_config = (
        MoveItConfigsBuilder("hannahbot", package_name="hannahbot_moveit")
        .robot_description(file_path=os.path.join(
            get_package_share_directory("hannahbot_description"),
            "urdf",
            "hannahbot.urdf.xacro"
            )
        )
        .robot_description_semantic(file_path="config/hannahbot.srdf")
        .trajectory_execution(file_path="config/moveit_controllers.yaml")
        .moveit_cpp(file_path="config/planning_python_api.yaml")
        .to_moveit_configs()
    )

    task_server_python = Node(
        package="hannah_bot",
        executable="simple_service_server",
        condition= launch.conditions.IfCondition(use_python),
        parameters=[moveit_config.to_dict(),
                    {"use_sim_time": is_sim}]
    )

    task_server_cpp = Node(
        package="hannabot_remote",
        executable="task_server_node",
        condition= launch.conditions.UnlessCondition(use_python),
        parameters=[{"use_sim_time": is_sim}]
    )

    return LaunchDescription([
        is_sim_arg,
        is_python_arg,
        task_server_python, 
        task_server_cpp,  
    ])