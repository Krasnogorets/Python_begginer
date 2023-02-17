# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.
# transformation = lambda x: x
# values = [1, 23, 42, "asdfg"]
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print("ok")
# else:
#     print("fail")
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

#
# def find_farthest_orbit(x):
#     listsq = []
#     for i in x:
#         l, k = i
#         if l != k:
#             listsq.append((i, round(3.14 * l * k, 2)))
#     maxt, maxo = listsq[0]
#     for i in listsq:
#         l, k = i
#         if k > maxo:
#             maxo = k
#             maxt = l
#     return maxt
# print(*find_farthest_orbit(orbits))
# var from seminar shat
# def find_farthest_orbit(list_of_orbits):
#     list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
#     list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]
#     max_area_index = list_of_areas.index(max(list_of_areas))
#     return list_of_elliptical_orbits[max_area_index]
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
#
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: Вывод:
values = []


def same_by(x, val):
    for i in val:
        if x(i) != 0:
            return False
    return True


if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
