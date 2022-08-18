s='s'
cal=[]
cont=0
p=0
while s=='s' or s=='y' or s=='S' or s=='Y':
    cal1=float(input("Calificacion de alumno: "))
    cal.append(cal1)
    s=input("¿Continuar? ")
    if s=='n' or s=='N':
        for i in range(1,len(cal)+1):
            if cal[i-1]>4:
                cont+=1
                p+=cal[i-1]
        print (cont)
        print(i)
        print("Porcentaje de alumnos aprobados: ",(cont*100)/i)
        print("Promedio de los aprobados: ",p/cont)