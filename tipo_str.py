# Profundizando en el tipo str

from mi_clase import MiClase

# concatenacion automatica en python
variable = 'adios'
mensaje = 'Hola' 'Mundo' + variable
mensaje += 'Universidad' 'Python'
#print(mensaje)

#help(MiClase)
#print(MiClase.__doc__) #Solo llama la documentacion de la clase
#print(MiClase.__init__.__doc__) # la documentacion del metodo init
#print(MiClase.mi_metodo.__doc__) # documentacion del metodo

#help(str.capitalize)
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()
#print(f'mensaje1: {mensaje1}, id:{id(mensaje1)}')
#print(f'mensaje2: {mensaje2}, id:{id(mensaje2)}')

#help(str.join)
tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
mensaje = ' '.join(tupla_str)
#print(f'Mensaje: {mensaje}')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
mensaje = ', '.join(lista_cursos)
#print(f'Mensaje: {mensaje}')

diccionario = {'nombre':'Juan', 'Apellido':'Perez', 'Edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
#print(f'Llaves: {llaves}')
#print(f'Valores: {valores}')

#help(str.split) convertir una cadena a lista
cursos = 'Java Python JavaScript Angular Spring Excel'
lista_cursos = cursos.split()
#print(f'Lista de cursos: {lista_cursos}')

cursos_separados_coma = 'Java,Python,JavaScript,Angular,Spring,Excel'
lista_cursos = cursos_separados_coma.split(',')
#print(f'Lista de cursos: {lista_cursos}')

lista_cursos = cursos_separados_coma.split(',', 2)
#print(f'Lista de cursos: {lista_cursos}')

#Dar formato a un str
nombre = 'Juan'
edad = 28
mensaje_con_formato = 'Mi nombre es: %s y tengo %d años'%(nombre,edad) # '%' nos permite sustituir
#print(mensaje_con_formato)

persona = ('Karla','Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.2f'%persona
#print(mensaje_con_formato)

# metodo Format

nombre = 'Juan'
edad = 28
sueldo = 5000.00
mensaje = 'Nombre {} Edad {} Sueldo {:.2f}'.format(nombre, edad, sueldo)
#print(mensaje)

mensaje = 'Nombre {0} Edad {1} Sueldo {2:.2f}'.format(nombre, edad, sueldo)
#print(mensaje)

# Multiplicacion str
resultado = 5 * 'Hola'
#print(f'Resultado: {resultado}')

# Multiplicacion de tuplas
resultado = 5 * ('Hola', 'Mundo')
#print(f'Resultado: {resultado}')

# Multiplicacion de listas
resultado = 10 * [0]
#print(f'Resultado: {resultado}, largo: {len(resultado)}')

# CARACTERES DE ESCAPE
resultado = 'Hola \' Mundo' # \ caracter de escape
#print(f'Resultado: {resultado}')
resultado = 'Se va a eliminar el punto .\b' # \b quita el ultimo caracter
#print(f'Resultado: {resultado}')

# Caracter \
resultado = 'c:\\directorio\\Juan' ## Se usa la doble \\ para escapar de la primera \
#print(f'Resultado: {resultado}')

# RAW string
resultado = r'Cadena con \n salto de linea'
#print(f'Resultado: {resultado}')

# Caracteres UNICODE
#print('Hola\u0020Mundo')
#print('Notacion simple:', '\u0041')
#print('Notacion extendida:','\U00000041')

# CARACTERES BYTES
caracteres_en_bytes = b'Hola Mundo'
#print(caracteres_en_bytes)

mensaje = b'Universidad Python'
#print(mensaje[0]) # el inidice 0 es U pero en byte por la b
#print(chr(mensaje[0]))

lista_caracteres = mensaje.split()
#print(lista_caracteres)

# CONVERTIR STR A BYTES
string = 'Programación con Python'
print('string original:', string)
bytes = string.encode('UTF-8')
print('Bytes codificado: ', bytes)

# CONVERTIR DE BYTES A STR
string2 = bytes.decode('UTF-8')
print('String decodificado: ', string2)