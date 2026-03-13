# File Operations in Python

# Function to write data to a file with exception handling
def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as file:
            file.write(data)
            print('Data written successfully.')
    except Exception as e:
        print(f'Error writing to file: {e}')

# Function to read data from a file with exception handling
def read_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except Exception as e:
        print(f'Error reading from file: {e}')
        return None

# Function to append data to a file with exception handling
def append_to_file(file_name, data):
    try:
        with open(file_name, 'a') as file:
            file.write(data)
            print('Data appended successfully.')
    except Exception as e:
        print(f'Error appending to file: {e}')

# Test the functions
if __name__ == '__main__':
    file_path = 'C:\temp\sample.txt'
    write_to_file(file_path, 'Hello, World!\n')
    print('Data written to file:')
    print(read_from_file(file_path))
    append_to_file(file_path, 'Appending this line.\n')
    print('Data after appending:')
    print(read_from_file(file_path))