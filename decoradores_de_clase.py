# Decoradores de clase
# Permiten transformar de manera programatica nuestra clase
# es similar a los decoradores de funciones (es metaprogramacion)
import inspect


def decorador_repr(cls):
    print('Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    # Revisamos los atributos de la clase con el metodo vars
    atributos = vars(cls)
    for nombre, atributo in atributos.items():
        print(nombre, atributo)

    # Revisamos si se ha sobreescrito __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreesctrito el metodo __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma del metodo __init__: {firma_init}')

    # Recuperamos los paremetros excepto el primero que es self
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parametros init: {parametros_init}')

    # Revisamos si cada parametro tiene un metodo property asociado
    for parametro in parametros_init:
        # Property es un valor de tipo buil-in para preguntar
        # si se esta utlizando decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        #if not
    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido):
        print('Se ejecuta el iniciador')
        self._nombre = nombre
        self._apellido = apellido

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido


persona1 = Persona('Juan', 'Perez')