a=True
s=[]
cont=0
r=0
while a==True:
    s1=input("Escibe un caracter: ")
    s.append(s1)
    if len(s1)>=2 or s1=='0':
        s.remove(s1)
        for i in range(1,len(s)+1):
            if s[i-1]=='a':
                cont+=1
            r=i
        s="".join(s)
        a=False
print("El string completo es: ",s)
print("Porcentaje de letras 'a': ", (cont*100)/r)