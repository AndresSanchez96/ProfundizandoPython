import json
import urllib.request

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
respuesta = urllib.request.urlopen(peticion)
cuerpo_respuesta = respuesta.read()
# Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))

# Ejer1 Acceder a la descripcion del clima
descripcion_clima = json_respuesta.get('clima')[0].get('principal')
print(f'Descripcion clima: {descripcion_clima}')

# Ejercicio2 Mostrar temperatura max y min
temp_min = json_respuesta.get('principal')['temp_min']
print(f'Temperatura minima: {temp_min}')
temp_max = json_respuesta.get('principal')['temp_max']
print(f'Temperatura maxima: {temp_max}')
temp_actual = json_respuesta.get('principal')['temp']
print(f'Temperatura actual: {temp_actual}')
sensacion = json_respuesta.get('principal')['sensacion']
print(f'Sensacion termica: {sensacion}')

print(f'Id: {json_respuesta["id"]}')