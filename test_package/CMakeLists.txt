cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

message("CMAKE_PREFIX_PATH ${CMAKE_PREFIX_PATH}")
find_package(PkgConfig)
pkg_search_module(squashfuse REQUIRED IMPORTED_TARGET squashfuse)

add_executable(example example.cpp)
target_link_libraries(example PkgConfig::squashfuse)
