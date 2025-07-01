#ifndef AUDIO_PROCESSING_H
#define AUDIO_PROCESSING_H

#include <iostream>
#include <vector> 


std::vector<double> lowPassFilter(const std::vector<double> &input, int windowsSize, bool lpFilter);
std::vector<double> highPassFilter(const std::vector<double> &input, const std::vector<double> &averageValue);



#endif