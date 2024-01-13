import argparse

def extract_response(line):
    # Adjusting for escaped newline characters
    start_marker = "### RESPONSE:\\n"
    end_marker = '}]'
    start_idx = line.find(start_marker)
    if start_idx != -1:
        print("Debug: Start marker found")
        start_idx += len(start_marker)
        end_idx = line.find(end_marker, start_idx)
        if end_idx != -1:
            print("Debug: End marker found")
            response = line[start_idx:end_idx].replace('\\n', '\n').strip()  # Replace escaped newlines with actual newlines
            print("Debug: Extracted response:", repr(response))
            return response
        else:
            print("Debug: End marker not found")
    else:
        print("Debug: Start marker not found")
    return None

def process_file(input_file_path, output_file_path, delimiter='----'):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        for line in infile:
            response = extract_response(line)
            if response:
                outfile.write(response + "\n")
                outfile.write(delimiter + "\n")
            else:
                print("Debug: No response extracted")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Extract responses from a file and write them to another file with delimiters.')
    parser.add_argument('input_file', type=str, help='Path to the input file')
    parser.add_argument('output_file', type=str, help='Path to the output file')
    args = parser.parse_args()

    process_file(args.input_file, args.output_file)
