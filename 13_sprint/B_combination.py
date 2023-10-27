'''
На клавиатуре старых мобильных телефонов каждой цифре соответствовало несколько букв. Примерно так:

2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов. Напечатайте все комбинации букв, которые можно набрать такой последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.
'''
from itertools import product


BUTTONS = {
    2:'abc',
    3:'def',
    4:'ghi',
    5:'jkl',
    6:'mno',
    7:'pqrs',
    8:'tuv',
    9:'wxyz'
}

def unpacking_button(numbers):
    result = []
    for number in numbers:
        result.append(list(BUTTONS[number]))
    return result

def combination_result(*list_button):
    result = [''.join(i) for i in product(*list_button)]
    return result


if __name__ == '__main__':    
    numbers = list(map(int, input()))
    list_button = unpacking_button(numbers)
    result = (combination_result(*list_button))
    print(*result)
