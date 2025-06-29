import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from processing_audio import performProcessing

def plot_data(originalData, filteredData):
    print("[Debug - plot_data] Enter function")
    plt.plot(originalData[:500], label="Original", alpha=0.6)
    plt.plot(filteredData[:500], label="Filtered", alpha=0.8)
    plt.legend()
    plt.title("Low-Pass Filter on Audio Signal")
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()
    print("[Debug - plot_data] Exit function")

if __name__ == '__main__':
    print("[Debug - main] Reading file")
    rate, data = wavfile.read("example.wav")
    print("[Debug - main] Check if mono or stereo")
    if len(data.shape) == 2:
        data = data.mean(axis=1)
    print("[Debug - main] Check data type")
    if(data.dtype != np.float32 and data.dtype != np.float64):
        data = data/npiinfo(data.dtype).max
    window_size = 3
    print("[Debug - main] Calling function low_pass_filter")
    filtered = performProcessing(data, window_size)
    print("[Debug - main] Filtered data recieved")
    print("[Debug - main] Plotting")
    plot_data(data, filtered)
    print("[Debug - main] Writting output to file")
    filtered_array = np.array(filtered)
    filtered_int16 = np.int16(filtered_array / np.max(np.abs(filtered_array)) * 32767)
    wavfile.write("filtered_output.wav", rate, filtered_int16)



