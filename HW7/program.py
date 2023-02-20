# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает,
# Вам стоит написать программу. Винни-Пух считает, что ритм есть,
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке |
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-да
# ,"е","и","о","у","э","ю","я"
# Вывод:
# Парам пам-пам
# var1
# list1 = input('Веедите стих: ').split(' ')
#
#
# def f(list):
#     list3 = []
#     for i in list:
#         count = 0
#         for l in range(len(i)):
#             if i[l] == 'а':
#                 count += 1
#         list3.append(count)
#     return list3
#
#
# def check(list):
#     if list.count(list[0]) == len(list):
#         return True
#     return False
#
#
# if check(f(list1)):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')
# var 2
stroka1 = 'пара-ра-рам рам-пaм-папам па-ра-па-дам'
vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
phrases = stroka1.split()
if len(phrases) < 2:
    print('Количество фраз должно быть больше одной!')
else:
    countVowels = []

    for i in phrases:
        countVowels.append(len([x for x in i if x.lower() in vowels]))

    if countVowels.count(countVowels[0]) == len(countVowels):
        print('Парам пам-пам')
    else:
        print('Пам парам')


# Задача 36:
# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Ввод:
#
# print_operation_table(lambda x, y: x * y)
#
# Вывод:
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 |
# var1
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):
#         for k in range(1, num_columns+1):
#             print(operation(k, i), end=' ')
#         print( end='\n')
#
#
#
# print_operation_table(lambda x, y: x * y)


# var 3

def print_operation_table(operation, num_rows=4, num_columns=4):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        print('	'.join([str(i) for i in range(1, num_columns + 1)]))
        for i in range(2, num_rows + 1):
            print(i, end='	')
            for j in range(2, num_columns + 1):
                print(operation(i, j), end='	')
            print()


print_operation_table(lambda x, y: x * y)
