from itertools import count, cycle, takewhile

new_list = []
c = 0
n = int(input('Введите число: '))
for el in count(n):
    if el > n + 10:
        break
    else:
        new_list.append(el)
print(f'Последовательность чисел от {n} до {n + 10} выглядит следующим образом:\n{new_list}')
print(f'В последвательность входят следующие числа:')
for symbol in cycle(new_list):
    if c > len(new_list) - 1:
        break
    print(symbol)
    c += 1
