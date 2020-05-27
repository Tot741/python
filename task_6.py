import re

try:
    dict_lesson = {}
    with open('text_6.txt') as file_obj:
        for line in file_obj:
            lesson = line.split()[0][:-1]
            hours = sum(map(int, re.findall(r'\d+', line)))
            dict_lesson.update({lesson: hours})
    print(dict_lesson)
except FileNotFoundError:
    print('Файл с данными не найден или имеет неправильное имя.\nИмя файла должно быть text_6.txt')
