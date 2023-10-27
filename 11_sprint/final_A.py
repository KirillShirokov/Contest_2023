'''
Тимофей ищет место, чтобы построить себе дом. Улица, на которой он хочет жить, имеет длину n, то есть состоит из n одинаковых идущих подряд участков. Каждый участок либо пустой, либо на нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице. Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого участка. Если участок пустой, эта величина будет равна нулю — расстояние до самого себя.

Помогите Тимофею посчитать искомые расстояния. Для этого у вас есть карта улицы. Дома в городе Тимофея нумеровались в том порядке, в котором строились, поэтому их номера на карте никак не упорядочены. Пустые участки обозначены нулями.

Формат ввода
В первой строке дана длина улицы —– n (1 ≤ n ≤ 106). В следующей строке записаны n целых неотрицательных чисел — номера домов и обозначения пустых участков на карте (нули). Гарантируется, что в последовательности есть хотя бы один ноль. Номера домов (положительные числа) уникальны и не превосходят 109.
'''
# ID 88861933
from typing import List, Tuple


def result_func(length, number_house):
    result = nearest_empty(length, number_house)
    return result

def calculate_distance(length: int, number_house: List[int]) -> List[int]:
    distance = []
    empty_position = None
    for i, value in enumerate(number_house):
        if value == 0:
            empty_position = i
            distance.append(0)
        elif empty_position is not None:
            distance.append(i - empty_position)
        else:
            distance.append(length)
    return distance

def nearest_empty(length: int, number_house: List[int]) -> List[int]:
    distance = calculate_distance(length, number_house)
    distance_reverse = calculate_distance(length, reversed(number_house))
    distance_reverse.reverse()
    result = []
    for step in range(length):
        result.append(min(distance[step], distance_reverse[step]))
    return result

def read_input() -> Tuple[int, List[int]]:
    length = int(input())
    number_house = [int(num) for num in input().split(' ')]
    return length, number_house

if __name__ == '__main__':
    length, number_house = read_input()
    print(*(result_func(length, number_house)))
