cont=0
cont1=0
while True:
    cad=input("Cadena: ")
    cont1+=1
    for i in cad:
        if i.isdigit():
            cont+=1
    if cad == "*":
        print("Se leyeron {} lineas completas".format(cont1))
        break
    elif cad == "/":
        print ("Aparecen {} digitos en la linea".format(cont))
        cont=0
        cont1=0