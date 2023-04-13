# su usa para unir uno o varios iterables

numeros = [1,2,3]
lestras = ['a','b','c']
identidicadores = 321, 322, 323, 324, 325
conjunto = {6,4,0,9,8,15,10}
mezcla = zip(numeros, lestras, identidicadores, conjunto)
print(mezcla)
print(list(mezcla))

#Iterar en paralelo
for numero, letra, id, aleatorio in zip(numeros,lestras,identidicadores, conjunto):
    print(f'Numero: {numero}, Letra: {letra}, Id: {id}, aleatorio: {aleatorio}')


nueva_lista = []
for numero, letra, id, aleatorio in zip(numeros,lestras,identidicadores, conjunto):
    nueva_lista.append(f'{id}-{numero}-{letra}-{aleatorio}')
print(nueva_lista)

#Unzip
mezcla = [(1,'a'),(2,'b'),(3,'c')]
numeros, letras = zip(*mezcla)
print(f'Numeros: {numeros}, Letras: {letras}')

# Ordenamiento usando zip
letras = ['c','d','a','e','b']
numeros = [3,2,4,1,0]
mezcla = zip(letras, numeros)
print(tuple(mezcla))
# ordenar por letra
print(sorted(zip(letras,numeros))) #Sorted ordena

# Crear un diccionario xon zip y dos iterables
llaves = ['Nombre', 'Apellido', 'Edad']
valores = ['Juan', 'Perez', 18]
diccionario = dict(zip(llaves, valores))
print(diccionario)

# Actualizar un elemento del diccionario
llave = ['Edad']
nueva_edad = [28]
diccionario.update(zip(llave, nueva_edad))
print(diccionario)