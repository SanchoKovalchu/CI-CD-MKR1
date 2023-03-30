def read_file(file_name):
    # Open the input file
    with open(file_name, 'r') as f:
        # Read the contents of the file
        contents = f.read()
    return contents

if __name__ == "__main__":
    contents = read_file("input.txt")
    print(contents)