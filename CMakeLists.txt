cmake_minimum_required(VERSION 3.14)
project(audio_signal_processing)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include_directories(include)

# Don't hardcode Python executable path — use -DPython_EXECUTABLE in CLI or CI
find_package(Python REQUIRED COMPONENTS Interpreter Development)

# Dynamically fetch pybind11 cmake path from active Python
execute_process(
  COMMAND ${Python_EXECUTABLE} -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 REQUIRED CONFIG PATHS ${pybind11_DIR})

# Create the pybind11 module
pybind11_add_module(audio_processing
    src/audio_processing.cpp
    src/binding.cpp
)

target_include_directories(audio_processing PRIVATE include)
