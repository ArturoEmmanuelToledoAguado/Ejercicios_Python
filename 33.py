i=True
n1=[]
while i==True:
    n=int(input("Número: "))
    n1.append(n)
    if n==0:
        print("Mayor numero ingresado: ",max(n1))
        i=False
    