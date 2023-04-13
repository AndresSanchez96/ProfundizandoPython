# Profundizando en set
# Un set es una coleccion de elementos unicos y es mutable
# Los elementos de un ser deben ser inmutables

conjunto = {'Juan', True, 18.9}
print(conjunto)
#set vacio
conjunto = set()
print(conjunto)
# Mutable
conjunto.add('Juan')
print(conjunto)
# Contiene valores unicos
# Crear un set a partir de un interable
conjunto = set([4,5,6,7,4,8])
print(conjunto)
# Podemos agregar mas elmenentos o incluso otro set
conjunto2 = {100,200,300,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([20,30,40,40])
print(conjunto)

# Copiar un set (poco profunda, solo se copia las referencias)
conjunto_copia = conjunto.copy()
print(conjunto_copia)
# Verificar igualdad
print(f'Es igual en contenido? {conjunto == conjunto_copia}')
print(f'Es la misma referencia? {conjunto is conjunto_copia}')

#FUNCIONES DE CONJUNTOS CON SET
# Personas con distintas caracteristicas
pelo_negro = {'Juan', 'Karla', 'Pedro', 'Maria'}
pelo_rubio = {'Lorenzo', 'Laura', 'Marco'}
ojos_cafe = {'Karla', 'Laura'}
menores_30 = {'Juan', 'Karla', 'Maria'}
# UNION
# todos con ojos cafe y perlo rubio
print(ojos_cafe.union(pelo_rubio))

# (intersection) solo las personas con ojos_cafe y pelo rubio
print(ojos_cafe.intersection(pelo_rubio))
# (difference) pelo negro pero sin ojos cafe (no es comutativa)
print(pelo_negro.difference(ojos_cafe))
# (symmetric difference) pelo negro u ojos cafe pero no ambos
print(pelo_negro.symmetric_difference(ojos_cafe))

# Preguntar si un set esta contenido en otro (subset)
# Revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))

# Preguntar si un set contiene a otro set (superset)
# Revisar si los elementos del primer set estan contenidos en el otro set
print(menores_30.issuperset(pelo_negro))

# Preguntar si los de pelo negro no tienen pelo rubio (distjoint)
print(pelo_negro.isdisjoint(pelo_rubio))