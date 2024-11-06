# file: seismic_tool/cli.py
import argparse
from .data_io import load_data, plot_data
from .processing import apply_bandpass, apply_agc

def main():
    parser = argparse.ArgumentParser(description="Seismic Data Processing Tool")
    parser.add_argument("file", type=str, help="Path to data file (e.g., CSV or .npy format)")
    parser.add_argument("--filter", type=str, choices=["bandpass"], help="Type of filter to apply")
    parser.add_argument("--lowcut", type=float, help="Low cut frequency for bandpass filter")
    parser.add_argument("--highcut", type=float, help="High cut frequency for bandpass filter")
    parser.add_argument("--fs", type=float, default=1000, help="Sampling frequency")
    parser.add_argument("--agc", action="store_true", help="Apply automatic gain control")
    parser.add_argument("--plot", action="store_true", help="Plot the processed data")

    args = parser.parse_args()
    
    # Load data from the file
    data = load_data(args.file)

    # Apply bandpass filter if specified
    if args.filter == "bandpass":
        if args.lowcut is None or args.highcut is None:
            print("Error: --lowcut and --highcut must be specified for bandpass filter.")
            return
        data = apply_bandpass(data, args.lowcut, args.highcut, args.fs)

    # Apply automatic gain control if specified
    if args.agc:
        data = apply_agc(data)

    # Plot the data if specified
    if args.plot:
        plot_data(data)

    print("Processing complete.")

if __name__ == "__main__":
    main()
