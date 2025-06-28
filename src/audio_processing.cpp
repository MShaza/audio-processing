#include "audio_processing.h"

std::vector<double> lowPassFilter(const std::vector<double> &input, int WindowSize){
    std::cout<<"[Debug - lowPassFilter] Enter function."<<std::endl;
    std::vector<double> output;
    int counter = 0;
    double averageSum = 0;
    double average = 0;
    if(input.size() <= 0){
        return output;
    }
     std::cout<<"[Debug - lowPassFilter] Calculate moving average."<<std::endl;
    for(int i = 0 ; i < input.size(); i++){
        int j = i;
        while(j >= 0 && counter < WindowSize){
            averageSum += input[j];
            counter ++;
            // std::cout<<"[Debug - lowPassFilter] counter:"<< counter<<std::endl;
            j = j -1;
        }
        average =  averageSum/counter;
        //std::cout<<"[Debug - lowPassFilter] average:"<< average<<std::endl;
        output.push_back(average);
        averageSum = 0;
        counter = 0;
    }
    std::cout<<"[Debug - lowPassFilter] Function ended successfully."<<std::endl;
    return output;
}