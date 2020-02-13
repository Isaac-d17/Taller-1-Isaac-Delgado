codigo= input("Introduzca el codigo del articulo:\n")
descripcion= input("Introduzca la descripcion del articulo:\n")
pa= int(input("Introduzca el precio del articulo:\n"))
pc= int(pa*30/100)+pa
print("Bienvenido el articulo :", descripcion,"\nCon codigo de:", codigo,"\nEl precio es del costo es de:", pc,)