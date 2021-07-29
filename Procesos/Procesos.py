class Gestion:

    def gestiondatos(self,cedula,lista):
        obj = None
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                obj = lista[i]
                break
        return obj

    def getPosicion(self,cedula,lista):
        pos = -1
        for i in range(len(lista)):
            if cedula == lista[i].cedula:
                pos = i
                break
        return pos

    def gestiondatos2(self,usuario,lista):
        lis = None
        nom = usuario
        # cla = clave

        for i in range(len(lista)):
            if nom == lista[i].usuario:
                lis = lista[i]
                break
        return lis

    def getPosicionUsua(self,usuario,lista):
        pos = -1
        for i in range(len(lista)):
            if usuario == lista[i].usuario:
                pos = i
                break
        return pos