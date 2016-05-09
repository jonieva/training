cmake_minimum_required(VERSION 3.4)
project(temp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set(SOURCE_FILES mylists.h)
add_executable(temp main.cpp ${SOURCE_FILES})