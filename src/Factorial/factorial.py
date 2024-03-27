#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys
def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")

    elif num == 0: 
        return 1
        
    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

def calcular_factoriales(desde, hasta):
    for num in range(desde, hasta + 1):
        print("Factorial de", num, "! es", factorial(num))

def obtener_rango(argumento):
    if argumento.startswith("-"):
        hasta = int(argumento[1:])
        desde = 1
    elif argumento.endswith("-"):
        desde = int(argumento[:-1])
        hasta = 60
    else:
        desde, hasta = map(int, argumento.split("-"))
    return desde, hasta

if len(sys.argv) == 1:
    rango = input("Por favor, ingrese el rango de números (desde-hasta): ")
else:
    rango = sys.argv[1]

desde, hasta = obtener_rango(rango)

if desde >= hasta:
    print("El extremo 'desde' debe ser menor que el extremo 'hasta'.")
    sys.exit()

calcular_factoriales(desde, hasta)

