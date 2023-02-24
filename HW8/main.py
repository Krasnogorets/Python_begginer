#  Задача No49.
def input_data():
    with open("data.txt", "a") as f:
        for i in range(int(input("введите кол-во новых записей в справочник - "))):
            f.writelines(input("введите ФИО и номер телефона: ").upper())


def read_data():
    with open("data.txt", "r") as f:
        print(f.read())


def find_data(x):
    with open("data.txt", "r") as f:
        find_feature = input("введите одну из характеристик для поиска - ").upper()
        flag = False
        lines = f.readlines()
        for i in lines:
            list_feature = i.split()
            if find_feature in list_feature and x == 1:
                print(i, end="")
                flag = True
            elif find_feature in list_feature and x == 2:
                return i, lines, list_feature
            elif find_feature in list_feature and x == 3:
                return i, lines, list_feature
        if not flag:
            print("такой записи не найдено")


def replace_data():
    i, lines, list_feature = find_data(2)
    print(i, end="")
    while True:
        get_choice = (int(input(
            """\n             1 - для изменения фамилии,
             2 - для изменения имени, 
             3 - для изменения отчества,
             4 - для изменения телефона
             5 - возврат к главному меню: """)))
        match get_choice:
            case 1:
                list_feature[0] = input("введите новую фамилию: ").upper()
                write_lines(lines, list_feature, i)
                break
            case 2:
                list_feature[1] = input("введите новое имя: ").upper()
                write_lines(lines, list_feature, i)
                break
            case 3:
                list_feature[2] = input("введите новое отчество: ").upper()
                write_lines(lines, list_feature, i)
                break
            case 4:
                list_feature[3] = input("введите новый телефон: ").upper()
                write_lines(lines, list_feature, i)
                break
            case 5:
                return


def write_lines(lines, list_feature, i):
    print(*list_feature, end="")
    lines[lines.index(i)] = " ".join(list_feature) + '\n'
    with open("data.txt", "w") as f:
        f.writelines("%s" % line for line in lines)


def remove_data():
    i, lines, list_feature = find_data(3)
    m = int(input('Желаете полностью удалить эту строк? (1-да, 2-нет)'))
    if m == 1:
        lines.remove(i)
        with open("data.txt", "w") as f:
            f.writelines("%s" % line for line in lines)


while True:
    get_choice = (int(input(
        """\n введите 1 - для добавления записи,
         2 - для вывода всего справочника, 
         3 - для поиска, 
         4 - для изменения данных
         5 - для удаления данных         
         6 - для завершения работы : """)))
    match get_choice:
        case 1:
            input_data()
        case 2:
            read_data()
        case 3:
            find_data(1)
        case 4:
            replace_data()
        case 5:
            remove_data()
        case _:
            break
