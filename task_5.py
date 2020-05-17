my_list = [7, 5, 3, 3, 2]
print(f'Текущий рейтнг - {my_list}')
while True:
    n = int(input('Введите новый элемент рейтинга (натуральное число):'))
    n_count = my_list.count(n)
    if n_count == 1:
        my_list.insert(my_list.index(n) + 1, n)
    elif n_count > 1:
        for i in range(-1, -len(my_list), -1):
            if my_list[i] == n:
                my_list.insert(i + 1, n) if (i + 1) != 0 else my_list.append(n)
                break
    else:
        for el in my_list:
            if n > el:
                my_list.insert(my_list.index(el), n)
                break
            elif my_list.index(el) == (len(my_list) - 1):
                my_list.append(n)
                break
    print(f'Новый рейтинг выглядит так - {my_list}')
    ask_cont = input('Хотите еще ввести данные для рейтнга (y/n)? ')
    if ask_cont.lower() != 'y':
        break
