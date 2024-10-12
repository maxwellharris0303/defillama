# Read the file and remove duplicate lines
def remove_duplicates(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Use a set to remove duplicates while preserving the order
    seen = set()
    unique_lines = []
    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

    # Write the unique lines back to a new file (or overwrite the original)
    with open(output_file, 'w') as file:
        file.writelines(unique_lines)

# Example usage
input_file = 'urls.txt'  # Replace with your file name
output_file = 'output.txt'  # Replace with your desired output file name

remove_duplicates(input_file, output_file)
