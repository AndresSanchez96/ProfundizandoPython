# Ejemplo atributos publicos, protegidos, privados

class MiClase:
    def __init__(self, publico, protegido, privado):
        self.publico = publico
        self._protegido = protegido
        self.__privado = privado

objeto = MiClase('Valor publico', 'Valor protegido', 'Valor privado')
# Acceso al atributo publico
print(objeto.publico)
# Modificar el valor publico
objeto.publico = 'Nuevo valor publico'
print(objeto.publico)

# Acceso al valor protegido
# Solo dentro de la misma clase o clases hijas
print(objeto._protegido) # no recomendado
# Modificar atributo protegido
objeto._protegido = 'Nuevo valor protegido' # mala practica
print(objeto._protegido)

# Acceso al valor privado
# solo dentro de la misma clase
# print(objeto.__privado)
# pero, convierte: objeto._clase__atributo_privado
print(objeto._MiClase__privado) # no es recomendado, mala practica