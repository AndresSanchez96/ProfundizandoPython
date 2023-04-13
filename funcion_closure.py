# Un closure es una funcnion que defina a otra, y ademas la resgresa
# La funcion anidada puede acceder a las variables locales definidas
# en funcion principal o externa

# Funcion principal
#def operacion(a, b):
    # Definimos una funcion interna o anidada
 #   def sumar():
  #      return a + b

   # # Retornar la funcion
    #return sumar

# Funcion Principal con lambda
def operacion (a, b):
    # Definimos una funcion lambda interna o anidada y la retornamos
    return lambda :a + b

mi_funcion_closure = operacion(5, 2)
print(f'Resultado de la funcion closure: {mi_funcion_closure()}')

# llamar la funcion regresada al vuelo
print(f'Resultado de la funcion closure al vuelo: {operacion(3, 2)()}')