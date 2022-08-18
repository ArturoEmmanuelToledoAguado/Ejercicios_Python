i=True
s=0
while i==True:
    n=float(input("Monto de una venta: $"))
    if n<0:
        print("Monto no valido")
    else:
        s=s+n
        if n==0:
            if s>1000:
                s=s-(s/10)
            i=False
            print("Monto total a pagar: $",s)