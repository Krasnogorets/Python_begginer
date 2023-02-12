# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
a=int(input('Введите число a (положительное):'))
b=int(input('Введите число b (положительное):'))

def exp(a,b):
    if b == 0:
        return 1
    return a*exp(a,b-1)
print(exp(a,b))

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. использовать +1 и -1
# 2 2
# 4
#var 1
a = int(input('Введите число a (целое, можно положительное и отрицательное):'))
b = int(input('Введите число b (только положительное, <=996)):'))


def summa(a, b): # принцип уменьшения второго слагаемого на 1 и одновремено увеличение на 1 первого
    try:
        a += 1
        b -= 1
        if b > 0:
            return summa(a, b)
        else:
            return a
    except RecursionError:
        print("Такие числа нет возможности складывать рекурсией")

print(f"{a} + {b} = {summa(a, b)}")