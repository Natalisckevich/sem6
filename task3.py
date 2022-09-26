# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0, 56 -> 11
# num = str(input('Введите число: '))
# sum = 0
# for i in num:
#    if i != '.' and i != ',':
#         sum += int(i)
# print(f'Сумма цифр в числе: {sum}')


# Второе решение
def sum_num(num: str) -> int:
    return sum(map(int, filter(lambda i: i.isdigit(), str(num))))


print(sum_num(6782))
print(sum_num(0.56))