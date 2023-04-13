numeros = range(10)
lista_pares = []

# creamos una nueva lista con los valores pares
for numero in numeros:
    #Revisamos si es par
    if numero % 2 == 0:
        lista_pares.append(numero*numero)

print(f'Lista de pares: {lista_pares}')

# Hacemos lo mismo pero con list comprehensions
# [expresion for var in coleccion if condicion]
# La condicion del if es opcional

lista_pares = []
lista_pares = [numero*numero for numero in numeros if numero % 2 == 0]
print(f'Resultado con list comprehension: {lista_pares}')

# Un ejemplo similar pero con dos condiciones
#Solo se agrega el valor a la lista cuando el valor cumple ambas condiciones
# Es decir, debe ser divisible entre 2 y divisible entre 6

pares = [numero for numero in range(50) if numero % 2 == 0 and numero % 6 == 0]
print(f'Lista divisible entre 2 y 6: {pares}')

# Ejemplo con if else
lista_pares = []
lista_impares = []
for numero in range(10):
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)
print(f'Lista pares {lista_pares}')
print(f'Lista impares: {lista_impares}')

# El mismo pero usando listcomprehensions
lista_pares = []
lista_impares = []
[lista_pares.append(numero) if numero%2==0 else lista_impares.append(numero)
 for numero in range(10)]
print(f'Lista pares {lista_pares}')
print(f'Lista impares: {lista_impares}')

# Lista de lsitas
lista_listas = [[1,2,3], [4,5,6], [7,8,9,10]]
# Convertimos la lista de listas en una sola lista
lista_simple = [valor for sublista in lista_listas for valor in sublista]
print(f'Lista simple: {lista_simple}')

# Numeros pares
lista_pares = []
lista_impares = []
lista_pares = [valor for sublista in lista_listas for valor in sublista if valor % 2 == 0]
print(f'Lista pares {lista_pares}')
print(f'Lista impares: {lista_impares}')
