cmake_minimum_required(VERSION 3.14)
project(case4_unit_tests CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(GTest REQUIRED)

add_executable(run_tests
    tests_queue.cpp
    tests_heap.cpp
    tests_binary_tree.cpp
)

target_link_libraries(run_tests PRIVATE GTest::gtest GTest::gtest_main pthread)

enable_testing()
add_test(NAME unit_tests COMMAND run_tests)
