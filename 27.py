n=int(input("Ingrese un numero: "))
fib= [1, 1]
for i in range(2,n):
    n=fib[i-1]+fib[i-2]
    fib.append(n)
print(fib)