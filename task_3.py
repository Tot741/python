count = 0
sum_salary = 0
try:
    with open('text_3.txt', 'r') as f_obj:
        for line in f_obj:
            content = line.split()
            if float(content[1]) < 20000:
                print(f'Сотрудник {content[0]} имеет зарплату меньше 20000')
            count += 1
            sum_salary = sum_salary + float(content[1])
    print(f'Средняя зарплата сотрудников - {round((sum_salary / count), 2)}')
except FileNotFoundError:
    print('Файл с данными сотрудников не найден или имеет неправильное имя.\nИмя файла должно быть text_3.txt')