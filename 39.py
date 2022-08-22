c_mult=""
c_cero=""
while True:
    c_num = input("Numero: ")
    if int(c_num)<0 or int(c_num)%10==0:
        break
    elif len(c_num)%3==0:
        c_mult = c_mult +c_num+"-"
        if '0' in c_num:
            c_cero = c_cero+c_num+"-"
    elif '0' in c_num:
        c_cero = c_cero+c_num+"-"
    else:
        pass
    print("Numeros cuya cantidad de digitos es multiplo de 3: ",c_mult)
    print("Numeros que contienen el 0: ",c_cero)