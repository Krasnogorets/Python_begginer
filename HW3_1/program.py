# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# list_1 = [i for i in range(1, 15, 2)]
# print(list_1)
# sum1 = 0
# for i in range(1, len(list_1), 2):
#     sum1 += list_1[i]
# print(f'Сумма нечетных элементов списка: ', sum1)

# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# list_2 = [i for i in range(2, 15, 1)]
# print(list_2)
# sumPair = 0
# for i in range(len(list_2)//2) :
#     sumPair += list_2[i] + list_2[-1-i]
# print(f'Сумма пар списка: ', sumPair)

# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным з
# начением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
# list_3 = [1.1, 1.2, 3.16, 5.45, 10.01, 0.23, 9.89]
# print(list_3)
# for i in range(len(list_3)):
#     list_3[i] = list_3[i] - int(list_3[i])
# minNum = maxNum = list_3[0]
# for i in list_3:
#     if i < minNum:
#         minNum = i
#     if i > maxNum:
#         maxNum = i
# print(f'=> {round(maxNum-minNum,2)}')
# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# n = int(input('Введите размер списка: '))
# list_4 = []
# x = 0
# for i in range(0, n + 1):
#     if i == n:
#         x = int(input(f'Введите искомое X: '))
#     else:
#         list_4.append(int(input(f'Введите {i}-ое число: ')))
# count = 0
# for i in list_4:
#     if i == x:
#         count += 1
# print(f" Число {x} встречается {count} раз")

# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# n = int(input('Введите размер списка: '))
# list_4 = []
# x = 0
# for i in range(0, n + 1):
#     if i == n:
#         x = int(input(f'Введите искомое X: '))
#     else:
#         list_4.append(int(input(f'Введите {i}-ое целое число: ')))
# numCloser = list_4[0]
# for i in list_4:
#     if x > 0:
#         if numCloser - x < i - x:
#             numCloser = i
# print(numCloser)

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.Ввод:ноутбук Вывод:
# 12
# dict = {"A": "1", "E": "1", 'I': "1", 'O': "1", 'U': "1",
#         'L': "1", 'N': "1", 'S': "1", 'T': "1", 'R': "1",
#         'D': "2", 'G': "2", 'B': "3", 'C': "3", 'M': "3",
#         'P': "3", 'F': "4", 'H': "4", 'V': "4", 'W': "4",
#         'Y': "4", 'K': "5", 'J': "8", 'X': "8", 'Q': "10",
#         'Z': "10", 'А': "1", 'В': "1", 'Е': "1", 'И': "1",
#         'Н': "1", 'О': "1", 'Р': "1", 'С': "1", 'Т': "1",
#         'Д': "2", 'К': "2", 'Л': "2", 'М': "2", 'П': "2",
#         'У': "2", 'Б': "3", 'Г': "3", 'Ё': "3", 'Ь': "3",
#         'Я': "3", 'Й': "4", 'Ы': "4", 'Ж': "5", 'З': "5",
#         'Х': "5", 'Ц': "5", 'Ч': "5", 'Ш': "8", 'Э': "8",
#         'Ю': "8", 'Ф': "10", 'Щ': "10", 'Ъ': "10"}
# word = input('Введите слово на русском или английском или смешанном англо-русском алфавите:').upper()
# result = 0
# for i in range(len(word)):
#     result += int(dict[word[i]])
# print(result)
# var2
dict1 = {'1': "[A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т]",
         '2': '[D, G, Д, К, Л, М, П, У]',
         '3': '[B, C, M, P, Б, Г, Ё, Ь, Я]',
         '4': '[F, H, V, W, Y, Й, Ы]',
         '5': '[K, Ж, З, Х, Ц, Ч]',
         '8': '[J, X, Ш, Э, Ю]',
         '10': '[Q, Z, Ф, Щ, Ъ]'}
word = input('Введите слово на русском или английском или смешанном англо-русском алфавите:').upper()
result = 0
for m in range(len(word)):
    for i, j in dict1.items():
        if word[m] in j:
            result += int(i)
print(result)
