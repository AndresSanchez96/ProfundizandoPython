# Profundizando en tuplas

# Declarar variables
a, b = 'Hola', 'Adios'
# swap (intercambio)
a, b = b, a

# Regresar multiples valores
def minmax(elementos):
    return min(elementos), max(elementos)

min,  max = minmax([1,2,3,4,5])
print(f'Valor minimo: {min}, Valor Maximo: {max}')

# regresar una suma de valores
resultado = sum((1,2,3,4,5))
print(f'Resultado: {resultado}')

def sumar(*args):
    return sum(args)

resultado = sumar(1,2,3,4,5)
print(f'Resultado: {resultado}')