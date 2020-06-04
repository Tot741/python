class Matrix:
    matrix_sum = []
    matrix_line = []
    matrix_str = ''

    def __init__(self, list_of_lists=[]):
        self.list_of_lists = list_of_lists

    def __str__(self):
        for el in self.list_of_lists:
            self.matrix_str += ''.join(str(el)) + '\n'
        return self.matrix_str

    def __add__(self, other):
        try:
            for i in range(len(self.list_of_lists)):
                for j in range(len(self.list_of_lists[i])):
                    self.matrix_line.append(self.list_of_lists[i][j] + other.list_of_lists[i][j])
                self.matrix_sum.append(self.matrix_line)
                self.matrix_line = []
            self.matrix_str = ''
            for el in self.matrix_sum:
                self.matrix_str += ''.join(str(el)) + '\n'
            return self.matrix_str
        except IndexError:
            print('Для суммирования матрицы должны иметь одинаковую размерность!')


matrix_1 = Matrix([[1, 3, 5], [2, 4, 6], [6, 3, 8]])
print(matrix_1)
matrix_2 = Matrix([[6, 12, 8], [16, 7, 3], [56, 34, 2]])
print(matrix_2)
print(f'Суммарная матрица:\n{matrix_1 + matrix_2}')
