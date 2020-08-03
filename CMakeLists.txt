cmake_minimum_required(VERSION 3.5)
project(gdb_test_pkg)

#set(CMAKE_BUILD_TYPE Release) #None, Debug, Release, RelWithDebInfo, MinSizeRel
add_compile_options(-std=c++14 -g)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fpermissive -std=c++14 -g")
set(CMAKE_CXX_STANDARD 14)

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(builtin_interfaces REQUIRED)

include_directories(include)

set(dependencies
  rclcpp
  std_msgs
  std_srvs
  builtin_interfaces
)

add_executable(gdb_test_node src/gdb_test_node.cpp src/main.cpp)

ament_target_dependencies(gdb_test_node
  ${dependencies}
)

#### Install
install(TARGETS gdb_test_node
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY include/
  DESTINATION include
)

install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_export_include_directories(include)
ament_export_dependencies(${dependencies})
ament_package()
