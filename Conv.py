import os

# Set the directory path where the CSV files are located

directory = '/path/to/csv/files/'

# Loop through all files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        # Open the file in read mode with the encoding set to UTF-8
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            # Read the contents of the file and convert it to UTF-16LE encoding
            contents = f.read().encode('utf-16le')

        # Open the same file in write mode with the encoding set to UTF-16LE
        with open(os.path.join(directory, filename), 'wb') as f:
            # Write the contents to the file
            f.write(contents)