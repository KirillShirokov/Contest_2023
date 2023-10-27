import random


def quick_sort(list_players):
    lenght = len(list_players)
    if lenght <= 1:
        return list_players
    else:
        pivot_dot = random.randint(0, lenght - 1)
        pivot = int(list_players[pivot_dot][1])
        print(pivot)
        left = []
        middle = []
        right = []
        for i, _ in enumerate(list_players):
            iteration_value = int(list_players[i][1])
            if  iteration_value < pivot:
                left.append(list_players[i])
            if  iteration_value > pivot:
                right.append(list_players[i])
            else:
                middle.append(list_players[i])
        sort_data = quick_sort(left) + middle + quick_sort(right)
        print(sort_data)

def result():
    pass

if __name__ == '__main__':
    number_of_players = int(input())
    list_players = [0] * number_of_players
    for i in range(number_of_players):
        name, points, fines = input().split()
        list_players[i] = [name, points, fines]
    print(list_players)
    quick_sort_list = quick_sort(list_players)


    
