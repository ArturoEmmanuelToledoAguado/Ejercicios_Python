def esPar(num):
    return True if num%2==0 else False

i=0
par=0
im=0
while i<10:
    a=float(input("Numero: "))
    if esPar(a) == True:
        par+=a
    else:
        im+=a
    i+=1
print("Suma de los pares: {}\nSuma de los impares: {}".format(par,im))