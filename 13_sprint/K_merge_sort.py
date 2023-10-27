'''
Гоше дали задание написать красивую сортировку слиянием. Поэтому Гоше обязательно надо реализовать отдельно функцию merge и функцию merge_sort.
Функция merge принимает два отсортированных массива, сливает их в один отсортированный массив и возвращает его. Если требуемая сигнатура имеет вид merge(array, left, mid, right), то первый массив задаётся полуинтервалом 
[
l
e
f
t
,
m
i
d
)
 массива array, а второй – полуинтервалом 
[
m
i
d
,
r
i
g
h
t
)
 массива array.
Функция merge_sort принимает некоторый подмассив, который нужно отсортировать. Подмассив задаётся полуинтервалом — его началом и концом. Функция должна отсортировать передаваемый в неё подмассив, она ничего не возвращает.
Функция merge_sort разбивает полуинтервал на две половинки и рекурсивно вызывает сортировку отдельно для каждой. Затем два отсортированных массива сливаются в один с помощью merge.
Заметьте, что в функции передаются именно полуинтервалы 
[
b
e
g
i
n
,
e
n
d
)
, то есть правый конец не включается. Например, если вызвать merge_sort(arr, 0, 4), где 
a
r
r
=
[
4
,
5
,
3
,
0
,
1
,
2
]
, то будут отсортированы только первые четыре элемента, изменённый массив будет выглядеть как 
a
r
r
=
[
0
,
3
,
4
,
5
,
1
,
2
]
.
Реализуйте эти две функции.
'''
def merge(arr, lf, mid, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	result = []
	left = arr[lf:mid]
	right = arr[mid:rg]
	ileft = iright = 0
	while len(result) < len(left) + len(right):
		if left[ileft] <= right[iright]:
			result.append(left[ileft])
			ileft += 1
		else:
			result.append(right[iright])
			iright += 1
		if iright == len(right):
			result += left[ileft:]
			break
		if ileft == len(left):
			result += right[iright:]
			break
	return result


def merge_sort(arr, lf, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	if rg - lf >= 2:
		mid = (lf + rg) // 2
		merge_sort(arr, lf, mid)
		merge_sort(arr, mid, rg)
		arr[lf:rg] = merge(arr, lf, mid, rg)

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected
	
if __name__ == '__main__':
	test()