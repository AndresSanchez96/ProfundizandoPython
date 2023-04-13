import math

# NaN significa Not a Number
# NaN no es sensible a mayusculas/minisculas
# NaN es un tipo de dato numerico indefinido
a = float('NaN')
print(f'a: {a}')
print(f'es NaN?: {math.isnan(a)}')
