
# Задача 1: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# мое понимание, что количество монет гербом или решкой неизвестно, т.е не задаются никак
# minCoin=1
# maxCoin=100
# flag = True
# while flag:
#     N = int(input(f'Введите количество монет от {minCoin} до {maxCoin}: '))
#     if N < minCoin or N > maxCoin:
#         flag = True
#         print('Количество монет не в диапазоне ввода')
#     else:
#         flag = False
# if N == 1:
#     print('Такое количество монет невозможно по условию задачи, т.к. должны быть монеты и с гербом и с решкой')
# else:
#     print(f'Минимальное количество монет, которое нужно перевернуть = {minCoin}, '
#               f'максимальное количество монет, которое нужно перевернуть = {N // 2}')

# Задача 1 вариант 2. когда задается последовательности орлов и решек

# N = input('Введите монеты на столе, путем введения 0 или 1, без пробела ( 0-орел, 1 -решка)')
# print(f'Вы ввели {len(N)} монет')
# flag = True
# if len(N) > 1:
#     countHeads = 0
#     countTails = 0
#     for i in range(len(N)):
#         temp = int(N[i])
#         if temp > 1 or temp < 0:
#             print('числа не в указанном диапазоне, только 0 или 1')
#             flag = False
#             break
#         if temp == 0:
#             countHeads += 1
#         else:
#             countTails += 1
#     if flag and countHeads > countTails:
#         print(f'Минимальное количество монет, которое нужно перевернуть = {countTails}')
#     elif flag and countTails == countHeads:
#         print(f'Минимальное количество монет, которое нужно перевернуть = {countTails}')
#     elif flag:
#         print(f'Минимальное количество монет, которое нужно перевернуть = {countHeads}')
# else:
#     print('Такое количество монет невозможно по условию задачи, т.к. должны быть монеты и с гербом и с решкой')

# Задача 2: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

print('Загадайте два натуральных числа Х и Y в диапазоне от от 1 до 1000')
s = int(input(f'введите сумму Х и Y: '))
p = int(input(f'введите сумму Х и Y: '))
flag = False
for i in range(1, 1001):
    for k in range(1, 1001):
        if p == i * k  and s == i + k:
            x = i
            y = k
            flag = True
if flag:
    print(f'Загаданные числа {x} и {y}')
else:
    print(f'Загаданные числа  не соответсвуют условию суммы {s} и произведению {p}')


# Задача 3: Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8
flag = True
minNum = 1
maxNum = 1500
while flag:
    N = int(input(f'введите натурально число N от 1 до 1500: '))
    if N < minNum or N > maxNum:
        flag = True
        print('число не в диапазоне ввода')
    else:
        flag = False
i = 0
while 2 ** i <= N:
    print(f' {2 ** i},', end=' ')
    i += 1
    if 2 ** i > N:
        break
