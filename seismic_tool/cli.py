# file: seismic_tool/cli.py
import argparse
from .data_io import load_segy
from .processing import apply_bandpass, apply_agc

def main():
    parser = argparse.ArgumentParser(description="Seismic Data Processing Tool")
    parser.add_argument("file", type=str, help="Path to SEG-Y file")
    parser.add_argument("--filter", type=str, choices=["bandpass"], help="Type of filter to apply")
    parser.add_argument("--lowcut", type=float, help="Low cut frequency for bandpass filter")
    parser.add_argument("--highcut", type=float, help="High cut frequency for bandpass filter")
    parser.add_argument("--fs", type=float, default=1000, help="Sampling frequency")
    parser.add_argument("--agc", action="store_true", help="Apply automatic gain control")

    args = parser.parse_args()
    data = load_segy(args.file)

    if args.filter == "bandpass":
        data = apply_bandpass(data, args.lowcut, args.highcut, args.fs)

    if args.agc:
        data = apply_agc(data)

    # Save or display results here
    print("Processing complete.")

if __name__ == "__main__":
    main()
