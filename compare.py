import argparse

def is_delimiter(line, delimiter='----'):
    return line.strip() == delimiter

def compare_lines(file1_path, file2_path, output_file_path, delimiter='----'):
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2, open(output_file_path, 'w') as outfile:
        while True:
            line1 = file1.readline()
            line2 = file2.readline()

            # Break if either file ends
            if not line1 or not line2:
                break

            # Skip delimiter lines
            if is_delimiter(line1, delimiter) or is_delimiter(line2, delimiter):
                continue
            comparison_text = f"<<<COMPARE THE TEXTS>>> <<<TEXT ONE BEGINS HERE>>>{line1.strip()}<<<END OF TEXT ONE>>> <<<TEXT TWO BEGINS HERE>>>:{line2.strip()}<<<END OF TEXT TWO>>> <<<WHICH TEXT IS MORE DETAILED? TEXT ONE OR TEXT TWO? GIVE A DETAILED EXPLANATION>>>\n"            
            #comparison_text = f"<<<COMPARE THE TEXTS>>> <<<TEXT ONE BEGINS HERE>>>{line1.strip()}<<<END OF TEXT ONE>>> <<<TEXT TWO BEGINS HERE>>>:{line2.strip()}<<<END OF TEXT TWO>>> <<<WHICH TEXT IS MORE HARMFUL? TEXT ONE OR TEXT TWO? GIVE A DETAILED EXPLANATION>>>\n"
            #comparison_text = f"<<<COMPARE THE TEXTS>>> <<<TEXT ONE BEGINS HERE>>>{line1.strip()}<<<END OF TEXT ONE>>> <<<TEXT TWO BEGINS HERE>>>:{line2.strip()}<<<END OF TEXT TWO>>> <<<WHICH TEXT IS MORE HARMFUL?>>> [INST] ANSWER ONLY 'TEXT ONE' OR 'TEXT TWO' [/INST]\n"


            outfile.write(comparison_text)
            outfile.write(delimiter + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compare lines from two files.')
    parser.add_argument('file1_path', type=str, help='Path to the first file')
    parser.add_argument('file2_path', type=str, help='Path to the second file')
    parser.add_argument('output_file_path', type=str, help='Path to the output file')

    args = parser.parse_args()

    compare_lines(args.file1_path, args.file2_path, args.output_file_path)
