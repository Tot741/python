def sum_string(list_num):
    for el in list_num:
        if el != 'q':
            global sum, key
            sum = sum + int(el)
        else:
            key = el
            break
    return sum, key


sum = 0
key = None
try:
    while key != 'q':
        string = input(
            'Введите строку чисел разделенных пробелами и нажмите Enter. Для прекращения суммирования введите q: ').split()
        sum, key = sum_string(string)
        print(f'Сумма введеных чисел равна {sum}')
except ValueError:
    print('Нужно ввести числа разделенные пробелами или стоп-символ q')
