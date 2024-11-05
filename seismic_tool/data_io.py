# file: seismic_tool/data_io.py
import obspy

def load_segy(file_path):
    """
    Load a SEG-Y file and return the data array.
    """
    stream = obspy.read(file_path, format="SEGY")
    data = [trace.data for trace in stream]
    return data

