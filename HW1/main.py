# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# num = int(input('Введите любое число: '))
# sum = 0
# while num > 0:  # решение через цикл и с любым числом
#     sum += num % 10
#     num //= 10
# print(f" Сумма цифр данного числа равна {sum}")
#
# num = input('Введите трехначное число: ')  # код не короче, но без цикла
# if len(num) == 3:
#     print(f" Сумма цифр данного числа равна {int(num[0])+int(num[1])+int(num[2])}")
# else:
#     print('Число не трехначное ')
# Задача 2: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10
# birds = int(input('Сколько всего журавликов сделали дети? :'))
# if birds % 6 > 0:
#     print('Такое количество журавликов нельзя разделить по условию задачи')
# else:
#     print(
#         f'Петя и Сережа сделали по  {birds // 6} журавликов, '
#         f'а Катя сделала {birds // 3 * 2} журавлика')

# Задача 3: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no
tiketsNumber = input('Введите шестизначный номер билета :')
if len(tiketsNumber) == 6:
    if int(tiketsNumber[0]) + int(tiketsNumber[1]) + int(tiketsNumber[2]) == int(tiketsNumber[3]) + int(
            tiketsNumber[4]) + int(tiketsNumber[5]):
        print('Ваш билет счастливый!')
    else:
        print('Ваш билет НЕ счастливый!')
else:
    print('Вы лузер по-любому, т.к. в вашем билете не 6 цифр!')
