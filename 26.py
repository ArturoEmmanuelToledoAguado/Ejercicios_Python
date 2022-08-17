pal=input("Ingrese una frase: ")
pal=pal.lower()
cont=0
for i in range(len(pal)):
    if pal[i] =='a' or pal[i] =='e' or pal[i] =='i' or pal[i] =='o' or pal[i]=='u':
        cont=cont+1
print(cont)