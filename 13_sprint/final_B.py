from random import randint


def quick_sort(data_in):
    lenght = len(data_in)
    if lenght <= 1:
        return data_in
    else:
        data = list(data_in.items())
        *_, pivot = data[randint(0, lenght - 1)]
        left = {}
        middle = {}
        right = {}
        for key, value in data_in.items():
            if int(value) < int(pivot):
                left[key] = value
            elif int(value) > int(pivot):
                right[key] = value
            else:
                middle[key] = value
        sort_data = {**left, **middle, **right}
        print(left)
        print(middle)
        print(right)
        print(pivot)
        return sort_data

def result(dict1, dict2):
    print(dict1)
    print(dict2)
    for key, value in dict1.items():
        if value == dict2[key]:
            print('USPECH')

if __name__ == '__main__':
    number_of_players = int(input())
    points_list = {}
    fines_list = {}
    for i in range(number_of_players):
        name, points, fines = input().split()
        points_list[name] = points
        fines_list[name] = fines
    points_list = quick_sort(points_list)
    fines_list = quick_sort(fines_list)
    result(points_list, fines_list)
