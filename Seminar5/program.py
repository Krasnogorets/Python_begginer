# Последовательностью Фибоначчи называется
# последовательность чисел a0
# , a1
# , ..., an
# , ..., где
# a0
#  = 0, a1
#  = 1, ak
#  = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию
# def fib(n, x, list1):
#     if len(list1) == n + 1:
#         return n, x, list1
#     else:
#         x += 1
#         list1.append(list1[x - 1] + list1[x - 2])
#         return fib(n, x, list1)
#
#
# x = 1
# list1 = [0,1]
# n = int(input('введите n:'))
# fib(n, x, list1)
# print(list1[n])
# var2
# def fib(n):
#     if n in (0,1):
#         return 1
#     return fib(n-1) + fib(n-2)
# n = int(input('введите n:'))
# print(fib(n-2))

# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4  16-> 1 2 3 3 5 5 4 4 3 3 5 5 1 1 2 2
# Output: 1 3 3 3 1           1 2 3 3 1 1 4 4 3 3 1 1 1 1 2 2
# def mark_change(i, min, max, list3):
#     if i == len(list3) - 1:
#         return list3
#     if list3[i] == max:
#         list3[i] = min
#     i += 1
#     return mark_change(i, min, max, list3)
#
#
# list1 = input('Введите оценки Василия:').split()
# min1 = max1 = 0
# list2 = list.copy(list1)
# list2.sort()
# min1 = list2[0]
# max1 = list2[-1]
# i = 0
# mark_change(i, min1, max1, list1)
# print(list1)
# var2
# list1 = input('Введите оценки Василия:').split()
# list1 = [int(x) for x in list1]
# min1 = min(list1)
# max1 = max(list1)
# for i in range(len(list1)):
#     if list1[i] == max1:
#         list1[i] = min1
# print(*list1)

# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes
# n = int(input('Введите число n:'))
# def simple(i, n):
#     if i == n:
#         return i
#     if n / i == n // i:
#         return False
#     i += 1
#     return simple(i, n)
#
# i = 2
# if simple(i, n):
#     print(f"число {n} простое")
# elif i:
#     print(f"число {n} НЕ простое")
# var2
# def simple(n):
#     flag = True
#     for i in range(2, n):
#         if n % i != 0:
#             continue
#         else:
#             flag = False
#     return flag
#
#
# print(simple(int(input('Введите число n:'))))
#
# Дано натуральное число N и
# последовательность из N элементов.
# Требуется вывести эту последовательность в
# обратном порядке.
# Примечание. В программе запрещается
# объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3
# n = int(input('Введите число n:'))
# list1 = []
# i = 0
#
#
# def input1(i, n, list1):
#     if i == n:
#         return list1
#     list1.append(int(input(f'Введите элемент {i}:')))
#     i += 1
#     return input1(i, n, list1)
# input1(i,n,list1)
# list1.sort()
# print(list1)
# var2
n = int(input('Введите число n:'))
list1 = []


def input1(i, n, list1):
    if i == n:
        return list1
    list1.append(int(input(f'Введите элемент {i}:')))
    i += 1
    return input1(i, n, list1)


i = 0
input1(i, n, list1)


def sortN(i,n,min3,list1):
    if i == n:
        return list1
    temp=0
    list1[i+1]<list2[i]:

def min1(i, n, min3, list1):
    if i == n:
        return min3,i
    min3 = list1[i]
    if list1[i] < min3:
        min3 = list1[i]
    i += 1
    return min1(i, n, min3, list1)


min3 = list1[0]
print(min1(i, n, min3 ,list1))

