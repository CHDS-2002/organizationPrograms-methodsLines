# os - библиотека для работы с консолью
import os

# Зададим цвет шрифта консоли - голубой
os.system('COLOR B')

# Введём в переменную my_string произвольный текст
# с консоли
try:
    my_string = input()  # my_string - строка
except:
    my_string = ''
    # присваиваем пустую строку в случае пустого ввода

# Зададим информацию о строке
COUNT_LINES = len(my_string)
# COUNT_LINES - количество символов строки
UPPER = my_string.upper()
# UPPER - строка в верхнем регистре
LOWER = my_string.lower()
# LOWER - строка в нижнем регистре
new_my_string = my_string.replace(' ', '')
# new_my_string - строка без пробелов
FIRST = my_string[0] if my_string else ''
# FIRST - первый символ строки
LAST = my_string[-1] if my_string else ''
# LAST - последний символ строки

# Выведем информацию о строке
print('\nИНФОРМАЦИЯ О СТРОКЕ', my_string, end=':\n\n')
print('Количество символов:', COUNT_LINES, end='.\n')
print('Строка', my_string, 'в верхнем регистре:', UPPER, end='.\n')
print('Строка', my_string, 'в нижнем регистре:', LOWER, end='.\n')
print('Строка', my_string, 'без пробелов:', new_my_string, end='.\n')
print('Первый символ строки ', my_string, ': ', FIRST, sep='', end='.\n')
print('Последний символ строки ', my_string, ': ', LAST, sep='', end='.\n\n')

try:
    os.system('PAUSE')  # Останавливаем работу программы
    os.system('CLS')  # Очищаем экран консоли
except:
    os.system('CLS')  # Очищаем экран консоли
