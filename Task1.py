# 1. На языке Python реализовать алгоритм (функцию) определения четности целого числа, который будет аналогичен нижеприведенному по функциональности, но отличен по своей сути. 
# Объяснить плюсы и минусы обеих реализаций.
# Python example:
# def isEven(value):
# return value%2==0

def isEven(number: int) -> bool:
    """This function takes the integer number with string format and returns boolean value 
    (True if number is Even, False otherwise)"""
    number = str(number)
    if len(number) > 0 and (number[0] == '-' and number[1:].isdigit() or number.isdigit()):
        return number[-1] in tuple(map(str, range(0, 9, 2)))
    else:
        raise ValueError('Your number is not integer!')

for value in (123, '321', '', 'abcd', '\n', '14', '-196', '12.4', str, (18, 14, '42')):
    try:
        print(isEven(value))
    except ValueError:
        print(f'{value} is not integer number.')