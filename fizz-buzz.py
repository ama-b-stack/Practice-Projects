#!/usr/bin/env python3.7

upper_number = int(input('how many values should we process: '))

for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('fizzbuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)
