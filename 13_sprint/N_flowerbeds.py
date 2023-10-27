'''
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. На схеме земельного участка клумбы обозначаются просто горизонтальными отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято n садовников. Каждый из них обрабатывал какой-то отрезок на схеме. Процесс был организован не очень хорошо, иногда один и тот же отрезок или его часть могли быть обработаны сразу несколькими садовниками. Таким образом, отрезки, обрабатываемые двумя разными садовниками, сливаются в один. Непрерывный обработанный отрезок затем станет клумбой. Нужно определить границы будущих клумб.
Рассмотрим примеры.
Пример 1:
Даны 4 отрезка: 
[
7
,
8
]
, 
[
7
,
8
]
 ,
[
2
,
3
]
, 
[
6
,
1
0
]
. Два одинаковых отрезка 
[
7
,
8
]
 и 
[
7
,
8
]
 сливаются в один, но потом их накрывает отрезок 
[
6
,
1
0
]
. Таким образом, имеем две клумбы с координатами 
[
2
,
3
]
 и 
[
6
,
1
0
]
.
Пример 2
Во втором сэмпле опять 4 отрезка: 
[
2
,
3
]
, 
[
3
,
4
]
, 
[
3
,
4
]
, 
[
5
,
6
]
. Отрезки 
[
2
,
3
]
, 
[
3
,
4
]
 и 
[
3
,
4
]
 сольются в один отрезок 
[
2
,
4
]
. Отрезок 
[
5
,
6
]
 ни с кем не объединяется, добавляем его в ответ.

Формат ввода
В первой строке задано количество садовников 
n
. Число садовников не превосходит 
1
0
0
0
0
0
.
В следующих 
n
 строках через пробел записаны координаты клумб в формате: start end, где start —– координата начала, end —– координата конца. Оба числа целые, неотрицательные и не превосходят 
1
0
7
. start строго меньше, чем end.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках. Данные должны выводиться в отсортированном порядке —– сначала клумбы с меньшими координатами, затем —– с бОльшими.
'''
def beds_sort(beds):
    beds.sort()
    bed_index = 0
    beds_result = []
    bed_start, bed_end = beds[bed_index]
    bed_index += 1
    while bed_index < number_of_gardeners:
        if bed_start <= beds[bed_index][0] <= bed_end:
            _, current_end = beds[bed_index]
            bed_index += 1
            if current_end > bed_end:
                bed_end = current_end
        else:
            beds_result.append([bed_start, bed_end])
            bed_start, bed_end = beds[bed_index]
            bed_index += 1
    beds_result.append([bed_start, bed_end])
    for result in beds_result:
        print(*result)            


if __name__ == '__main__':
    number_of_gardeners = int(input())
    beds = [0] * number_of_gardeners
    for i in range(number_of_gardeners):
        start, end = map(int, input().split())
        beds[i] = [start, end]
    beds_sort(beds)
