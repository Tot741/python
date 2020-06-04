class Cell:
    cell_string = ''

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        return self.quantity + other.quantity

    def __sub__(self, other):

        return self.quantity - other.quantity if (
                                                         self.quantity - other.quantity) > 0 else 'Невозможно произвести вычитание'

    def __mul__(self, other):
        return self.quantity * other.quantity

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def make_order(self, row):
        self.row = row
        for i in range(self.quantity // self.row):
            self.cell_string += (self.row * '*') + '\n'
        if self.quantity % self.row != 0:
            self.cell_string += (self.quantity % self.row) * '*'
        return self.cell_string


a = Cell(32)
b = Cell(14)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(9))
print()
print(b.make_order(5))
