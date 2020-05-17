string = input('Введите строку из нескольких слов, разделенных пробелами: ')
string = string.split()
for num, word in enumerate(string, 1):
    print(num, word[:10])
