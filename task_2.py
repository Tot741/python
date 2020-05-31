class Road:
    def __init__(self, length, width):
        self._lenght = length
        self._width = width

    def mass(self):
        return self._lenght * self._width * 0.025 * 5


a = Road(20, 5000)
print(a.mass())
