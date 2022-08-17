a=int(input("Año: "))
if a%4==0 and (a%100!=0 or a%400==0):
    print("Bisiesto")
else:
    print("No bisiesto")