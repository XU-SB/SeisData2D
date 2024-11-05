# file: tests/test_data_io.py
import numpy as np
from seismic_tool.data_io import load_data

def test_load_data():
    # Create synthetic test data
    test_data = np.random.rand(100, 100)
    np.savetxt("test.csv", test_data, delimiter=",")

    # Load data and check
    loaded_data = load_data("test.csv")
    assert loaded_data.shape == test_data.shape

