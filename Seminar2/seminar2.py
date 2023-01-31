# найти факториал числа n
# n = 5
# i = 1
# factorial=1
# while i <= n:
#     factorial = factorial * i
#     i += 1
# print(factorial)
# factorial=1
# for j in range(1, n+1):
#     factorial *= j
# print(factorial)
# получить на вход число >1, каким по порядку числом фибоначи оно является, если не является, то вывести -1
# a = int(input('Введите число А:'))
# if a > 1:
#     n = 0
#     n1 = 1
#     count = 0
#     for i in range(3, a+3):
#         fibonachi = n + n1
#         n = n1
#         n1 = fibonachi
#         if a == fibonachi:
#             count = i
#     if count != 0:
#         print(count)
#     else:
#         print('-1')
# else:
#     print("число не соответсвует условиям")
# ввести дни и температуру каждого дня, подсчитать сколько дней подряд было больше нуля
N = int(input('Введите число N:'))
Max = 0
count = 0
for i in range(1, N + 1):
    Temp = int(input(f'Введите температуру дня {i}:'))
    if Temp > 0:
        count += 1
        if count > Max:
            Max = count
    else:
        count = 0
print(Max)
# print ("fjfjjf", and = ' ') - будет выводить через пробел, по умолчанию and = переносу