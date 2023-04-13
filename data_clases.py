from dataclasses import dataclass
from typing import ClassVar


@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacio: {self.nombre}')


domicilio1 = Domicilio('Saturno', 1)
persona1 = Persona('Juan', 'Perez', domicilio1)
print(persona1)
# Variable de clase
print(f'Variable de clase {Persona.contador_personas}')
# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}')
# Varibale con valores vacios
persona_vacia = Persona('Karla','',None)
print(f'Persona vacia: {persona_vacia}')
# Revisa igualdad entre objetos
persona2 = Persona('Juan','Perez', Domicilio('Jupiter', 30))
print(f'Objetos iguales? {persona2 == persona1}')
# Agregar eta clase a una coleccion
coleccion = {persona1, persona2} # es decir que los valores no se pueden modificar usando forzen=True
print(coleccion)
