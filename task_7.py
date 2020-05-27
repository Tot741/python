import re, json

try:
    average_profit = 0
    dict_firm = {}
    with open('text_7.txt') as file_obj:
        for line in file_obj:
            profit = int(re.findall(r'\d+', line)[0]) - int(re.findall(r'\d+', line)[1])
            name = line.split()[0]
            average_profit += profit if profit > 0 else profit
            dict_firm.update({name: profit})
    dict_average_profit = {'average_profit': average_profit}
    finish_list = [dict_firm, dict_average_profit]
    with open('text_7.json', 'w', encoding='utf-8') as file_obj:
        json.dump(finish_list, file_obj)
except FileNotFoundError:
    print('Файл с данными не найден или имеет неправильное имя.\nИмя файла должно быть text_7.txt')