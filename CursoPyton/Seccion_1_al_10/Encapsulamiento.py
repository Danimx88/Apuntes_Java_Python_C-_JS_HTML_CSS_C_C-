class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrar_detalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')

persona1 = Persona('Juan', 'Perez', 28)
persona1._nombre = 'Juan Carlos' ##Cuando se pone _ significa que no se puede acceder fuera de la clase a nuestro objeto a menos para pruebas pero no para produccion
persona1.mostrar_detalle()
