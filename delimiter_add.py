import argparse

def add_delimiter_to_file(input_file_path, output_file_path, delimiter="----"):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            outfile.write(line.rstrip('\n') + '\n' + delimiter + '\n')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a delimiter after each line of a file.")
    parser.add_argument("input_file", help="Path to the input file")
    parser.add_argument("output_file", help="Path to the output file")
    args = parser.parse_args()

    add_delimiter_to_file(args.input_file, args.output_file)
