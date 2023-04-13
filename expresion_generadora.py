# Expresion generadora (es un generador anonimo)

multiplicacion = (valor * valor for valor in range(4))
print(multiplicacion)
print(type(multiplicacion))
for numero in multiplicacion:
    print(numero)

# Tambien se puede pasar una expresion generadora a una funcion (sin parentesis)
import math
suma = sum(valor*valor for valor in range(4))
print(f'Resultado de la suma: {suma}')

# Tambien podemos usar una lista o otro iterador
lista = ['Juan', 'Perez']
generador = (valor for valor in lista)
for valor in generador:
    print(f'Valor de la lista: {valor}')

# Crear un str a partir de un generador creado a partir de una lista
lista = ['Karla', 'Gomez']
contador = 0
# definimos una funcion para incrementar el contador
def incrementar():
    global contador
    contador += 1
    return contador
# La primera parte es el yield, la segunda es el for
generador = (f'{incrementar()}.{nombre}' for nombre in lista)
lista = list(generador)
print(lista)
cadena = ', '.join(lista)
print(f'La cadena generada: {cadena}')