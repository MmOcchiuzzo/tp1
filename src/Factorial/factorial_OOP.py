import sys

class Factorial:
    def __init__(self):
        pass

    def factorial(self, num):
        if num < 0:
            print("El factorial de un número negativo no existe")
            return None
        elif num == 0:
            return 1
        else:
            fact = 1
            while num > 1:
                fact *= num
                num -= 1
            return fact

    def run(self, min_num, max_num):
        resultados = {}
        for num in range(min_num, max_num + 1):
            resultados[num] = self.factorial(num)
        return resultados

if len(sys.argv) == 1:
    rango = input("Por favor, ingrese el rango de números (min-max): ")
else:
    rango = sys.argv[1]

min_num, max_num = map(int, rango.split("-"))

factorial_calculator = Factorial()
resultados = factorial_calculator.run(min_num, max_num)
for num, factorial in resultados.items():
    print(f"Factorial de {num} es {factorial}")