#ifndef BINDING_H
#define BINDING_H
#include <iostream>
#include "audio_processing.h"
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  
#include <vector> 
namespace py = pybind11;
void bind_audio_processing(py::module_ &m);

#endif