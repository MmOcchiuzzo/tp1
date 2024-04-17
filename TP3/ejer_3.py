# 3) Genere una clase donde se instancie una comida rápida “hamburguesa” que 
# pueda ser entregada en mostrador, retirada por el cliente o enviada por 
# delivery. A los efectos prácticos bastará que la clase imprima el método de 
# entrega.

#Factory

from abc import ABC, abstractmethod

class Hamburguesa(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def entregar(self):
        pass

class HamburguesaMostrador(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.nombre} está lista para ser recogida en mostrador.")

class HamburguesaCliente(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.nombre} está lista para ser retirada por el cliente.")

class HamburguesaDelivery(Hamburguesa):
    def entregar(self):
        print(f"La hamburguesa {self.nombre} está en camino para ser entregada por delivery.")

def crear_hamburguesa(tipo, nombre):
    if tipo == 'mostrador':
        return HamburguesaMostrador(nombre)
    elif tipo == 'cliente':
        return HamburguesaCliente(nombre)
    elif tipo == 'delivery':
        return HamburguesaDelivery(nombre)
    else:
        raise ValueError("Tipo de entrega no válido.")

hamburguesa_mostrador = crear_hamburguesa('mostrador', "Clásica")
hamburguesa_cliente = crear_hamburguesa('cliente', "Clásica")
hamburguesa_delivery = crear_hamburguesa('delivery', "Clásica")

hamburguesa_mostrador.entregar()
hamburguesa_cliente.entregar()
hamburguesa_delivery.entregar()
