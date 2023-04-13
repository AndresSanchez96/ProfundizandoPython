# Unpacking - desempaquetado
valores = 1,2,3
print(valores)

valor1, valor2, valor3 = 1, 2, 3
print(valor1, valor2, valor3)

valor1, valor2, *valor3 = 1,2,3,4,5,6,7,8,9
print(valor1,valor2,valor3)

# help(str.partition)
hora, separador, minutos = '11:37'.partition(':')
print(hora, separador, minutos)
