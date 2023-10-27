'''
Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода
Выведите двоичное представление этого числа.
'''
def to_binary(number: int) -> str:
	result = []
	if number == 0:
		return 0
	while number > 0:
		result.append(number % 2)
		number = number // 2
	result.reverse()
	new_list = list(map(str, result))
	result2 = ''.join(new_list)
	return result2

def read_input() -> int:
	return int(input().strip())

print(to_binary(read_input()))