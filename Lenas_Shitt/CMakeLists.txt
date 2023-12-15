#----------------------------------------------#
#----konfiguration of the buildsystem CMake----#
#----------------------------------------------#

# minimal version of the buildsystem
cmake_minimum_required(VERSION 3.16)
# Name of the project
project(shitt)

#----------------------------------------------#
#-------------------options--------------------#
#----------------------------------------------#

# Set the C++-Standard to C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
# Optional: Baue mit Debugsymbolen / Optimierung
set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_BUILD_TYPE Release)
# Optional: Prüfe alle Targets auf Speicherlecks
add_compile_options(-fsanitize=address)
add_link_options(-fsanitize=address)


#----------------------------------------------#
#-------------example programms---------------#
#----------------------------------------------#


#add_executable(ex1 examples/ex1.cpp)
#add_executable(ex2 examples/ex2.cpp src/GameManager.cpp)

#add_executable(test extra/test.cpp)


add_executable(voc_trainer voc_trainer.cpp)