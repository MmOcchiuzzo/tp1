# Extienda el ejemplo visto en el taller en clase de forma que se pueda utilizar 
# para construir aviones en lugar de vehículos. Para simplificar suponga que un 
# avión tiene un “body”, 2 turbinas, 2 alas y un tren de aterrizaje. 

import os

class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder

    def getVehicle(self):
        vehicle = Vehicle()
        
        body = self.__builder.getBody()
        vehicle.setBody(body)
        
        for _ in range(2):
            engine = self.__builder.getEngine()
            vehicle.attachEngine(engine)
        
        for _ in range(2):
            wing = self.__builder.getWing()
            vehicle.attachWing(wing)
        
        landing_gear = self.__builder.getLandingGear()
        vehicle.setLandingGear(landing_gear)

        return vehicle

class Vehicle:
    def __init__(self):
        self.__engines = []
        self.__wings = []
        self.__body = None
        self.__landing_gear = None

    def setBody(self, body):
        self.__body = body

    def attachEngine(self, engine):
        self.__engines.append(engine)

    def attachWing(self, wing):
        self.__wings.append(wing)

    def setLandingGear(self, landing_gear):
        self.__landing_gear = landing_gear

    def specification(self):
        print("Especificaciones del avión:")
        print("Cuerpo:", self.__body.shape)
        print("Número de turbinas:", len(self.__engines))
        print("Número de alas:", len(self.__wings))
        print("Tipo de tren de aterrizaje:", self.__landing_gear.type)

class Builder:
    def getBody(self): pass
    def getEngine(self): pass
    def getWing(self): pass
    def getLandingGear(self): pass

class AirplaneBuilder(Builder):
    def getBody(self):
        body = Body()
        body.shape = "Avión"
        return body

    def getEngine(self):
        engine = Engine()
        engine.type = "Turbina"
        return engine

    def getWing(self):
        wing = Wing()
        wing.type = "Ala"
        return wing

    def getLandingGear(self):
        landing_gear = LandingGear()
        landing_gear.type = "Triciclo"
        return landing_gear

class Engine:
    type = None

class Wing:
    type = None

class Body:
    shape = None

class LandingGear:
    type = None

def main():
    airplane_builder = AirplaneBuilder()
    director = Director()
    director.setBuilder(airplane_builder)
    airplane = director.getVehicle()
    airplane.specification()

if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un avión\n")
    main()
