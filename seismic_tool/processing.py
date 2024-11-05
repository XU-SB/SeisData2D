# file: seismic_tool/processing.py
import numpy as np
from scipy.signal import butter, filtfilt

def apply_bandpass(data, lowcut, highcut, fs, order=4):
    """
    Apply a bandpass filter to seismic data.
    """
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    filtered_data = filtfilt(b, a, data)
    return filtered_data

def apply_agc(data, window=100):
    """
    Apply automatic gain control (AGC) to seismic data.
    """
    envelope = np.abs(data)
    gain = np.convolve(envelope, np.ones(window)/window, mode='same')
    return data / (gain + 1e-6)

