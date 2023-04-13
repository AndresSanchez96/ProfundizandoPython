# Profundizando en diccionarios

#los dic guardan un oreden a diferencia de los set
diccionario = {'Nombre':'Juan', 'Apellido':'Perez', 'Edad':28}
print(diccionario)
#Los dict son mutables, pero las llaves deben ser inmutables

# se agrega una llave si no se encuentra
diccionario['Departamento'] = 'Sistemas'
print(diccionario)

# No hay valores duplicados en las llaves de un diccionario
diccionario['Nombre'] = 'Juan Carlos'
print(diccionario)

#Reucperar elementos
print(diccionario['Nombre'])

# Metodo get recupera una llave pero si no existe no lanza error
# Ademas podemos regresar un valor en caso de que no exista
print(diccionario.get('Nombre', 'No se encontro la llave'))

# Metodo setdefault si modifica el dic si no encuentra la llave y agrega metodo default
nombre = diccionario.setdefault('Nombre', 'Valor por default')
print(nombre)
print(diccionario)

# Imprrmir con pprint
from pprint import pprint as pp
pp(diccionario)
