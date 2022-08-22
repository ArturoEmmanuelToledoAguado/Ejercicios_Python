def esPar(num):
    return True if num%2==0 else False

def sumatoriaDigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s

c=0
while True:
    a =int(input("Escribi un numero: "))
    if sumatoriaDigitos(a)%5==0 or sumatoriaDigitos(a)>1000:
        break
    elif esPar(a)==False:
        c+=1
print(c)