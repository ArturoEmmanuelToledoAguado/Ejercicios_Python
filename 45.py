def divisores(num):
    div=[]
    for i in range(1,num+1):
        if num%i==0:
            div.append(i)
    return div

def inicioNueve(num):
    while num>10:
        num=num//10
    return num

cant=0
while True:
    a=int(input("Numero entero: "))
    if inicioNueve(a)==9:
        break
    elif len(divisores(a))==2:
        cant+=1
print("La cantidad de numeros primos que se ingresaron fueron: ",cant)