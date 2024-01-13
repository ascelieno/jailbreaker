import argparse

def convert_double_quotes_to_single(input_file_path, output_file_path):
    with open(input_file_path, 'r') as file:
        content = file.read()
        converted_content = content.replace('"', "'")

    with open(output_file_path, 'w') as file:
        file.write(converted_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert double quotes to single quotes in a file.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')

    args = parser.parse_args()

    convert_double_quotes_to_single(args.input_file, args.output_file)
