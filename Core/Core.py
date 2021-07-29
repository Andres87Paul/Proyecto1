from Proyecto1.Dominio.Entidades import *
from Proyecto1.Entradas.Entradas import *
from Proyecto1.Procesos.Procesos import *
from Proyecto1.Menu.Menu import *
from Proyecto1.Archivos.Archivos import *
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import os
import sys


class Core2:
    def __init__(self):
        self.ObM = Menu2()
        self.ObE = Entradas2()
        self.ObG = Gestion()
        self.ObA = Archivo()
        self.lista = []


    def main1(self):
        while True:
            try:
                listamo=[]
                usuario = input("INGRESE USUARIO: ")
                clave = input("INGRESE CLAVE: ")
                # ADICIONADO PARA MANEJO DE FILE
                self.lista = self.ObA.listausuarios("USUARIOS.csv")
                lis = self.ObG.gestiondatos2(usuario,self.lista)
                # print(lis.getUsua())
                # objeto = Usuarios("PAUL","APAF1")
                ObUser =lis.getUser()
                v1=ObUser
                ObClave = lis.getClave()
                v2=str.strip(ObClave)

                if lis!=None:

                    if usuario == v1 and clave == v2:
                        print("USUARIO Y CLAVE CORRECTA\n")
                        self.main()
                    else:
                        print("CLAVE INCORRECTA, POR FAVOR INGRESE LOS DATOS CORRECTOS\n")
                else:
                    print("NO EXISTE")
                    # on.system("")

            except:
                print("INGRESE UN USUARIO O CONTRASEÑA VALIDA\n")
                #     input("<ENTER>PARA CONTINUAR...")
                #print(obj.getUsua())

    def main(self):
        print("CARGANDO EL SISTEMA")
        self.barra()
        print(Fore.GREEN+"  _____      # ________     # ______      # _________  # ______      # ___ __ __     # ________      #")
        print(Fore.GREEN+"/_____/\     #/_______/\    #/_____/\     #/________/\ #/_____/\     #/__//_//_/\    #/_______/\     #")
        print(Fore.GREEN+"\::::_\/_    #\__.::._\/    #\::::_\/_    #\__.::.__\/ #\::::_\/_    #\::\| \| \ \   #\::: _  \ \    #")
        print(Fore.GREEN+"  \_::._\:\  #   _\::\ \__  #  \_::._\:\  #    \::\ \  #  \::___\/_  #  \:.\-/\  \ \ #  \:: __  \ \  #")
        print(Fore.GREEN+"    /____\:\ #  /__\::\__/\ #    /____\:\ #     \::\ \ #   \:\____/\ #   \. \  \  \ \#   \:.\ \  \ \ #")
        print(Fore.GREEN+"    \_____\/ #  \________\/ #    \_____\/ #      \__\/ #    \_____\/ #    \__\/ \__\/#    \__\/\__\/ #")
        print(Fore.BLUE+"          ##              ##             ##            ##             ##               ##               ##")
        print("                                \n")
        print("\t ******MENU DE OPCIONES******")
        print("                                \n")

        tupla=("REGISTRAR CLIENTES","CONSULTAR CLIENTES","ACTUALIZAR CLIENTES","ELIMINAR CLIENTES","LISTAR CLIENTES","INTEGRANTES","SALIR")
        op = self.ObM.menu(tupla)


        if op == 1:

            print("*****REGISTRAR DATOS DE CLIENTES******")
            self.registrar()
            self.main()
        if op == 2:
            print("*****CONSULTAR DATOS DE CLIENTES******")
            self.consultar()
            self.main()
        if op == 3:
            print("*****ACTUALIZAR DATOS DE CLIENTES******")
            self.actualizar()
            self.main()
        if op == 4:
            print("*****ELIMINAR DATOS DE CLIENTES******")
            self.eliminar()
            self.main()
        if op == 5:
            print("*****LISTAR DATOS DE CLIENTES******")
            self.listar()
            self.main()
        if op == 6:
            print("*************INTEGRANTES**************\n")
            self.integrantes()
            self.main()
        if op == 7:
            print("*****SALIR******")
            self.limpiar()

    def registrar(self):

        cedula =   input("INGRESAR CEDULA: ")

        self.lista = self.ObA.listaclientes("SEGUNDOA.csv")
        pos = self.ObG.getPosicion(cedula, self.lista)
        if pos == -1:

            nombre =   input("INGRESAR NOMBRE: ")
            edad =     input("INGRESAR EDAD: ")
            empresa =  input("INGRESAR EMPRESA: ")
            telefono = input("INGRESAR TELEFONO: ")

            obC1 = Cliente(cedula,nombre,edad,empresa,telefono)
            # self.lista.append(obC1)
            registro = obC1.cedula+";"+obC1.nombre+";"+obC1.edad+";"\
            +obC1.empresa+";"+obC1.telefono+";\n"
            self.ObA.insertar("SEGUNDOA.csv",registro,"a")
            self.barra()
            print("REGISTROS GUARDADOS CON EXITO")
        else:
            print("CEDULA YA EXISTE")
        input("<ENTER>PARA CONTINUAR...")

    def listar(self):
        # ADICIONADO PARA MANEJO DE FILE
        self.lista = self.ObA.listaclientes("SEGUNDOA.csv")

        for i in range(len(self.lista)):
            # print(self.lista[i].getDatos())
            # self.barra()
            print(self.lista[i].listar())
        input("<ENTER>PARA CONTINUAR...")

    def consultar(self):
        cedula=input("INGRESE CEDULA: ")
        # ADICIONADO PARA MANEJO DE FILE
        self.lista = self.ObA.listaclientes("SEGUNDOA.csv")
        obj=self.ObG.gestiondatos(cedula,self.lista)
        if obj!=None:
            self.barra()
            print(obj.getDatos())
        else:
            self.barra()
            print("NO EXISTE")
        input("<ENTER>PARA CONTINUAR...")

    def actualizar(self):
        cedula = input("INGRESE CEDULA: ")
        self.lista = self.ObA.listaclientes("SEGUNDOA.csv")
        pos = self.ObG.getPosicion(cedula, self.lista)
        if pos>-1:
            print(self.lista[pos].getDatos())
            nombre=input("nombre")
            edad = input("edad")
            empresa = input("empresa")
            telefono = input("telefono")
            self.lista[pos].nombre=nombre
            self.lista[pos].edad = edad
            self.lista[pos].empresa = empresa
            self.lista[pos].telefono = telefono

            # ADICIONADO PARA MANEJO DE FILE
            msg = ""
            for i in range(len(self.lista)):
                msg = msg + self.lista[i].cedula + ";" \
                      + self.lista[i].nombre + ";" \
                      + self.lista[i].edad + ";" \
                      + self.lista[i].empresa + ";" \
                      + self.lista[i].telefono + ";\n"
            # print(msg)
            self.ObA.insertar("SEGUNDOA.csv", msg, "w")
            self.barra()
            print("REGISTROS GRABADOS CON EXITO")

    def eliminar(self):
        cedula = input("INGRESE CEDULA: ")
        self.lista = self.ObA.listaclientes("SEGUNDOA.csv")
        pos = self.ObG.getPosicion(cedula, self.lista)
        if pos>-1:
            print(self.lista[pos].getDatos())
            self.lista.pop(pos)
            # ADICIONADO PARA MANEJO DE FILE
            msg = ""
            for i in range(len(self.lista)):
                msg = msg + self.lista[i].cedula + ";" \
                      + self.lista[i].nombre + ";" \
                      + self.lista[i].edad + ";" \
                      + self.lista[i].empresa + ";" \
                      + self.lista[i].telefono + ";\n"
            # print(msg)
            self.ObA.insertar("SEGUNDOA.csv", msg, "w")

            self.barra()
            print("REGISTRO ELIMINADO CON EXITO")
        else:
            self.barra()
            print("CEDULA NO EXISTE")

    def integrantes(self):
        self.barra()
        print("TECNOLOGIA SUPERIOR EN DESARROLLO DE SOFTWARE")
        print("2A NOCTURNA\n")
        print("1.- KATHERINE DANIELA LINDAO JORDAN")
        print("2.- KEN ARMANDO JIMENEZ MEJIA")
        print("3.- ANDRES PAUL AVENDAÑO FIGUEROA")
        print("4.- JOSE ROBERTO CORTEZ PERALTA")
        print("5.- DENILSON ELGIN GONZALEZ SOLANO\n")

        input("<ENTER>PARA CONTINUAR...")

    def barra(self):
        import sys
        import time
        import tqdm as tqdm
        from tqdm import tqdm
        for i in tqdm(range(10)):
            time.sleep(0.1)

     # def limpiar(self):
     #
     #     import os
     #     clear = lambda: os.system('cls')
     #     clear()





