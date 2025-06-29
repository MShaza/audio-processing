#ifndef AUDIO_PROCESSING_H
#define AUDIO_PROCESSING_H

#include <iostream>
#include <vector> 


std::vector<double> lowPassFilter(const std::vector<double> &input, int windowsSize);


#endif