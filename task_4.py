number = int(input('Введите целое положительное число: '))
max_number = number % 10
while True:
    if max_number < number % 10:
        max_number = number % 10
    number = number // 10
    if number == 0:
        break
print(f'Самая большая цифра в введенном числе - {max_number}')
