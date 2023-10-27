'''
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.
'''
def comparate(num1, num2):
    return num1 < num2

def intersection_sort(array, comparate, number):
    for i in range(1, number):
        key_item = array[i]
        j = i - 1
        while j >= 0 and comparate(
            int(array[j] + key_item), int(key_item + array[j])):
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1
    return(''.join(array))


if __name__ == '__main__':
    number = int(input())
    array = input().split(' ')
    print(intersection_sort(array, comparate, number))