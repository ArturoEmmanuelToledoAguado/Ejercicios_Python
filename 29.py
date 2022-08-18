n=[]
print("Ingrese 6 numeros enteros: ")
i=0
s=0
s1=0
cont=0
while i<6:
    n1=int(input("Número: "))
    n.append(n1)
    if n[i]<0:
        s+=n[i]
    else:
        cont+=1
        s1+=n[i]
    i+=1
print("Sumatoria de los negativos: ",s)
print("Promedio de los positivos: ",s1/cont)