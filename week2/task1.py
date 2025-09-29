user_input = input("Enter a number: ")
result_string = ''

try:
    user_input_int = int(user_input)
    divisable_by_two = False
    if(user_input_int % 2 == 0):
        result_string += f'{user_input_int} is divisible by 2 '
        divisable_by_two = True
    else:
        result_string += f'{user_input_int} is not divisible by 2 '
    
    if(user_input_int > 5):
        result_string += 'AND, ' if(divisable_by_two) else 'BUT, '
        result_string += 'is larger than 5.'
    else:
        result_string += 'BUT, ' if(divisable_by_two) else 'AND, '
        result_string += 'is less than 5.'

except ValueError:
    print("Please enter valid number!")

print(result_string)
