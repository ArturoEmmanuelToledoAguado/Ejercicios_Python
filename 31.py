f=input("Frase: ")
f1=[]
f2=[]
i=len(f)
while i>0:
    f1+=f[i-1]
    i-=1
    f2="".join(f1)
print(f2)