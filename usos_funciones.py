# Las funciones en python son ciudadanas de primera clase

# Difinimos la funcion
def sumar(a, b):
    return a + b

# 1. Asignar una funcion a una variable (no se usa parentesis)
mi_funcion = sumar

# Verificar el tipo de la variable
print(type(mi_funcion))

# Llamamos la funcion a traves de la variable
resultado = mi_funcion(5,8)
print(f'Resultado de la suma: {resultado}')

# 2. Funcion como argumento
def operacion(a, b, sumar_arg):
    print(f'Resultado de sumar: {sumar_arg(a, b)}')

operacion(4, 5, sumar)

# 3. podemos retornar una funcion
def retornar_funcion():
    #retornamos una funcion
    return sumar

mi_funcion_retornada = retornar_funcion()
print(f'Resultado funcion retornada: {mi_funcion_retornada(5, 7)}')