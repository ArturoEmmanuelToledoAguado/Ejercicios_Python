f=input("Frase: ")
f1=list(f)
c=input("Caracter: ")
for i in range(len(f1)):
    if f1[i]==c[0]:
        f1[i]="*"
        f="".join(f1)
print(f)