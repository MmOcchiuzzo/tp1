# 1) Provea una clase que dado un número entero cualquiera retorne el factorial del 
# mismo, debe asegurarse que todas las clases que lo invoquen utilicen la misma 
# instancia de clase.

#Singleton

class FactorialCalculator:
    _instance = None
    _factorials = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def factorial(self, n):
        if n in self._factorials:
            return self._factorials[n]
        elif n == 0:
            return 1
        else:
            result = n * self.factorial(n - 1)
            self._factorials[n] = result
            return result

factorial_calculator1 = FactorialCalculator()
factorial_calculator2 = FactorialCalculator()

print(factorial_calculator1) 
print(factorial_calculator2)  
print(factorial_calculator1 is factorial_calculator2)
