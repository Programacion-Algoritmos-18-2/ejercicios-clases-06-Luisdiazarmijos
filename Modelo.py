
class PersonaEquipo(object):
 
    def __init__(self):
        self.nombre = " "

    def agregar_nombre(self, nombre):
    	self.nombre=nombre
    def obtener_nombre(self):
    	return self.nombre                 
    	
    def entrenar(self):
    	print("Entreno")
    	

class Futbolista(PersonaEquipo):

    def __init__(self):
        super(Futbolista, self).__init__()
        self.posicion_campo=""
    def posicion_campo(self,pc):
    	self.posicion_campo=pc
    def obtener_posicion_campo(self):
    	return self.posicion_campo
    	
    def entrenar(self):
        print(" Hago practica en el  entrenamiento")
                


class Entrenador(PersonaEquipo):

    def __init__(self):
        super(Entrenador, self).__init__()
        self.codigo_entrenador=""
    def agregar_codigo_entrenador(self,ce):
        self.codigo_entrenador=ce
    def obtener_codigo_entrenador(self):
    	return codigo_entrenador