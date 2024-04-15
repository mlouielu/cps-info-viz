import argparse
import pathlib
import pickle

def get_parser():
    parser = argparse.ArgumentParser(description="Convert a .pkl file to a .csv file")
    parser.add_argument("inputs", help="The input .pkl files", nargs="+")
    parser.add_argument("--output-dir", "-o", help="The output .csv file")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()

    if not args.output_dir:
        print("Please specify an output directory")
        return 1


    output_dir = pathlib.Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for input_file in args.inputs:
        input_file = pathlib.Path(input_file)
        df = pickle.load(open(input_file, "rb"))
        df.to_csv(output_dir / f"{input_file.stem}.csv", index=False)


if __name__ == "__main__":
    main()
