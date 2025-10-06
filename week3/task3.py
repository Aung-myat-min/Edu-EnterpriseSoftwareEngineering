total = 0
number = 0
while(number < 20):
    number += 1
    print(' The value of number is ', number)

    if(number % 2 != 0):
        total += number
    else:
        continue

    total += number

print('The total is ', total)