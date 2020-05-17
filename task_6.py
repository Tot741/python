# создание структуры
goods = []
n = int(input('Введите какое количество позиций вы хотите ввести в структуру: '))
for i in range(n):
    tmp_dict = {}
    tmp_tuple = ()
    name = input('Введите наименование товара: ')
    tmp_dict.update({'Наименование': name})
    cost = input('Введите цену товара: ')
    tmp_dict.update({'Цена': cost})
    quantity = input('Введите количество товара: ')
    tmp_dict.update({'Количество': quantity})
    unit = input('Введите единицу измерения: ')
    tmp_dict.update({'Ед. изм.': unit})
    tmp_tuple = (i + 1, tmp_dict)
    goods.append(tmp_tuple)
print(f'Полученная структура выглядит следующим образом:\n{goods}')
# создание аналитики
tmp_analitic = {}
tmp_name = []
tmp_cost = []
tmp_quantity = []
tmp_unit = []
for i in range(len(goods)):
    tmp_analitic = goods[i][1]
    tmp_name.append(tmp_analitic.get('Наименование'))
    tmp_cost.append(tmp_analitic.get('Цена'))
    tmp_quantity.append(tmp_analitic.get('Количество'))
    tmp_unit.append(tmp_analitic.get('Ед. изм.'))
# Неочень понял из задания надо ли удалять дубли в списках аналитики, но на всякий случай
# добавил 4 строки ниже. Если не нужно, то можно их просто закомментировать
tmp_name = list(set(tmp_name))
tmp_cost = list(set(tmp_cost))
tmp_quantity = list(set(tmp_quantity))
tmp_unit = list(set(tmp_unit))
analitics = {'Наименование': tmp_name, 'Цена': tmp_cost, 'Количество': tmp_quantity, 'Ед. изм.': tmp_unit}
print(f'Аналитика выглядит следующим образом:\n{analitics}')
