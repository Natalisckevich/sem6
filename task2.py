# Найти расстояние между двумя точками пространства(числа вводятся через пробел)"""

# import math
# def calculate_distance(a, b):
#    return math.sqrt(sum((a - b) ** 2.0 for a, b in zip(a, b)))
# first_point = [float(input("Введите координату x первой точки")), float(input("Введите координату y первой точки"))]
# second_point = [float(input("Введите координату x второй точки")), float(input("Введите координату y второй точки"))]
# print(f'A {first_point}, B {second_point} -> {calculate_distance(first_point, second_point)}')

# Второе решение
# Импорт модуля math чтобы воспользоватся функцией sqrt
import math

pt1 = list(map(int, input('Координата точки 1: ').split()))
pt2 = list(map(int, input('Координата точки 2: ').split()))

# Лямбда функция которая расчитывает расстояние межде 2-мя точками в пространстве
dist = lambda p1, p2: math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

print(f'Расстояние между 2-мя точками с координатами {pt1} и {pt2} в простанстве равно: {dist(pt1, pt2):.2f}')