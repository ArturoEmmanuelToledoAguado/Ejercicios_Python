def palindromo(pal):
    return (True if pal==pal[::-1] else False)

p=""
cant=0
while p!='fin':
    p=input("Cadena: ")
    if palindromo(p)== True:
        cant+=1
print("Cantidad de Palindromos: ",cant)