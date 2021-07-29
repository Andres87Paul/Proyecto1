class Persona:
    def __init__(self,cedula,nombre,edad):
        self.cedula = cedula
        self.nombre = nombre
        self.edad   = edad


    def getDatos(self):
        return "Cedula:"+self.cedula\
               +"\nNombre:"+self.nombre\
               +"\nedad:" + self.edad

    def listar(self):
        return self.cedula+ " " +self.nombre+ " "+self.edad

#PRUEBA
# obP = Persona("0925107054","Andres Avendaño","23")
# print(obP.getDatos())


class Empleado(Persona):
    def __init__(self,cedula,nombre,edad,sueldo):
        # Persona.__init__(self,cedula,nombre)
        super().__init__(cedula,nombre,edad)
        self.sueldo = sueldo

    def getDatos(self):
        # return "Cedula:" + self.cedula \
        #        + "\nNombre:" + self.nombre\
        #        + "\nMatricula:" + str(self.cod_mat)
            return super().getDatos() + " " + "\nSueldo:" + str(self.sueldo)

# obA= Empleado("AAAA","AAAA","23","200")
# print(obA.getDatos())


class Cliente(Persona):
    def __init__(self,cedula,nombre,edad,empresa,telefono):
        # Persona.__init__(self,cedula,nombre)
        super().__init__(cedula,nombre,edad)
        self.empresa = empresa
        self.telefono = telefono

    def getDatos(self):
        # return "Cedula:" + self.cedula \
        #        + "\nNombre:" + self.nombre\
        #        + "\nMatricula:" + str(self.cod_mat)
            return super().getDatos() + " " + "\nNombre empresa:" + str(self.empresa)\
                   + "\nTelefono:" + str(self.telefono)

    def listar(self):
        return super().listar()+" "+self.empresa+ " "+self.telefono



# obA= Cliente("AAAA","AAAA","23","BRUCOSA","0979428717")
# print(obA.getDatos())


class Usuarios:
    def __init__(self,usuario,clave):
        self.usuario = usuario
        self.clave = clave

    def getUsua(self):
            return self.usuario+"    "+self.clave

    def getUser(self):
            return self.usuario

    def getClave(self):
            return self.clave



# obL= Usuarios("Andres","XXX")
# print(obL.getUsua())