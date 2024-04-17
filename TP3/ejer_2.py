# 2) Elabore una clase para el cálculo del valor de impuestos a ser utilizado por 
# todas las clases que necesiten realizarlo. El cálculo de impuestos simplificado 
# deberá recibir un valor de importe base imponible y deberá retornar la suma 
# del cálculo de IVA (21%), IIBB (5%) y Contribuciones municipales (1,2%) sobre 
# esa base imponible.

#Singleton

class ImpuestosCalculator:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def calcular_impuestos(self, base_imponible):
        iva = base_imponible * 0.21
        iibb = base_imponible * 0.05
        contribuciones_municipales = base_imponible * 0.012

        total_impuestos = iva + iibb + contribuciones_municipales
        return total_impuestos

# Uso
impuestos_calculator = ImpuestosCalculator()
base_imponible = 1000 
total_impuestos = impuestos_calculator.calcular_impuestos(base_imponible)
print("Total de impuestos a pagar:", total_impuestos)
