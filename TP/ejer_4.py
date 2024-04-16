class Number:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class NumberDecorator:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return str(self.number)

class AddTwoDecorator(NumberDecorator):
    def __init__(self, number):
        super().__init__(number)
        self.number.value += 2

class MultiplyByTwoDecorator(NumberDecorator):
    def __init__(self, number):
        super().__init__(number)
        self.number.value *= 2

class DivideByThreeDecorator(NumberDecorator):
    def __init__(self, number):
        super().__init__(number)
        self.number.value /= 3

# Número original
original_number = Number(10)
print("Número original:", original_number)

# Número con suma de 2
number_with_addition = AddTwoDecorator(Number(10))
print("Número con suma de 2:", number_with_addition)

# Número con multiplicación por 2
number_with_multiplication = MultiplyByTwoDecorator(Number(10))
print("Número con multiplicación por 2:", number_with_multiplication)

# Número con división por 3
number_with_division = DivideByThreeDecorator(Number(10))
print("Número con división por 3:", number_with_division)
