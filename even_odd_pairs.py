'''
На физкультуре происходит разбиение по двум командам. Ребята выстроены в шеренгу, 
у каждого из них есть свой рост. 
Разбиение по командам произойдет по принципу «четный-нечетный» — 
все школьники с четным ростом отправляются в одну команду,
 а нечетные — в другую.

В отличие от привычного урока, ребята не выстроились по росту. 
Вместо привычного порядка они встали случайно. Теперь физрук Яша смотрит на шеренгу и думает — 
может ли ровно одна пара учеников поменяться местами так, чтобы команды оказались такими же, 
как и по принципу «первый-второй».
Иначе говоря, он хочет получить такой порядок, при котором все ученики 
с четным ростом стоят на четных позициях,
 а с нечетным — на нечетных.

Помогите Яше найти нужную замену.

Формат входных данных

В первой строке находится число n (2 <= n <= 1000) — количество учеников в шеренге.

В следующей строке находится n натуральных чисел ai (1 <= ai <= 10^9) — рост учеников.

Формат выходных данных

В единственной строке выведите i и j — номера элементов, которые нужно поменять местами,
 чтобы добиться заданного условия (1 <= i, j <= n, i ≠ j). 
 Если ответов несколько — разрешается вывести любой.

Если не существует способа поменять два элемента местами — выведите -1 -1.

Замечания

В первом примере хотя бы один ученик с четным ростом будет стоять на нечетной позиции. 
Во втором тесте замена приведет к неправильному состоянию.

В третьем тесте из условия замена приведет шеренгу к валидному состоянию [1, 2].
Пример 1
4
2  1  4  6
-1  -1
Пример 2
2
1  2
-1  -1
Пример 3
2
2  1
1  2

'''
n = int(input())
pairs = list(map(int, input().split()))
error = 0
# err_list = []
even = 0
odd = 0
even_index = 0
odd_index = 0
for i, d in enumerate(pairs):
    if (i+1) % 2 != d % 2:
        if (i+1) % 2 == 0:
            even += 1
            even_index = i
        else:
            odd += 1
            odd_index = i
        error += 1

if error == 2 and odd == even:
    print(even_index+1, odd_index+1)
elif error == 0:
    print("-1 -1" if n < 3 else "1 3")
else:
    print("-1 -1")
