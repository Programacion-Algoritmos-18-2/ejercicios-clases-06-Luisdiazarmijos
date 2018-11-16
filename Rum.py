from  Modelo import * 
persona = PersonaEquipo()
persona.agregar_nombre("Ana")
persona.entrenar()

f=Futbolista()
f.agregar_nombre=("Marco")
f.entrenar()

e=Entrenador()
e.entrenar()
lista =(persona, f, e)
for l in lista:
    l.entrenar()	
