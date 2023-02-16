# def srtX(x):
#     return x*x
#
# print(srtX(6))
# print(type(srtX))
#
# a = srtX
# print(a(7))
# print(type(a))
#
# def calc1(a,b):
#     return a+b
# def calc2(a,b):
#     return a*b
#
# def math1(func, x,y):
#     return print(func(x,y))
#
# math1(calc1,4,6)
# math1(calc2,4,6)
# math1(lambda a,b : a+b, 34,67)
#
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)
# list1 = [1,2,3,5,8,15,23,38]
# list2 = []
# def func2(list,list4,x):
#     k=list[x]
#     if k%2 ==0:
#         return list4.append((k,k*k))
# for i in  range(len(list1)):
#     func2(list1,list2,i)
# print(list2)
#
# for i in list1:
#     if i % 2 == 0:
#         list2.append((i,i*i))
# print(list2)
#
# def select(f,col):
#     return [f(x) for x in col]
# def where (f,col):
#     return [x for x in col if f(x)]
#
# list1 = [1,2,3,5,8,15,23,38]
# res = select(int,list1)
# res = where(lambda x: x%2 == 0,res)
# res = select(lambda x: (x, x**2), res)
# print(res)

# list1= [i for i in range (1,20)]
# print(list1)
# list1= list(map(lambda x: x+10,list1))
# print(list1)
#
# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# data = '1 2 3 5 8 15 23 38'
# print(data)
# data = list(map(int, data.split()))
# print(data)

data = [1, 2, 3, 5, 8, 15, 25, 38]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
