"""
У Кости есть бумажка, на которой написано n чисел. Также у него есть возможность
не больше, чем k раз, взять любое число с бумажки, после чего закрасить одну из
старых цифр, а на ее месте написать новую произвольную цифру.

На какое максимальное значение Костя сможет увеличить сумму всех чисел на листочке?

Формат входных данных:
В первой строке входного файла даны два целых числа n, k — количество чисел
на бумажке и ограничение на число операций.
(1 ≤ n ≤ 1000, 1 ≤ k ≤ 10^4).
Во второй строке записано n чисел a_i — числа на бумажке (1 ≤ a_i ≤ 10^9).

Формат выходных данных:
В выходной файл выведите одно число — максимальную разность между конечной и начальной суммой.

Замечание:
В первом примере Костя может изменить две единицы на две девятки, в результате
чего сумма чисел увеличится на 16.
Во втором примере Костя меняет число 85 на 95.
В третьем примере можно ничего не менять.

Обратите внимание, что ответ может превышать вместимость 32-битного типа данных.

Примеры данных:

Пример 1:
Ввод:
5 2
1 2 1 3 5
Вывод:
16

Пример 2:
Ввод:
3 1
99 5 85
Вывод:
10

Пример 3:
Ввод:
1 10
9999
Вывод:
0
"""

n, k = map(int, input().split())
in_str = input().split()
digits = list(map(int, in_str))
start_sum = sum(digits)

lengths = set(len(w) for w in in_str)

lengths = sorted(lengths, reverse=True)
in_str.sort(reverse=True)

new_str = []

for l in range(lengths[0], 0, -1):
    block = [word for word in in_str if len(word) == l]
    block.sort()
    new_str += block
for l in range(lengths[0], 0, -1):
    for i, w in enumerate(new_str):
        c = len(w) - l
        if k > 0 and c >= 0 and int(w[c]) < 9:
            new_str[i] = w[:c]+'9'+w[c+1:]
            k -= 1
            if (k <= 0):
                break
    if k <= 0:
        break

print(sum(int(i) for i in new_str)-start_sum)
