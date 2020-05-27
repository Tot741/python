import random

with open('text_5.txt', 'w', ) as f_obj:
    for i in range(10):
        print(f'{random.randint(1, 100)} ', end='', file=f_obj)
sum_num = 0
with open('text_5.txt') as f_obj:
    string = f_obj.readline().split()
    for number in string:
        sum_num += int(number)
print(f'Сумма чисел в файле - {sum_num}')
