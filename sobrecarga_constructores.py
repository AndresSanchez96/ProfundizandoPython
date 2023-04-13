# Simulacion de sobrecarga de constructores en python
# nos permite crear otras formas de crear objetos

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @classmethod
    def crear_persona_vacia(cls):
        return cls(None, None)

    @classmethod
    def crear_persona(cls, nombre, apellido):
        return cls(nombre, apellido)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}'

persona1 = Persona('Juan', 'Perez')
persona_vacio = Persona.crear_persona_vacia()
persona_con_valores = Persona.crear_persona('Karla', 'Gomez')
print(persona_vacio, persona1, persona_con_valores)