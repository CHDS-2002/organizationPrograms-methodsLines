# os - library for working with the console
import os

# set the color font of the console - blue
os.system('COLOR B')

# input in the my_string variable arbitrary text
# from the console
try:
    my_string = input()  # my_string - string
except:
    my_string = ''
    # assign an empty string in case of an empty input

# let's set the information about the line
COUNT_LINES = len(my_string)
# COUNT_LINES - the number of characters in the string
UPPER = my_string.upper()
# UPPER - uppercase string
LOWER = my_string.lower()
# LOWER - lowercase string
new_my_string = my_string.replace(' ', '')
# new_my_string - a string without spaces
FIRST = my_string[0] if my_string else ''
# FIRST - the first character of the string
LAST = my_string[-1] if my_string else ''
# LAST - the last character of the string

# let's output information about the string
print('\nINFORMATION ABOUT THE LINE', my_string, end=':\n\n')
print('Number of characters:', COUNT_LINES, end='.\n')
print('The line', my_string, 'in uppercase:', UPPER, end='.\n')
print('The line', my_string, 'in lowercase:', LOWER, end='.\n')
print('The line', my_string, 'without whitespaces:', new_my_string, end='.\n')
print('The first character of the string ', my_string, ': ', FIRST, sep='', end='.\n')
print('The last character of the string ', my_string, ': ', LAST, sep='', end='.\n\n')

try:
    os.system('PAUSE')  # stopping the program
    os.system('CLS')  # clearing the console screen
except:
    os.system('CLS')  # clearing the console screen
