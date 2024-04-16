class Component:
    def show(self, indent=0):
        pass

class Piece(Component):
    def __init__(self, name):
        self.name = name

    def show(self, indent=0):
        print("  " * indent + f"-> Pieza: {self.name}")

class SubAssembly(Component):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def show(self, indent=0):
        print("  " * indent + f"-> Subconjunto: {self.name}")
        for child in self.children:
            child.show(indent + 1)

# Producto principal formado por tres subconjuntos, cada uno con cuatro piezas
main_product = SubAssembly("Producto Principal")

sub_assembly_1 = SubAssembly("Subconjunto 1")
sub_assembly_1.add(Piece("Pieza 1.1"))
sub_assembly_1.add(Piece("Pieza 1.2"))
sub_assembly_1.add(Piece("Pieza 1.3"))
sub_assembly_1.add(Piece("Pieza 1.4"))

sub_assembly_2 = SubAssembly("Subconjunto 2")
sub_assembly_2.add(Piece("Pieza 2.1"))
sub_assembly_2.add(Piece("Pieza 2.2"))
sub_assembly_2.add(Piece("Pieza 2.3"))
sub_assembly_2.add(Piece("Pieza 2.4"))

sub_assembly_3 = SubAssembly("Subconjunto 3")
sub_assembly_3.add(Piece("Pieza 3.1"))
sub_assembly_3.add(Piece("Pieza 3.2"))
sub_assembly_3.add(Piece("Pieza 3.3"))
sub_assembly_3.add(Piece("Pieza 3.4"))

main_product.add(sub_assembly_1)
main_product.add(sub_assembly_2)
main_product.add(sub_assembly_3)

# Mostrar la configuración actual
print("Configuración actual:")
main_product.show()

# Agregar un subconjunto opcional adicional
optional_sub_assembly = SubAssembly("Subconjunto Opcional")
optional_sub_assembly.add(Piece("Pieza O.1"))
optional_sub_assembly.add(Piece("Pieza O.2"))
optional_sub_assembly.add(Piece("Pieza O.3"))
optional_sub_assembly.add(Piece("Pieza O.4"))

main_product.add(optional_sub_assembly)

# Mostrar la configuración actual actualizada
print("\nConfiguración actualizada:")
main_product.show()
