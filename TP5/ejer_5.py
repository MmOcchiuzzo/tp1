import os

class Memento:
    def __init__(self, file, content):
        self.file = file
        self.content = content

class FileWriterUtility:
    def __init__(self, file):
        self.file = file
        self.content = ""
        self.history = []

    def write(self, string):
        self.content += string

    def save(self):
        memento = Memento(self.file, self.content)
        self.history.append(memento)
        if len(self.history) > 4:
            self.history.pop(0)

    def undo(self, step=0):
        if step >= len(self.history):
            step = len(self.history) - 1
        if step >= 0:
            memento = self.history[-1 - step]
            self.file = memento.file
            self.content = memento.content
            print(f"Undo realizado hasta el estado {step} atrás.")
        else:
            print("No hay más estados anteriores para deshacer.")

class FileWriterCaretaker:
    def save(self, writer):
        writer.save()

    def undo(self, writer, step=0):
        writer.undo(step)


if __name__ == '__main__':
    os.system("clear")
    print("Crea un objeto que gestionará la versión anterior")
    caretaker = FileWriterCaretaker()

    print("Crea el objeto cuyo estado se quiere preservar")
    writer = FileWriterUtility("GFG.txt")

    print("Se graba algo en el objeto y se salva")
    writer.write("Clase de IS2 en UADER\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional")
    writer.write("Material adicional de la clase de patrones\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se graba información adicional II")
    writer.write("Material adicional de la clase de patrones II\n")
    print(writer.content + "\n\n")
    caretaker.save(writer)

    print("Se invoca undo para retroceder 2 pasos")
    caretaker.undo(writer, 2)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")

    print("Se invoca undo para retroceder 1 paso")
    caretaker.undo(writer, 1)
    print("Se muestra el estado actual")
    print(writer.content + "\n\n")
