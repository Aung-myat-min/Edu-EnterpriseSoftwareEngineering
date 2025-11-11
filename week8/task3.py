# handle dict
def handle_dict(input_dict, key, value):
    try:
        input_dict[key] += value
    except KeyError:
        input_dict[key] = value
    return input_dict

# validate line
def validate_line(line):
    values = line.strip().split(" ")
    if len(values) == 2 and values[0].isdecimal() and values[1].isdecimal():
        return True
    else:
        return False

# main program
def main():
    while True:
        file_name = input("Enter file name: ")
        try:
            opened_file = open(file_name, "r")
        except FileNotFoundError:
            print("File not found")
            continue

        lines = opened_file.readlines()
        line_number = 1
        result_dict = {}

        for line in lines:
            result = validate_line(line)
            if result:
                values = line.strip().split(" ")
                result_dict = handle_dict(result_dict, int(values[0]), int(values[1]))
            else:
                print(f'Line No. {line_number} is empty.')
            line_number += 1
        opened_file.close()

        print(result_dict)
        break

main()