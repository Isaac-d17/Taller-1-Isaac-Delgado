nombre= input("Introduzca el nombre del Cliente:\n")
apellido= input("Introduzca el apellido:\n")
monto= int(input("Introduzca el monto a Cliente:\n"))
pt= int(monto*7/100)+monto
print("Su nombre es:",nombre, apellido,"\nSu monto Total a pagar es de:",pt,"de dolares")