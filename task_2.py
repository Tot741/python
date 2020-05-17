n = int(input('Введите количество элементов в списке?: '))
start_list = []
for i in range(n):
    el = input(f'Введите {i} элемент: ')
    start_list.append(el)
print(f'Закончили ввод элементов. В итоге мы имеем следующий список:\n{start_list}')
result_list = start_list.copy()
for i in range(0, len(result_list), 2):
    if i == len(result_list) - 1:
        break
    else:
        result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
print(f'Результат перестановки элементов списка:\n{result_list}')
