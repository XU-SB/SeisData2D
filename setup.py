from setuptools import setup, find_packages

setup(
    name="seismic_tool",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "seismic_tool=seismic_tool.cli:main",
        ],
    },
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",  # Removed obspy, added matplotlib
    ],
)

