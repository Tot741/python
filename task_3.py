original_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [original_list[i] for i in range(len(original_list)) if original_list.count(original_list[i]) == 1]
print(f'Исходный список:\n{original_list}')
print(f'Список и неповторяющихся значений:\n{new_list}')
