try:
    def my_div(num_1, num_2):
        ''' Function for dividing two numbers '''
        return num_1 / num_2


    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    print(f'Результат деления {num_1} на {num_2} будет {my_div(num_1, num_2)}')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
except ValueError:
    print('Вы ввели не число, деление невозможно')
