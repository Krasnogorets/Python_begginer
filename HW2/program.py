# Задача 1. Иван Васильевич пришел на рынок и решил купить два арбуза:
# один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
# N = int(input('Введите общее количество арбузов: '))
# if N > 2:
#     i = 1
#     maxWeight = const = 0.1
#     minWeight = const1 = 30
#     while i <= N:
#         flag = True
#         while flag:
#             weight = float(input(f'Введите вес (от 0.1 до 30) {i}-го арбуза в кг  '))
#             if weight < const or weight > const1:
#                 flag = True
#             else:
#                 flag = False
#         if weight > maxWeight:
#             maxWeight = weight
#         if weight < minWeight:
#             minWeight = weight
#         i += 1
#     print(f'Самый легкий арбуз: {minWeight}кг, самый тяжелый : {maxWeight}кг')
# elif N >= 0:
#     print(f"Среди {N} арбузов не определить самый легкий и самый тяжелый")
# elif N < 0:
#     print(f"Отрицательное количество арбузов не в этой вселенной")

# Задача 2: На столе лежат n монеток. Некоторые из них лежат вверх решкой,
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

# вариант 2. когда задается последовательности орлов и решек

N = input('Введите монеты на столе, путем введения 0 или 1, без пробела ( 0-орел, 1 -решка)')
print(f'Вы ввели {len(N)} монет')
flag = True
if len(N) > 1:
    countHeads = 0
    countTails = 0
    for i in range(len(N)):
        temp = int(N[i])
        if temp > 1 or temp < 0:
            print('числа не в указанном диапазоне, только 0 или 1')
            flag = False
            break
        if temp == 0:
            countHeads += 1
        else:
            countTails += 1
    if flag and countHeads > countTails:
        print(f'Минимальное количество монет, которое нужно перевернуть = {countTails}')
    elif flag and countTails == countHeads:
        print(f'Минимальное количество монет, которое нужно перевернуть = {countTails}')
    elif flag:
        print(f'Минимальное количество монет, которое нужно перевернуть = {countHeads}')
else:
    print('Такое количество монет невозможно по условию задачи, т.к. должны быть монеты и с гербом и с решкой')
