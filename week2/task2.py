user_input_year = input("Enter a year: ")
result_string = ''

try:
    user_input_int = int(user_input_year)
    divisable_by_four = False
    if((user_input_int % 4 == 0 and user_input_int % 100 != 0) or user_input_int % 400 == 0):
        result_string += f'{user_input_int} is a leap year'
        divisable_by_four = True
    else:
        result_string += f'{user_input_int} is not a leap year.'

except ValueError:
    print("Please enter valid year!")

print(result_string)
