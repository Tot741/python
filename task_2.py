original_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [original_list[i+1] for i in range(len(original_list)-1) if original_list[i+1] > original_list[i]]
print(f'Исходный список - {original_list}')
print(f'Полученный список - {new_list}')
generate_list = [el for el in range(20, 241) if el % 20 == 0 or el % 21 ==0]
print(f'Список чисел в диапазоне от 20 до 240, кратных 20 и 21:\n{generate_list}')
