# 4) Implemente una clase “factura” que tenga un importe correspondiente al total 
# de la factura pero de acuerdo a la condición impositiva del cliente (IVA 
# Responsable, IVA No Inscripto, IVA Exento) genere facturas que indiquen tal 
# condición. 

#Prototype

import copy

class Factura:
    def __init__(self, importe, condicion_impositiva):
        self.importe = importe
        self.condicion_impositiva = condicion_impositiva

    def generar_factura(self):
        impuesto, total = self.calcular_impuesto()

        print(f"Factura para cliente {self.condicion_impositiva}:")
        print(f"Importe: ${self.importe}")
        if impuesto > 0:
            print(f"IVA (21%): ${impuesto}")
        print(f"Total: ${total}")

    def calcular_impuesto(self):
        if self.condicion_impositiva == "IVA Responsable":
            impuesto = self.importe * 0.21
        elif self.condicion_impositiva == "IVA No Inscripto":
            impuesto = 0
        elif self.condicion_impositiva == "IVA Exento":
            impuesto = 0
        else:
            raise ValueError("Condición impositiva no válida.")

        total = self.importe + impuesto
        return impuesto, total

    def clone(self):
        return copy.deepcopy(self)

factura_prototype = Factura(1000, "IVA Responsable")
factura1 = factura_prototype.clone()
factura1.generar_factura()
print("--------------------------")
factura2 = factura_prototype.clone()
factura2.condicion_impositiva = "IVA No Inscripto"
factura2.generar_factura()
print("--------------------------")
factura3 = factura_prototype.clone()
factura3.condicion_impositiva = "IVA Exento"
factura3.generar_factura()

