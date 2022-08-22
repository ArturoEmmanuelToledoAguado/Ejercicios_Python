f= input("Cadena de caracteres:  ")
le=0
num=0 
mult=0
esp=0
for i in f:
    if i.isdigit():
        num+=1
        if int(i)%4==0:
            mult+=1
    elif i.isalpha():
        le+=1
    else:
        esp+=1
print("Cantida de letras: {}\nCantidad de especiales: {}\nCantidad de numeros: {}\nCantidad de multiplos de 4: {}".format(le,esp,num,mult))