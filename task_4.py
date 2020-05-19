def my_func(x, y):
    # Первый способ
    #return x ** y
    # Второй способ
    for i in range(abs(y) - 1):
        x += x
    return 1 / x


x = -1
y = 1
while x <= 0:
    x = float(input('Введите действительное положительное число: '))
    print('Вы ввели неположительное число! Повторите ввод') if x <= 0 else x
while y >= 0:
    y = int(input('Введите целое отрицательное число: '))
    print('Вы ввели неотицательное число! Повторите ввод!') if y >= 0 else y
print(f'Число {x} в степени {y} будет равно {my_func(x, y)}')
