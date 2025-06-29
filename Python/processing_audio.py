import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../build")))
import audio_processing

def performProcessing(data, window_size):
    print("[Debug - performProcessing] Enter function")
    filtered = audio_processing.low_pass_filter(data.tolist(), window_size)
    print("[Debug - performProcessing] Enter function")
    return filtered
