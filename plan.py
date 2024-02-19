"""
Формат входных данных:

Переговорка и ее план имеют форму прямоугольника. Первая строка входного файла
содержит два вещественных числа: координаты X и Y переговорки (1 ≤ X ≤ 1000, 1 ≤ Y ≤ 1000).
Координаты углов переговорки равны (0,0), (X,0), (X,Y), (0,Y).

Во второй строке файла даются восемь вещественных чисел, описывающих положение
углов плана переговорки. Сначала вводятся координаты того угла плана, который
соответствует углу переговорки с координатами (0,0), затем — (X,0), (X,Y),
наконец, (0,Y). Гарантируется, что входные данные корректны, то есть план
является прямоугольником, линейные размеры которого соответствуют размерам
переговорки, а также он не выходит за границы переговорки.

Все числа во входном файле вещественные, заданы с точностью 5 знаков после
десятичной точки. План выполнен в масштабе не менее 0.0001 и строго менее 1.

Формат выходных данных:

Выведите два вещественных числа — координаты неподвижной точки в координатах
переговорки. Выводить число нужно с точностью не менее четырех знаков после запятой.

Замечание:

Заметьте, что для читаемости условий входные данные в примере даются с меньшим
количеством десятичных знаков. В реальных тестовых данных в координатах будут
дополнительные нули на конце.
"""

import math


def find_map(coodr, x, y):
    # dx = coodr[2] - coodr[0]
    # dy = coodr[7] - coodr[1]
    dx = math.sqrt((coodr[2] - coodr[0])**2 + (coodr[3] - coodr[1])**2)*- \
        1 if coodr[0] > coodr[2] else math.sqrt(
            (coodr[2] - coodr[0])**2 + (coodr[3] - coodr[1])**2)
    dy = math.sqrt((coodr[2] - coodr[4])**2 + (coodr[5] - coodr[3])**2)*- \
        1 if coodr[3] > coodr[5] else math.sqrt(
            (coodr[2] - coodr[4])**2 + (coodr[5] - coodr[3])**2)
    scalex = dx/x
    scaley = dy/y*-1
    new_coord = [coodr[0]+coodr[0]*scalex, coodr[1]-coodr[1]*scaley, coodr[0]+coodr[2]*scalex, coodr[1]-coodr[3]*scaley,
                 coodr[0]+coodr[4]*scalex, coodr[1]-coodr[5]*scaley, coodr[0]+coodr[6]*scalex, coodr[1]-coodr[7]*scaley]

    return new_coord


def task8(x, y, corners):
    xx, yy = 0, 0

    for _ in range(100):
        alpha = xx / x
        beta = yy / y

        xx = (1 - alpha) * ((1 - beta) * corners[0] + beta * corners[6]) + alpha * (
            (1 - beta) * corners[2] + beta * corners[4])
        yy = (1 - alpha) * ((1 - beta) * corners[1] + beta * corners[7]) + alpha * (
            (1 - beta) * corners[3] + beta * corners[5])

    return xx, yy


x, y = map(float, input().split())
coodr = list(map(float, input().split()))

while True:
    new_coodr = find_map(coodr, x, y)
    if (math.fabs(new_coodr[0] - new_coodr[4]) <= 0.00001 and math.fabs(new_coodr[1] - new_coodr[5]) <= 0.00001):
        result = (new_coodr[0], new_coodr[1])
        break
    else:
        coodr = new_coodr

# result = task8(x, y, coodr)
print("{:.4f} {:.4f}".format(round(result[0], 4), round(result[1], 4)))
