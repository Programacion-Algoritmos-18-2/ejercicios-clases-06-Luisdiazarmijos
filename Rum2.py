from Modelo2 import *
#p=PersonaEquipo("Luis")
f=Futbolista("Antonio")


m=MedicoEquipo("Ramon")


p=PresidenteEquipo("Francisco")


e=Entrenador("Jose")


lista=[f, m, p, e]
for l in lista:
    l.entrenar()