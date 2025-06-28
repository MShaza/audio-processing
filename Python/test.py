import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../build")))

import  audio_processing

data = [1.0, 2.0, 4.0, 5.0, 6.0]
window = 3

result =  audio_processing.low_pass_filter(data, window)
print(result)