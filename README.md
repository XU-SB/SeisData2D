# SeisData2D

SeisData2D is an open-source Python package created by Dr. Xu Shibo from ENEOS Xplora, offering tools for processing and analyzing 2D seismic datasets. Designed for geophysicists and researchers, this package aims to simplify the workflow for loading, manipulating, and visualizing seismic data. The package includes a variety of useful functionalities for 2D seismic data processing, such as data loading, common offset and shot gathers visualization, and basic seismic data manipulation.

## Installation
To install SeisData2D, first clone the repository:
```bash
git clone https://github.com/XU-SB/SeisData2D.git
```

Navigate to the project directory and install the required dependencies:
```bash
cd SeisData2D
pip install -r requirements.txt
```

## Main Features
- Load 2D seismic data in common formats (e.g., SEG-Y, Binary)
- Extract and visualize shot gathers, CMP gathers, and stacked sections
- Simple data manipulation including scaling, filtering, and trace editing
- Display seismic data with customizable visualization settings

## Additional Features
- **Convolution**: Apply convolution operations for synthetic seismogram generation and data processing.
- **Cross-Correlation**: Perform cross-correlation for similarity analysis, time shifts, and velocity estimation.
- **Signal Processing and Filter Application**: Use a variety of filters (e.g., bandpass, high-pass, low-pass) to enhance seismic data quality.
- **Amplitude Recovery**: Apply amplitude recovery techniques to compensate for energy loss over distance.
- **Velocity Analysis**: Conduct velocity analysis to determine subsurface velocity models for improved imaging.
- **Reverse Time Migration (RTM)**: Use RTM for high-resolution imaging of complex structures.
- **Full Waveform Inversion (FWI)**: Apply FWI techniques to retrieve detailed subsurface properties from seismic data.


## Usage Example
```python
from seisdata2d import SeismicData

# Load seismic data from a SEG-Y file
seismic_data = SeismicData('example.sgy')

# Display a shot gather
seismic_data.plot_shot_gather(shot_number=10)

# Apply bandpass filter to the data
filtered_data = seismic_data.bandpass_filter(frequencies=[5, 10, 40, 50])
```

## Dependencies
- Python >= 3.8
- ObsPy
- NumPy
- Matplotlib

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. Make sure to check out the contribution guidelines in `CONTRIBUTING.md`.

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.

## Contact
For any questions or to report issues, please contact the project owner at: xushibo11@gmail.com

## Development Status
SeisData2D is actively being developed, with planned feature additions including advanced seismic processing functions, such as migration, NMO correction, and data inversion.

