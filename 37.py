mul=0
while True:
    p=0
    im=0
    num=int(input("Numero (-1 para terminar el programa): "))
    if num == -1:
        break
    while num>0:
        aux=num%10
        if (aux%2)==0:
            p+=1
        elif (aux%3)==0 and (aux%2)!=0:
            mul+=1
            if(aux%2)!=0:
                im+=1
        elif(aux%2)!=0:
            im+=1
        num=num//10
    print("Pares: ",p,"\nImpares: ",im,"\nMultiplos de 3: ", mul)