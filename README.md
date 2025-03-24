## Hannah - Robotic Manipulator


This project features a robotic manipulator built using ROS2 Humble, Ignition Gazebo, and MoveIt2 for motion planning. The OMPL (Open Motion Planning Library) is utilized for path planning, ensuring efficient and collision-free trajectories. The system enables real-time simulation, kinematic control, and motion execution, making it ideal for robotic manipulation tasks in dynamic environments.

Software: ROS2 humble 
OS: UBUNTU 22.04 

ROS2 packages used so far:

->ros2_control

Project Description:

  Hannah is a voice controlled robot made using ROS2 framework , for the initial face I'm testing out the control logic in a simualted enviornment called gazebo

Present progress:

  - Created urdf for the manipultor ,intergrated them with gazebo

  launch file code:

        ros2 launch hannahbot_description gazebo_launch.py 

  ![image](https://github.com/user-attachments/assets/901796a1-d1c4-400e-ac87-45e3c796e406)

In terminal 2: run controller : 

     ros2 launch hannahbot_controller controller.launch.py 
Then run moveit launch file:

    ros2 launch hannahbot_moveit moveit.launch.py 
![image](https://github.com/user-attachments/assets/adeedb1b-c977-4ea9-9cdf-595d87fae509)


