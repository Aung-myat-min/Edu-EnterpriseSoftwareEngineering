# GET AND READ FILE
def read_file(file_name):
    try:
        lines = []
        file = open(file_name, 'r')
        for line in file.readlines():
            lines.append(line)
        return lines
    except FileNotFoundError:
        print("Such a file does not exist!")
        return []

# GET LINE BY LINE AND RETURN COUNT & LINE
def count_words(line_array):
    if len(line_array) == 0: print("Empty Lines!")
    for line in line_array:
        list_line = line.strip().split(" ")
        stripped_list = [x for x in list_line if x.strip()]
        print(f"{len(stripped_list)} {line}")

file_name = input("Please enter file name: ")
count_words(read_file(file_name))