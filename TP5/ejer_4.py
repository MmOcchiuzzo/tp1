import os

class State:
    def scan(self):
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

class AmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fmstate

    def toggle_memories(self):
        print("Cambiar a memoria AM")
        self.radio.state = self.radio.am_memory_state

class FmState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.amstate

    def toggle_memories(self):
        print("Cambiar a memoria FM")
        self.radio.state = self.radio.fm_memory_state

class AmMemoryState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["M1_AM", "M2_AM", "M3_AM", "M4_AM"]
        self.pos = 0
        self.name = "AM Memory"

    def toggle_amfm(self):
        print("Cambiando a FM")
        self.radio.state = self.radio.fm_memory_state

    def scan(self):
        print("Recorriendo memorias AM:")
        for station in self.stations:
            print("Sintonizando... Estación {} {}".format(station, self.name))

class FmMemoryState(State):
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["M1_FM", "M2_FM", "M3_FM", "M4_FM"]
        self.pos = 0
        self.name = "FM Memory"

    def toggle_amfm(self):
        print("Cambiando a AM")
        self.radio.state = self.radio.am_memory_state

    def scan(self):
        print("Recorriendo memorias FM:")
        for station in self.stations:
            print("Sintonizando... Estación {} {}".format(station, self.name))


class Radio:
    def __init__(self):
        self.fmstate = FmState(self)
        self.amstate = AmState(self)
        self.fm_memory_state = FmMemoryState(self)
        self.am_memory_state = AmMemoryState(self)
        self.state = self.fmstate

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def toggle_memories(self):
        self.state.toggle_memories()

    def scan(self):
        self.state.scan()

if __name__ == "__main__":
    os.system("clear")
    print("\nCrea un objeto radio y almacena las siguientes acciones")
    radio = Radio()
    actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.toggle_memories] + [radio.scan] * 3
    actions *= 2

    print("Recorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado")
    for action in actions:
        action()
