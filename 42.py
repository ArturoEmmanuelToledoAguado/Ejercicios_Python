def sumatoriaDigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s

a=0
while a!=100:
    a = int(input("Escribi un numero: "))
    if a==100:
        break
    else:
        print("Suma de los digitos: ",sumatoriaDigitos(a))