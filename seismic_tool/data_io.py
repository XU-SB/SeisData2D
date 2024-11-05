# file: seismic_tool/data_io.py
import numpy as np
import matplotlib.pyplot as plt

def load_data(file_path):
    """
    Load data from a CSV or NumPy file.
    """
    # For example, load from a CSV file
    data = np.loadtxt(file_path, delimiter=',')
    return data

def plot_data(data):
    """
    Simple plotting function for seismic data.
    """
    plt.imshow(data, aspect='auto', cmap='seismic')
    plt.colorbar()
    plt.title("Seismic Data Plot")
    plt.xlabel("Trace")
    plt.ylabel("Time Sample")
    plt.show()
