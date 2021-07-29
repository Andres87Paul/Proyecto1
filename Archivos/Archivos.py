from Proyecto1.Dominio.Entidades import *

class Archivo:

    def insertar(self,nombre,datos,modo):
        archivo = open(nombre,modo)
        archivo.write(datos)
        archivo.close()

    def listaclientes(self,nombre):
        lista = []
        try:
            archivo = open(nombre,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Cliente(tupla[0],tupla[1],tupla[2],tupla[3],tupla[4])
                lista.append(obj)
            archivo.close()
        except:
            print("ERROR DE LECTURA")
        return lista


    def listausuarios(self,nombre):
        lista = []
        try:
            archivo = open(nombre,"r")
            for linea in archivo.readlines():
                tupla = linea.split(";")
                obj = Usuarios(tupla[0],tupla[1])
                lista.append(obj)
            archivo.close()
        except:
            print("ERROR DE LECTURA")
        return lista