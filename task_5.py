cash = int(input('Введите полученную выручку: '))
costs = int(input('Введите издержки фирмы: '))
profit = cash - costs
if profit >= 0:
    print(f'Ваша фирма отработала с прибылью и рентабельность составила {profit / cash * 100:.2f}%')
    workers = int(input('Введите количество сотрудников: '))
    print(f'В пересчете на одного сотрудника прибыль составит {profit / workers:.2f}')
else:
    print(f'Ваша фирма отработала с убытком')
