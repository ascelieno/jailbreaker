import re

def extract_responses_from_file(input_file_path, output_file_path=None):
    # Read the content of the file
    with open(input_file_path, 'r') as file:
        file_content = file.read()

    # Function to extract response texts
    def extract_responses(text):
        responses = []
        # Regular expression to match the required pattern
        matches = re.finditer(r"Response: \[{'generated_text': \"### HUMAN:\n.*?\n\n### RESPONSE:\n(.*?)\"}\]", text, re.DOTALL)
        for match in matches:
            responses.append(match.group(1).strip())
        return responses

    # Extract responses
    extracted_responses = extract_responses(file_content)

    # Output extracted responses
    if output_file_path:
        with open(output_file_path, 'w') as outfile:
            for response in extracted_responses:
                outfile.write(response + "\n")
    else:
        for response in extracted_responses:
            print(response)

# Usage example
input_file_path = 'path_to_your_input_file.txt'  # Replace with your input file path
output_file_path = 'path_to_your_output_file.txt'  # Replace with your output file path, or set to None to print responses

extract_responses_from_file(input_file_path, output_file_path)
