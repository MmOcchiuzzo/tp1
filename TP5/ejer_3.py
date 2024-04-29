class Subject:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, id):
        for observer in self.observers:
            observer.update(id)

class Observer:
    def __init__(self, id):
        self.id = id

    def update(self, received_id):
        if self.id == received_id:
            print(f"El ID {received_id} ha sido recibido por el observador {self.__class__.__name__}.")


class ObserverA(Observer):
    def __init__(self):
        super().__init__("ABCD")

class ObserverB(Observer):
    def __init__(self):
        super().__init__("EFGH")

class ObserverC(Observer):
    def __init__(self):
        super().__init__("IJKL")

class ObserverD(Observer):
    def __init__(self):
        super().__init__("MNOP")

if __name__ == "__main__":
    subject = Subject()

    observer_a = ObserverA()
    observer_b = ObserverB()
    observer_c = ObserverC()
    observer_d = ObserverD()

    subject.add_observer(observer_a)
    subject.add_observer(observer_b)
    subject.add_observer(observer_c)
    subject.add_observer(observer_d)

    emitted_ids = ["ABCD", "WXYZ", "EFGH", "1234", "IJKL", "5678", "MNOP", "9101"]

    for emitted_id in emitted_ids:
        subject.notify_observers(emitted_id)
