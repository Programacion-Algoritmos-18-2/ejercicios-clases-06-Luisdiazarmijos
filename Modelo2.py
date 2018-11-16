import abc
class PersonaEquipo(metaclass=abc.ABCMeta):
    """
        se define la clases abstracta
    """
    __metaclass__ = abc.ABCMeta
    
    def __init__(self, nom):
        self.nombre = nom

    @abc.abstractmethod
    def entrenar():
        pass



class Entrenador(PersonaEquipo):
    

    def __init__(self,n):
        #Heredamos los atributos de la clase padre
        super(Entrenador, self).__init__(n)
        self.codigo_entrenado =""
        #Presentamos 
    def entrenar(self):
        print("Yo %s  entrenador, soy el director del entrenamiento" % \
                self.nombre)

class Futbolista(PersonaEquipo):
    

    def __init__(self, n):

        super(Futbolista, self).__init__(n)

    def entrenar(self):
        print("Yo %s futbolista, hago practica en el  entrenamiento" % \
                self.nombre)

class MedicoEquipo(PersonaEquipo):
    def __init__(self,n):
        super(MedicoEquipo,self).__init__(n)
        self.titulo =""
    def agregar_titulo(self, titulo):
        self.titulo=titulo
    def entrenar(self):
        print("Yo %s medico, atiendo a los jugadores en el entrenamiento."% self.nombre)
        
class PresidenteEquipo(PersonaEquipo):
    def __init__(self,n):
        super(PresidenteEquipo,self).__init__(n)
        self.numero_propiedades=""
    def agregar_numero_propiedades(self,np):
        self.numero_propiedades=np
    def obtener_numero_propiedades(self):
        return numero_propiedades
    def entrenar(self):
        print("Yo %s presidente, pongo el dinero para el entrenamiento."% self.nombre)
