# Ejemplo de herencia simple
class ListaSimple:
    def __init__(self, elementos):
        self._elementos = list(elementos)

    def agregar(self, elemento):
        self._elementos.append(elemento)

    def __getitem__(self, indice):
        return self._elementos[indice]

    def ordenar(self):
        self._elementos.sort() # ordena

    def __len__(self):
        return len(self._elementos)

    def __repr__(self):
        return f'{self.__class__.__name__}({self._elementos!r}'

class ListaOrdenada(ListaSimple):
    def __init__(self, elementos = []):
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()

    def agregar(self, elemento):
        super().agregar(elemento)
        # Simpre se ordena
        self.ordenar()

class ListaEnteros(ListaSimple):
    def __init__(self, elementos=[]):
        for elemento in elementos:
            self._validar(elemento)
        # Una vez validados los elementos, los agregamos
        super().__init__(elementos)

    def _validar(self, elemento):
        # Validamos si el elemento es de tipo entero
        if not isinstance(elemento, int):
            raise ValueError(f'No es un valor entero {elemento}')

    # Sobreescribimos el metodo agregar de la clase padre
    def agregar(self, elemento):
        self._validar(elemento)
        # una vez validado agregamos a la lista
        super().agregar(elemento)

# Lista de enteros ordenada
class ListaEnterosOrdenada(ListaEnteros, ListaOrdenada):
    pass

lista_simple = ListaSimple([5, 3, 6, 8])
print(lista_simple)
#lista ordenada
lista_ordenada = ListaOrdenada([4,3,6,9,10,-1])
print(lista_ordenada)
lista_ordenada.agregar(-14)
print(lista_ordenada)
print(len(lista_ordenada))
# lista de enteros
lista_enteros = ListaEnteros([1,3,4])
print(lista_enteros)

#Lista de enteros ordenada
lista_enteros_ordenada = ListaEnterosOrdenada([4,5,-1,10,14,-4])
print(lista_enteros_ordenada)
lista_enteros_ordenada.agregar(-20)
print(lista_enteros_ordenada)
# Saber las clases padres y su orden
print(ListaEnterosOrdenada.__bases__)

# MRO METHOD RESOLUTION ORDER
print(ListaEnterosOrdenada.__mro__)

# ISINSTANCE
print('Es entero?', isinstance(10,int))
print('Es cadena?', isinstance('Hola', str))
print('Es lista de enteros ordenada?', isinstance(lista_enteros_ordenada, ListaEnterosOrdenada))
print('Es lista enteros?', isinstance(lista_enteros_ordenada, ListaEnteros ))
print('Es de varios tipos?', isinstance(lista_enteros_ordenada, (ListaEnteros, ListaSimple, ListaOrdenada)))