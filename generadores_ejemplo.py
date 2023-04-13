# Generador de numeros del 1-5
def generador_numeros():
    numero = 0
    for numero in range(1, 6):
        yield numero
        print('Se reanuda la ejecucion de la funcion')


# Utilizar nuestro objeto generador
generador = generador_numeros()
print(f'Objeto generador: {generador}')
print(type(generador))

# Consumimos los valores del generador
for valor in generador:
    print(f'Numero producido en el generador: {valor}')

# Consumir a demanda
generador = generador_numeros()
try:
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
    print(f'Consumimos a demanda: {next(generador)}')
except StopIteration as e:
    print(f'Error al consumir generador')