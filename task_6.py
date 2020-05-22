def fact(n):
    fact = 1
    for el in range(1, n + 1):
        fact *= el
        yield fact


i = 1
n = int(input('Введите до какого числа вы хотите получить факториалы: '))
for el in fact(n):
    print(f'{i}! = {el}')
    i += 1
