# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
#
# 6 12
# n = int(input('Введите кол-во элементов множества 1:'))# по условию ввод элементов в строчку,
# # поэтому задавать количества элементов достаточно бессмысленно, т.к. проверку длины строки input можно только после ввода
# m = int(input('Введите кол-во элементов множества 2:'))
# s = set(input('Введите через пробел элементы множества 1:').split())
# s1 = set(input('Введите через пробел элементы множества 2:').split())
# result = set(s.intersection(s1))
# list1= []
# for i in result:
#     list1.append(i)
# list1.sort()
# print(*list1)
# var 2
# n = int(input('Введите кол-во элементов множества 1:'))
# m = int(input('Введите кол-во элементов множества 2:'))
# list2 = set()
# list3 = set()
# for i in range(n):
#     s = int(input(f"Введите элемент №{i+1} множества 1: "))
#     list2.add(s)
# for i in range(m):
#     s = int(input(f"Введите элемент №{i+1} множества 2: "))
#     list3.add(s)
# result = set(list2.intersection(list3))
# list4 = []
# for i in result:
#     list4.append(i)
# list4.sort()
# print(*list4)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
#
# 4 -> 1 2 3 4
# 9
import random
n = int(input('Введите кол-во кустов:'))
list5 = []
minBerries = 5  # мин кол-во ягод на одном кусте
maxBerries = 15  # макс кол-во ягод на одном кусте
for i in range(n):
    list5.append(random.randint(minBerries, maxBerries + 1))
print('Ваша грядка вот такой урожай:', *list5)
list5.append(list5[0])  # грядка круглая, поэтому для последнего куста соседний - первый и наоборот,
list5.insert(0, list5[-2])  # добавим первый и последний рядом
dict1 = {}
max1 = 0
maxkey=0
temp1 = 0
for i in range(1, n + 1):
    temp1 = int(list5[i - 1]) + int(list5[i]) + int(list5[i + 1])
    dict1.update({int(i): temp1})
    if max1 < temp1:
        max1 = temp1
        maxkey = i
print(f'Максимальное число ягод ({max1}) за один подход вы получите, подойдя к кусту {maxkey}')
