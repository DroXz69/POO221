#Salida de datos
print("Escribe tu Nombre")
#Entrada de datos
mivariable = input()
#Salida de datos
print("Tu Nombre es: "+mivariable)
#Entrada
edad = int(input("Escribe tu edad: "))
#Salida
print("Tu edad es: "+str(edad))
#Proceso
edad = int(edad) +1
edad += 1 #Equivalente al anterior
print("En 2 años mas, tendras: "+str(edad))
#Se puede usar muchos IF, pero es ineficiente
if(edad>18):
    print("Es mayor de edad")
if(edad==18):
    print("Cumplio la mayoria de edad")
if(edad<18):
    print("Es menor de edad")
#Otra alternativa
if(edad<18):
    print("Es Mayor de edad")
    if(edad>65):
        print("Es Adulto Mayor")
else:
    if(edad<5):
        print("Es Infante")
    print("Es menor de edad")
print("Fin del Programa")

i=0
while(i<10):
    print("ciclo")
    i=i+1 # i += 1 es equivalente