from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    node = Node(
        package='gdb_test_pkg',
        executable='gdb_test_node',
        name='gdb_test_node',
        prefix=['gdb -ex run --args'],
        output='screen')

    ld = LaunchDescription()

    ld.add_action(node)

    return ld
