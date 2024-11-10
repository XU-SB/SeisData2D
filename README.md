# SeisData2D

SeisData2D is an open-source Python package created by Dr. Xu Shibo, offering tools for processing and analyzing 2D seismic datasets. Designed for geophysicists and researchers, this package aims to simplify the workflow for loading, manipulating, and visualizing seismic data. The package includes a variety of useful functionalities for 2D seismic data processing, such as data loading, common offset and shot gathers visualization, and basic seismic data manipulation.

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
- Load 2D seismic data in common formats (e.g., SEG-Y)
- Extract and visualize shot gathers, CMP gathers, and stacked sections
- Simple data manipulation including scaling, filtering, and trace editing
- Display seismic data with customizable visualization settings

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

