# FUNCIONES LAMBDA
# son funciones anonimas, y son pequeñas (una linea de codigo)

def sumar(a, b):
    return a + b
# Con una funcion lambda (anonima, sin nombre, una sola linea de codigo)
# No se neceita agregar parentesis para los parametros
# NO se necesira return, pero si debe regresar una expresion valida
mi_funcion_lambda = lambda a, b: a + b
print(f'Resultado de sumar: {mi_funcion_lambda(5,6)}')

# Funcion lambda que no recibe argumentos pero se debe regresar una expresion valida
mi_funcion_lambda = lambda : 'Funcion sin argumentos'
print(f'Llamar funcion lambda sin argumentos: {mi_funcion_lambda()}')

# Funcion lambda con parametros por default
mi_funcion_lambda = lambda a=2, b=3: a + b
print(f'Resultado argumentos por dafault: {mi_funcion_lambda()}')

# Funcion lambda con argumentos variables *args y **kwargs
mi_funcion_lambda = lambda *args, **kwargs: len(args) + len(kwargs)
print(f'Resultado de argumentos variables: {mi_funcion_lambda(1,2,3, a=5,b=6)}')

# Funciones lambda con argumentos, argumentos cariables y valores por default
mi_funcion_lambda = lambda a, b, c=3, *args, **kwargs: a+b+c+len(args)+len(kwargs)
print(f'Resultado de la funcion lambda: {mi_funcion_lambda(1,2,4, 5,6,7, e=5,f=7)}')