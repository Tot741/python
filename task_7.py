class Complex_number():
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def __str__(self):
        return f'{self.real_part}+{self.imaginary_part}i' if self.imaginary_part > 0 else f'{self.real_part}-{self.imaginary_part}i'

    def __add__(self, other):
        sum_real = self.real_part + other.real_part
        sum_imaginary = self.imaginary_part + other.imaginary_part
        return Complex_number(sum_real, sum_imaginary)

    def __mul__(self, other):
        mul_real = self.real_part * other.real_part + self.imaginary_part * other.imaginary_part * -1
        mul_imaginary = self.imaginary_part * other.real_part + self.real_part * other.imaginary_part
        return Complex_number(mul_real, mul_imaginary)


number_1 = Complex_number(2, 3)
number_2 = Complex_number(3, -2)
print(number_1 + number_2)
print(number_1 * number_2)
print('Проверка:')
print(complex(2, 3) + complex(3, -2))
print(complex(2, 3) * complex(3, -2))



