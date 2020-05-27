# Task 1
with open('text.txt', 'w', encoding='utf-8') as f_obj:
    string = 'text'
    while string:
        string = input('Введите сроку для записи в файл. Для прекращения ввода оставьте строку пустой инажмите Enter: ')
        f_obj.write(string + '\n') if string else string
# Task 2
count = 0
with open('text.txt', 'r') as f_obj:
    for line in f_obj:
        count += 1
        print(f'Количество слов в {count} строке - {len(line.split())}')
print(f'Количество строк в файле - {count}')
