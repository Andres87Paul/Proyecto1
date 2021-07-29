import os
class  Entradas2:

    def Int(self,msg):

        while True:
            try:
                n = int(input(msg))
                break
            except ValueError:
                print("¡Debes ingresar un número!")
        return n