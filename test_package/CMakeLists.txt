cmake_minimum_required(VERSION 2.8.12)
project(PackageTest CXX)

find_package(PkgConfig)
pkg_check_modules(squashfuse REQUIRED IMPORTED_TARGET squashfuse)

add_executable(example example.cpp)
target_link_libraries(example PkgConfig::squashfuse)
