'''
Гоша реализовал структуру данных Дек, максимальный размер которого определяется заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front() работали корректно. Но, если в деке было много элементов, программа работала очень долго. Дело в том, что не все операции выполнялись за O(1). Помогите Гоше! Напишите эффективную реализацию.

Внимание: при реализации используйте кольцевой буфер.

Формат ввода
В первой строке записано количество команд n — целое число, не превосходящее 100000. Во второй строке записано число m — максимальный размер дека. Он не превосходит 50000. В следующих n строках записана одна из команд:

push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов, вывести «error».
push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, вывести «error».
pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
Value — целое число, по модулю не превосходящее 1000.
Формат вывода
Выведите результат выполнения каждой команды на отдельной строке. Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
'''
# ID 89058773

class CustomError(Exception):
    pass


class Deque:
    def __init__(self, n):
        self.__items = [None] * n
        self.__max_size = n
        self.__head = -1
        self.__tail = 0
        self.__size = 0

    def is_full(self):
        return self.__size >= self.__max_size

    def is_empty(self):
        return self.__size == 0

    def get_index(self, index, new):
        return (index + new) % self.__max_size

    def push_front(self, value):
        if self.is_full():
            raise CustomError
        self.__items[self.__head] = value
        self.__size += 1
        self.__head = self.get_index(self.__head, -1)

    def push_back(self, value):
        if self.is_full():
            raise CustomError
        self.__items[self.__tail] = value
        self.__size += 1
        self.__tail = self.get_index(self.__tail, 1)

    def pop_front(self):
        if self.is_empty():
            raise CustomError
        self.__head = self.get_index(self.__head, 1)
        result = self.__items[self.__head]
        self.__size -= 1
        return result

    def pop_back(self):
        if self.is_empty():
            raise CustomError
        self.__tail = self.get_index(self.__tail, -1)
        result = self.__items[self.__tail]
        self.__size -= 1
        return result


def result_func(deque, command, *values):
    try:
        result_method = getattr(deque, command)
        result =  result_method(*values)
    except CustomError:
        result = 'error'
    return result


if __name__ == '__main__':
    command_quantity = int(input())
    max_size=int(input())
    deque = Deque(max_size)
    for _ in range(command_quantity):
        command, *values = input().strip().split('')
        result =  result_func(deque, command, *values)
        if result:
            print(result)
