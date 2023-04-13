#ALCANCE DE VARIABLES
#scope, tiempo de vida de una variable

var_global = 'variable global'

def imprimir():
    # ACceder a una variable global
    global var_global # asi se puede trabajar para lectura y escritura
    print(f'Variable globar desed funcion: {var_global}')
    # Definicion de variable local
    var_local = 'Variable local'
    print(f'Variable local desde funcion: {var_local}')
    var_global = 'Nuevo valor de la variable global'

imprimir()
imprimir()