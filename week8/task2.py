# ask for user valid input
import os.path


def input_values():
    while True:
        user_input = input("Enter a negative number and a character separated by a space: ")
        try:
            input_value = user_input.strip().split(" ")
            if len(input_value) == 2 and input_value[0].replace('-', '').isdecimal():
                if int(input_value[0]) < 0:
                    return input_value
            else:
                print("don’t write the values to the file in this case")
        except:
            print("dont write the values to the file in this case")

# main function
def main():
    while True:
        file_name = input("Enter the file name: ")
        if os.path.isfile(file_name):
            file = open(file_name, 'a')
            user_input = input_values()
            file.write(f'{user_input[0]}  {user_input[1].upper()}\n')
            file.close()
            print("good bye")
            return
        else:
            print("file does not exist")

main()