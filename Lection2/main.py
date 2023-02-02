# создание списков
# list_1 = []  # создание пустого списка
# list_1 = list()  # создание пустого списка
# list_1 = [1, 2, 3, 8]
# # print(*list_1)
# # for i in list_1:
# #     print(i)
# print(list_1)
# list_1.append(0)
# print(list_1)

# list_1 = [1,2,3,4]
# print(list_1)
# # for i in range(5):
# #     list_1.append(i)
# #     print(list_1)
# list_1.pop(1)
# print(list_1)
#
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# list_1.insert(2, 11)
# print(list_1)
# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])  # 1
# print(list_1[1])  # 2
# print(list_1[len(list_1) - 1])  # 10
# print(list_1[-5])  # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])  # [1, 2]
# print(list_1[len(list_1) - 2:])  # [9, 10]
# print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])  # []
# print(list_1[0:len(list_1):6])  # [1, 7] - идем с начала до конца с шагом 6
# print(list_1[::6])  # [1, 7]  идем с начала до конца с шагом 6
#
# a = 1
# b = 2
# a, b = 1, 2
# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1) # создается не кортеж, а целочисленная переменная
# print(type(t))
# b = (28, 7)
# print(b, type(b))
# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t # распаковка кортежа на переменные
# print('r:{} g:{} b:{}'.format(red, green, blue))# r:red g:green b:blue

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ← типы ключей могут отличаться
# print(dictionary['up']) # ↑ типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
#
# del dictionary['left'] # удаление элемента
# colors = {'red', 'green', 'blue'} # задаются такими же скобками как и словари, но ключ не нужен,
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red') #также только уникальные задаются, при попытке добавить ничего не поизойдет
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red') # удаление элемента
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red' повторно уже не удалить
# colors.discard('red') # удаление элемента, с предварительной проверкой его наличия, т.е. если нет то ошибки не будет

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8} копирование
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,21) объединение множеств
# i = a.intersection(b) # i = {8, 2, 5} пересечение множест
# dl = a.difference(b) # dl = {1, 3} разница множеств, т.е как а отличается от b
# dr = b.difference(a) # dr = {13, 21} разница множеств, т.е как b отличается от a
# q = a.union(b).difference(a.intersection(b))# {1, 21, 3, 13} сначала действия в скобках a.intersection(b),
# # далее разница между объединениеем а и б т полученным пересечением а и б

# list_1 = [(i, i*i) for i in range(1, 101) if i % 2 == 0]# [(2, 2), (4, 4),..., (100, 100)]
# print(list_1)
# colors = ['red','green', 'blue']
# data  = open('file.txt', 'a')
# data.writelines(colors)
# data.write('line3\n')
# data.write('line4\n')
# data.close()
with open('file.txt','w') as data:
    data.write('line3\n')
    data.write('line4\n')
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()