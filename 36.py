s=0
nE=int(input("Escribe un numero: "))
while nE!=0:
    eN=nE%10
    nE//=10
    s+=eN
print("Suma de los digitos: ",s)