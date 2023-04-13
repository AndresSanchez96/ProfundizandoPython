# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros) # * desempaqueta los numeros de la lista
print(*numeros, sep=' - ')

# desempaquetando al momento de pasar un parametro a una funcion
def sumar(a, b, c):
    print(f'Resultado suma: {a+b+c}')

sumar(*numeros)

# Extraer algunas partes de una lista o iterable
mi_lista = list(range(1,7))
a, *b, c, d = mi_lista
print(a,b,c,d)

# Unir lista
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = [lista1, lista2]
print(f'Lista de listas: {lista3}')
lista3 = [*lista1, *lista2]
print(f'Lista unida: {lista3}')
lista4 = lista1 + lista2
print(lista4)

# unir diccionarios
dic1 = {'A':1, 'B':2, 'C':3}
dic2 = {'D':4, 'E':5}
dic3 = {**dic1, **dic2}
print(f'Unir Diccionarios: {dic3}')

# Construir una lista apartir de un str
lista = [*'Hola mundo']
print(lista)
print(*lista,sep='')
