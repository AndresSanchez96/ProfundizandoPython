# LEER CONTENIDO ONLYNE
from urllib.request import urlopen

with urlopen('https://www.globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    #contenido = mensaje.read()
    contenido = mensaje.read().decode('UTF-8')
    print(contenido)

with open('Nuevo_archivo.txt','w', encoding='utf-8') as archivo:
    archivo.write(contenido)