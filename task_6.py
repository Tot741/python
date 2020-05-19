def int_func(word):
    words_list = list(set(word))
    for el in words_list:
        if 97 <= ord(el) <= 122 or ord(el) == 32:
            continue
        else:
            return 'Строка содержит не только маленькие латинские буквы'
    return word.title()


string = input('Введите строку слов из латинских букв разделенных пробелами: ')
print(int_func(string))
