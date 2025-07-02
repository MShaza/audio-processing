import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../build")))
#import audio_processing
build_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build"))
print(f"[Debug] Adding to sys.path: {build_path}")
print(f"[Debug] Files in build folder: {os.listdir(build_path)}")

sys.path.append(build_path)

import audio_processing

def performProcessing(data, window_size, filter_type):
    print("[Debug - performProcessing] Enter function")
    ##lpFilter = False
    filtered = audio_processing.low_pass_filter(data.tolist(), window_size, filter_type)
    print("[Debug - performProcessing] Enter function")
    return filtered
