# file: tests/test_processing.py
import numpy as np
from seismic_tool.processing import apply_bandpass, apply_agc

def test_apply_bandpass():
    # Test case for bandpass filtering
    data = np.random.randn(1000)
    filtered_data = apply_bandpass(data, lowcut=10, highcut=50, fs=1000)
    assert len(filtered_data) == len(data)

def test_apply_agc():
    # Test case for AGC
    data = np.random.randn(1000)
    agc_data = apply_agc(data)
    assert len(agc_data) == len(data)

