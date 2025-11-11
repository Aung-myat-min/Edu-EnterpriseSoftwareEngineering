def read_file():
    file_name = input("Enter file name: ")
    reader = open(file_name, 'r')
    lines = reader.readlines()
    print(lines)

read_file()