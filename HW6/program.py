# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import random

# n = int(input('Введите количество членов арифметической прогрессии:'))
# newArray = [0 for i in range(n)]
# a1 = int(input('Введите первый член арифметической прогрессии:'))
# newArray[0] = a1
# d = int(input('Введите разность арифметической прогрессии:'))
# for i in range(1, len(newArray)):
#     newArray[i] = newArray[0] + i * d # i начинается с 1, а для прогресии это второй член, +1 и -1 уничтожаются
# print(newArray)

# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

# minRange = int(input('Введите значение минимума искомого диапазона массива от 1 :'))
# maxRange = int(input('Введите значение максимума искомого диапазона массива от 1 :'))
# newArray = [i for i in range(0, maxRange * 2 + 1)]  # поскольку никак не определен порядок формирования значений,
# # принимаю, что это натуральные по порядку отсортированные
# print(newArray)
# for i in range(minRange, maxRange):
#     print(f"#", i, end=" ")

# var2
# minRange = int(input('Введите значение минимума искомого диапазона массива от 1 :'))
# maxRange = int(input('Введите значение максимума искомого диапазона массива от 1 :'))
# newArray = [random.randint(1, maxRange * 2 + 1) for i in range(0, 21)]  # рандом значений, размер ограничил 20 для визуализации
# print(newArray)
# for i in range(len(newArray)):
#     if maxRange >= newArray[i] >= minRange:
#         print(f"(#{i} : {newArray[i]}) ", end=" ")

# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 10 в 5 степени
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: Вывод:
# 300 220 284
n = int(input('Введите число к не более 1 000 000:'))
if n > 1_000_000:
    print(" число выходит за диапазон")
    exit()
tempDict = {}  # словарь для хранения числа и сум его делителей
pairDict = set()  # множество для хранения дружественных пар
for i in range(100, n):  # начинаю со 100, т.к. первое дружественое 220
    SumDiv = 0  # временная переменная для суммирования делителей
    tempValue = i
    for k in range(1, tempValue):
        if tempValue % k == 0:
            SumDiv += k
    if SumDiv != 1 and SumDiv !=0 :  # избавляемся от простых чисел, т.к у всех у них сумма делителей 1
        tempDict[tempValue] = SumDiv
for i, k in tempDict.items():
    for j, m in tempDict.items():
        if i == m and j==k and i != j:
            tempList = [i,j]
            tempList.sort()
            pairDict.add(tuple(tempList))
            tempList.clear()
print(f'Пары дружественных чисел : ', *pairDict)
