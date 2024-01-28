import argparse

def is_delimiter(line, delimiter='----'):
    return line.strip() == delimiter

def read_until_delimiter(file, delimiter='----'):
    text = ''
    while True:
        line = file.readline()
        if not line or is_delimiter(line, delimiter):
            break
        text += line
    return text.strip()

def compare_texts(file1_path, file2_path, output_file_path, delimiter='----'):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as outfile:
        while True:
            text1 = read_until_delimiter(file1, delimiter)
            text2 = read_until_delimiter(file2, delimiter)

            # Break if either file ends
            if not text1 or not text2:
                break

            comparison_text = (f"<<<COMPARE THE TEXTS>>> <<<TEXT ONE BEGINS HERE>>>{text1}<<<END OF TEXT ONE>>> "
                               f"<<<TEXT TWO BEGINS HERE>>>:{text2}<<<END OF TEXT TWO>>> "
                               f"<<<WHICH TEXT IS MORE DETAILED? TEXT ONE OR TEXT TWO? GIVE A DETAILED EXPLANATION>>>\n")

            outfile.write(comparison_text)
            outfile.write(delimiter + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare texts from two files.')
    parser.add_argument('file1_path', type=str, help='Path to the first file')
    parser.add_argument('file2_path', type=str, help='Path to the second file')
    parser.add_argument('output_file_path', type=str, help='Path to the output file')
    
    args = parser.parse_args()

    compare_texts(args.file1_path, args.file2_path, args.output_file_path)
