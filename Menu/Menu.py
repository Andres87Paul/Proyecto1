from Proyecto1.Entradas.Entradas import *
import os

class Menu2:

    def __init__(self):
        self.entradaob = Entradas2()

    def menu(self,tupla):
        for i in range(len(tupla)):
            print(str(i + 1) + ".- " + tupla[i] + ".")
        print("**************************************")
        op = -1
            # SE DESTRUYE CUANDO ES FALSO (F O F)
        while op < 1 or op > len(tupla):
            op =  self.entradaob.Int("ingrese una opcion[1.." + str(len(tupla)) + "]:")
            print("**************************************\n\n")
        return op