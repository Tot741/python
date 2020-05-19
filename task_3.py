def my_func(n1, n2, n3):
    ''' Return sum of two max number'''
    arg_list = [n1, n2, n3]
    arg_list.remove(min(arg_list))
    return sum(arg_list)


try:
    n1 = int(input('Введите первое число: '))
    n2 = int(input('Введите второе число: '))
    n3 = int(input('Введите третье число: '))
    print(f'Сумма двух максимальных из введенных чисел будет равна {my_func(n1, n2, n3)}')
except ValueError:
    print('Вы ввели не число!')
