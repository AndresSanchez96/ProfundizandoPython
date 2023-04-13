# orden de inicializacion de objetos
class Padre:
    def __init__(self):
        print('Inicializador Padre')

    def metodo(self):
        print('Metodo Padre')

class Hijo(Padre):
    # Se manda a llamr el metedo __init__ de la clase padre
    # Simepre y cuando la clase hijo no defina su propio metodo init
    #definimos el metodo inir
    def __init__(self):
        # de manera opcional podemos llamar el metodo init de la clase padre
        # con super
        super().__init__()
        print('Inicializador hijo')

    # sobreescribimos el metodo heredado de la clase padre
    def metodo(self):
        print('Mettodo sobreescrito hijo')
        super().metodo()

#padre1 = Padre()
#padre1.metodo()
hijo1 = Hijo()
hijo1.metodo()