#!/usr/bin/env python3.7

value = int(input('enter an integer value: '))

if value % 5 == 0 and value % 3 == 0:
    print('fizzbuzz')
elif value % 3 == 0:
    print('fizz')
elif value % 5 == 0:
    print('buzz')
else:
    pass #lab wrote print(value), either way
