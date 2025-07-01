#include "binding.h"


void bind_audio_processing(py::module_ &m){
    m.def("low_pass_filter", &lowPassFilter, "Simple moving average filter");
    m.def("high_pass_filter", &highPassFilter, "Calculate HPF");
}

//module python module name "audio processing to import in python"
PYBIND11_MODULE(audio_processing, m){
    bind_audio_processing(m);
}
