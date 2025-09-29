import random

number1 = int(random.random()*10)
number2 = int(random.random()*10)
answer = input(f'What is {number1} + {number2}?: ')

try:
    answer_int = int(answer)
    if(number1 + number2 == answer_int):
        print('Well done')
    else:
        print('Sorry, try another time')
except ValueError:
    print('This is not a number.')