result_list = [2, 2.05, "Yes", True, (2, 3), [4, 5], {"key1": 12, "key2": 15}, None]
print(f'Имеется следующий список:\n{result_list}\nПроверим типы данных его элементов:')
for el in result_list:
    print(f'{el} - {result_list.index(el)} элемент списка, его тип - {type(el)}')
