n=int(input("Numero: "))
r=1
if n==1:
    print("Factorial: 0")
elif n<=0:
    print("No existen factoriales negativos ")
else:
    while n>1:
        r*=n
        n-=1
    print("Factorial: ",r)