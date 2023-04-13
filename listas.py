# Profundizando en listas
# las listas son mutables

nombres1 = ['Juan', 'Karla', 'Pedro']
nombres2 = 'Laura Maria Gonzalo Ernesto'.split() # split genera una lsita de una cadena
# Sumar listas
print(f'Sumar listas {nombres1 + nombres2}')
# Extender una lista sobre otra lista
nombres1.extend(nombres2)
print(f'Extender la lista1 con la lista2 {nombres1}')

# Lista de numeros
numeros1 = [10, 40, 15, 4, 20, 90, 4]
print(f'Lista original: {numeros1}')
# obtener el indice del primer elemento encontrado en una lista
#help(list.index)
print(f'Indice 4: {numeros1.index(4)}')

# Invertir el orden de los elementos de una lista
numeros1.reverse() #este metodo invierte los elementos
print(f'Lista invertida {numeros1}')

# Ordenar los elementos de una lista asc y des
numeros1.sort() # nos permite ordenar los elementos de la lista
print(f'Lista Ordenada: {numeros1}')
numeros1.sort(reverse=True)
print(f'Lista ordenada descendente {numeros1}')

# Obtener el valor minimo y maximo de una lista
print(f'Valor minimo: {min(numeros1)}')
print(f'Valor maximo: {max(numeros1)}')

# Copiar de los elementos de una lista
numeros2 = numeros1.copy()
print(f'Mismo contenido?: {numeros2 == numeros1}')

# slicing
numeros2 = numeros1[:]
print(f'Mismo contenido?: {numeros2 == numeros1}')

# Multiplicacion de listas
lista_multiplicacion = 5*[[2, 5]]
print(f'Misma resferencia? {lista_multiplicacion[0] is lista_multiplicacion[1]}')
print(f'Mismo contenido? {lista_multiplicacion[0] == lista_multiplicacion[1]}')
lista_multiplicacion[2].append(10)
print(lista_multiplicacion)

# Matrices en Python
matriz = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]
print(f'Matriz original: {matriz}')
print(f'Renglon 0, Columna 0: {matriz[0][0]}')
print(f'Renglon 2, columna 2: {matriz[2][2]}')

lista_listas =[[10,14,87,90,71],[4,5,6,7],[9,0,11,15,45,61,70]]
lista_listas.sort(key=len)
print(f'Ordenar Lista: {lista_listas}')

# sorted biult-in
nombres1 = ['Juan Carlos', 'Karla', 'Pedro', 'Esperanza']
nombres1 = sorted(nombres1)
print(nombres1)
# Ordenar de manera descendente
nombres1 = sorted(nombres1, reverse=True)
print(nombres1)