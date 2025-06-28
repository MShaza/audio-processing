import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../build")))
import audio_processing


rate, data = wavfile.read("example.wav")
if len(data.shape) == 2:
    data = data.mean(axis=1)
if(data.dtype != np.float32 and data.dtype != np.float64):
    data = data/npiinfo(data.dtype).max

window_size = 3
filtered = audio_processing.low_pass_filter(data.tolist(), window_size)
plt.plot(data[:500], label="Original", alpha=0.6)
plt.plot(filtered[:500], label="Filtered", alpha=0.8)
plt.legend()
plt.title("Low-Pass Filter on Audio Signal")
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.grid()
plt.show()
