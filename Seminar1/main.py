# task 1 определить за сколько дней проедем машина без использования уиклов и if
# Distance = 12
# rangeCar = 24
# print(f"Машине нужно {(Distance + rangeCar-1)// rangeCar} дней")
# task 2 подчитать наименьшее кол-во парт, для трех классов, причем нельзя кол-во ученики в разных кабинетов
# pClass1 = int(input("Класс 1 учеников сколько: "))
# pClass2 = int(input("Класс 2 учеников сколько: "))
# pClass3 = int(input("Класс 3 учеников сколько: "))
# print(f"нужно {((pClass1+1)// 2)+((pClass2+1)// 2)+((pClass3+1)// 2)} парт")

# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# vagonEnter = int(input("в какой вагон с головы поезда по порядку сел: "))
# vagonNumber = int(input("какой номер вагона : "))
# if vagonEnter != vagonNumber :
#     print(f" в эелектричке {vagonEnter+vagonNumber-1} вагонов")
# else:
#     print("нужна доп информация")
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
year = int(input("Введите год: "))
if year % 4 > 0 or year % 100 == 0 :
    print("NO")
else:
    print("Yes")