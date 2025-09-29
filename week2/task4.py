import random

number1 = int(random.random()*10)
number2 = int(random.random()*10)
number3 = int(random.random()*10)
random_generated_numbers = [number1, number2, number3]
print(random_generated_numbers)



try:
    matches = 0
    user_input = input('Enter First Number: ')
    user_input2 = input('Enter Second Number: ')
    user_input3 = input('Enter Third Number: ')
    user_input_int = int(user_input)
    user_input2_int = int(user_input2)
    user_input3_int = int(user_input3)
    place_matches = [False, False, False]

    user_input_numbers = [user_input_int, user_input2_int, user_input3_int]

    for i in random_generated_numbers:
        if(i == user_input_int):
            matches += 1
        elif(i == user_input2_int):
            matches += 1
        elif(i == user_input3_int):
            matches += 1
    
    print(matches)
    if(matches > 1):
        for i in range(3):
            for j in range(3):
                # print(i, j)
                print(random_generated_numbers[i] ,user_input_numbers[j])

except ValueError:
    print('One inputted digit is not a number')