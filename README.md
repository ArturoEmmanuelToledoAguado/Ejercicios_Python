#Sección 1
###Entrada/salida de datos - Variables - Tipos de datos 
1. Escribí un programa que solicite al usuario que ingrese su nombre. El nombre se debe almacenar en una variable llamada nombre. A continuación se debe mostrar en pantalla el texto “Ahora estás en la matrix, [usuario]”, donde “[usuario]” se reemplazará por el nombre que el usuario haya ingresado.
2. Escribí un programa que solicite al usuario ingresar un número con decimales y almacenalo en una variable. A continuación, el programa debe solicitar al usuario que ingrese un número entero y guardarlo en otra variable. En una tercera variable se deberá guardar el resultado de la suma de los dos números ingresados por el usuario. Por último, se debe mostrar en pantalla el texto “El resultado de la suma es [suma]”, donde “[suma]” se reemplazará por el resultado de la operación.
3. Escribí un programa que solicite al usuario dos números y los almacene en dos variables. En otra variable, almacená el resultado de la suma de esos dos números y luego mostrá ese resultado en pantalla.
A continuación, el programa debe solicitar al usuario que ingrese un tercer número, el cual se debe almacenar en una nueva variable. Por último, mostrá en pantalla el resultado de la multiplicación de este nuevo número por el resultado de la suma anterior.
4. Escribí un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.
5. Escribí un programa que solicite al usuario el ingreso de una temperatura en escala Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius. La fórmula de conversión que se usa para este cálculo es: _Celsius = (5/9) * (Fahrenheit-32)_
6. Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.
7. Escribí un programa que solicite al usuario un número y le reste el 15%, almacenando todo en una única variable. A continuación, mostrar el resultado final en pantalla.
8. Escribí un programa que solicite al usuario el ingreso de dos palabras, las cuales se guardarán en dos variables distintas. A continuación, almacená en una variable la concatenación de la primera palabra, más un espacio, más la segunda palabra. Mostrá este resultado en pantalla.
9. Escribí un programa que solicite al usuario el ingreso de un texto y almacene ese texto en una variable. A continuación, mostrar en pantalla la primera letra del texto ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la cantidad de caracteres que tiene el texto que ingresó (por ejemplo, si escribió la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y almacenar este número en una variable llamada indice.
Mostrar en pantalla el carácter del texto ubicado en la posición dada por indice.
10. Escribí un programa que solicite al usuario que ingrese cuántos shows musicales ha visto en el último año y almacene ese número en una variable. A continuación mostrar en pantalla un valor de verdad (True o False) que indique si el usuario ha visto más de 3 shows.
~~~
shows=int(input("Cuantos Shows musicales ha visto en el ultimo año: "))
print("",(shows>3))
~~~
11. Escribí un programa que le solicite al usuario ingresar una fecha formada por 8 números, donde los primeros dos representan el día, los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con tipo int (número entero). Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.
~~~
Fecha=input("Ingrese la fecha formada por 8 numeros en el formato DDMMAAAA: ")
print(Fecha[0]+""+Fecha[1]+"/"+Fecha[2]+""+Fecha[3]+"/"+Fecha[4]+""+Fecha[5]+""+Fecha[6]+""+Fecha[7])
~~~
12. Escribí un programa para solicitar al usuario el ingreso de un número entero y que luego imprima un valor de verdad dependiendo de si el número es par o no. Recordar que un número es par si el resto, al dividirlo por 2, es 0.
~~~
num=int(input("Ingrese un numero entero: "))
print("",(num%2)==0)
~~~
13. Escribí un programa que le solicite al usuario su edad y la guarde en una variable. Que luego solicite la cantidad de artículos comprados en una tienda y la guarde en otra variable. Finalmente, mostrar en pantalla un valor de verdad (True o False) que indique si el usuario es mayor de 18 años de edad y además compró más de 1 artículo.
~~~
Edad=int(input("Ingrese su edad: "))
Art=int(input("Ingrese la cantidad de articulos comprados: "))
print("Tu edad: ",Edad)
print("Articulos comprados: ",Art)
print((Edad>=18 and Art>1))
~~~
14. Escribí un programa que, dada una cadena de texto por el usuario, imprima True si la cantidad de caracteres en la cadena es un número impar, o False si no lo es.
~~~
Cadena=input("Ingrese un texto\n")
print(((len(Cadena))%2)==0)
~~~
15. Escribí un programa que le pida al usuario ingresar dos palabras y las guarde en dos variables, y que luego imprima True si la primera palabra es menor que la segunda o False si no lo es.
~~~
p1=input("Una palabra: ")
p2=input("Otra palabra: ")
print((p1<p2))
~~~
16. Escribí un programa para pedir al usuario su nombre y luego el nombre de otra persona, almacenando cada nombre en una variable. Luego mostrar en pantalla un valor de verdad que indique si: los nombres de ambas personas comienzan con la misma letra ó si terminan con la misma letra. Por ejemplo, si los nombres ingresados son María y Marcos, se mostrará True, ya que ambos comienzan con la misma letra. Si los nombres son Ricardo y Gonzalo se mostrará True, ya que ambos terminan con la misma letra. Si los nombres son Florencia y Lautaro se mostrará False, ya que no coinciden ni la primera ni la última letra.
~~~
n1=input("Tu nombre: ")
n2=input("Otro nombre: ")
print((n1[0]==n2[0])or(n1[len(n1)-1]==n2[len(n2)-1]))
~~~
#Sección 2
###Bloques - Selección - Repeticiones
17. Escribí un programa que, dado un número entero, muestre su valor absoluto. Recordá que, para los números positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).
~~~
num=float(input("Numero: "))
if num<0:
    print("Valor absoluto: ",num*-1)
else:
    print("Valor absoluto: ",num)
~~~
18. Escribí un programa que solicite al usuario el ingreso de dos números diferentes y muestre en pantalla al mayor de los dos.
~~~
num=float(input("Ingrese un numero: "))
num2=float(input("Otro numero distinto: "))
if num<num2:
    print(num2,"es mayor")
else:
    print(num, "es mayor")
~~~
19. Escribí un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “Es vocal”. Verificar si el usuario ingresó un string de más de un carácter y, en ese caso, informarle que no se puede procesar el dato.
~~~
vocal=input("Letra: ")
vocal =vocal.lower()
if len(vocal)>1:
    print("No se puede procesar el dato.")
elif (vocal=='a'or vocal=='e' or vocal=='i'or vocal=='o' or vocal=='u'):
    print("Es vocal")
~~~
20. Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
~~~
a=float(input("Primer numero: "))
b=float(input("Segundo numero: "))
c=float(input("Tercer numero: "))
if a<b and a<c:
    print(a)
elif b<a and b<c:
    print(b)
else:
    print(c)
~~~
21. Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
~~~
nombre=input("Nombre de usuario: ")
password=input("Contraseña: ")
if nombre=="Gwenevere" and password=="excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")
~~~
22. Escribí un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
~~~
a=int(input("Año: "))
if a%4==0 and (a%100!=0 or a%400==0):
    print("Bisiesto")
else:
    print("No bisiesto")
~~~
23. Escribí un programa que le solicite al usuario un número entero y muestre todos los números correlativos entre el 1 y el número ingresado por el usuario.
~~~
a=int(input("Ingresá un número entero: "))
for i in range(1,a+1):
    print(i)
~~~
24. Escribí un programa que muestre la sumatoria de todos los números entre el 0 y el 100.
~~~
n=int(input("Ingrese un numero: "))
print("Sumatoria ",(n*(n+1))/2)
~~~
25. Escribí un programa que, dado un número por el usuario, muestre todos sus divisores positivos. Recordá que un divisor es aquel que divide al número de forma exacta (con resto 0).
~~~
n=int(input("Ingrese un número: "))
div=[]
for i in range(1,n+1):
    if n%i==0:
        div.append(i)
print(div)
~~~
26. Escribí un programa que, dada una frase por el usuario, muestre la cantidad total de vocales (tanto mayúsculas como minúsculas) que contiene.
~~~
pal=input("Ingrese una frase: ")
pal=pal.lower()
cont=0
for i in range(len(pal)):
    if pal[i] =='a' or pal[i] =='e' or pal[i] =='i' or pal[i] =='o' or pal[i]=='u':
        cont=cont+1
print(cont)
~~~
27. Escribí un programa que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y, a partir de éstos, cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…
~~~
n=int(input("Ingrese un numero: "))
fib= [1, 1]
for i in range(2,n):
    n=fib[i-1]+fib[i-2]
    fib.append(n)
print(fib)
~~~
28. Escribí un programa que, dado un número entero positivo, calcule y muestre su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.
~~~
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
~~~
29. Escribí un programa que permita al usuario ingresar 6 números enteros, que pueden ser positivos o negativos. Al finalizar, mostrar la sumatoria de los números negativos y el promedio de los positivos. No olvides que no es posible dividir por cero, por lo que es necesario evitar que el programa arroje un error si no se ingresaron números positivos.
~~~
n=[]
print("Ingrese 6 numeros enteros: ")
i=0
s=0
s1=0
cont=0
while i<6:
    n1=int(input("Número: "))
    n.append(n1)
    if n[i]<0:
        s+=n[i]
    else:
        cont+=1
        s1+=n[i]
    i+=1
print("Sumatoria de los negativos: ",s)
print("Promedio de los positivos: ",s1/cont)
~~~
30. Escribí un programa que permita al usuario ingresar una frase y luego un carácter (string de longitud 1) y luego muestre la frase ingresada, pero con todas las ocurrencias del carácter indicado por el usuario reemplazadas por “*”.
~~~
f=input("Frase: ")
f1=list(f)
c=input("Caracter: ")
for i in range(len(f1)):
    if f1[i]==c[0]:
        f1[i]="*"
        f="".join(f1)
print(f)
~~~
31. Escribí un programa que, dada una frase por el usuario, la muestre invertida, sin utilizar una rebanada con paso negativo.
~~~
f=input("Frase: ")
f1=[]
f2=[]
i=len(f)
while i>0:
    f1+=f[i-1]
    i-=1
    f2="".join(f1)
print(f2)
~~~
32. Escribí un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el monto total de 1000, se le debe aplicar un 10% de descuento.
~~~
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
~~~
33. Escribí un programa que permita al usuario ingresar una cantidad de números positivos indefinida (la cantidad que ingresará no se conoce y puede cambiar en cada ejecución), finalizando cuando ingresa el número 0 (que no se tendrá en cuenta). Una vez terminada la lectura de números, informar cuál fue el mayor de los números ingresados.
~~~
i=True
n1=[]
while i==True:
    n=int(input("Número: "))
    n1.append(n)
    if n==0:
        print("Mayor numero ingresado: ",max(n1))
        i=False
~~~
34. Escribí un programa que pregunte al usuario si desea analizar calificaciones de alumnos y, sólo si responde “S” comenzará el procesamiento de los datos, hasta que el usuario ingrese algo diferente de “S”. Por cada alumno, permitir ingresar su calificación. Si es mayor a 4 el alumno está aprobado. Finalmente, mostrar “Porcentaje de alumnos aprobados: x %” (donde x es el porcentaje de aprobados sobre el total de calificaciones procesadas). También se debe imprimir “Promedio de los aprobados: y” (donde y es la calificación promedio, sólo de los alumnos aprobados).
~~~
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
~~~
35. Escribí un programa que solicite al usuario el ingreso de strings de longitud 1 (un solo carácter), uno por vez. La repetición finalizará cuando se ingrese un string que no tenga longitud 1, o cuando el string ingresado corresponda al dígito numérico 0. Al finalizar, mostrar el string completo que se formó con todos los caracteres ingresados y qué porcentaje de caracteres del total fueron la letra “a”.
~~~
a=True
s=[]
cont=0
r=0
while a==True:
    s1=input("Escibe un caracter: ")
    s.append(s1)
    if len(s1)>=2 or s1=='0':
        s.remove(s1)
        for i in range(1,len(s)+1):
            if s[i-1]=='a':
                cont+=1
            r=i
        s="".join(s)
        a=False
print("El string completo es: ",s)
print("Porcentaje de letras 'a': ", (cont*100)/r)
~~~
36. Escribí un programa que, dado un número entero por el usuario (guardado como int), muestre la suma de todos sus dígitos. Recordá que vas a necesitar obtener cada uno de los dígitos por separado para poder sumarlos entre sí.
~~~
s=0
nE=int(input("Escribe un numero: "))
while nE!=0:
    eN=nE%10
    nE//=10
    s+=eN
print("Suma de los digitos: ",s)
~~~
37. Escribí un programa para solicitar al usuario que ingrese números enteros positivos (la cantidad que ingresará no se conoce y la decide el usuario). La lectura de números finalizará cuando el usuario ingrese el número -1. Por cada número ingresado, mostrar la cantidad de dígitos pares y la cantidad de dígitos impares que tiene. Al finalizar, mostrar cuántos números múltiplos de 3 ingresó el usuario.
~~~
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
~~~
38. Escribí un programa que solicite al usuario una cadena de caracteres (que puede contener letras, números o símbolos). Analizar la cadena para mostrar: cuántas letras del abecedario (minúsculas y mayúsculas) contiene, cuántos símbolos (caracteres que no son ni letras ni números), cuántos dígitos numéricos y, de los dígitos, cuántos son múltiplos de 4.
~~~
f= input("Cadena de caracteres:  ")
le=0
num=0 
mult=0
esp=0
for i in f:
    if i.isdigit():
        num+=1
        if int(i)%4==0:
            mult+=1
    elif i.isalpha():
        le+=1
    else:
        esp+=1
print("Cantida de letras: {}\nCantidad de especiales: {}\nCantidad de numeros: {}\nCantidad de multiplos de 4: {}".format(le,esp,num,mult))
~~~
39. Escribí un programa que permita al usuario ingresar números que serán leídos como string (no como int o float) hasta que ingrese uno que sea múltiplo de 10 ó menor que 0 (que no será procesado). Se formarán dos strings, en los cuales se concatenarán los números ingresados, según el siguiente criterio: en un string se concatenarán todos los números que el usuario ingrese cuya cantidad de dígitos sea un múltiplo de 3. En el otro, se concatenarán todos los números que contengan el dígito 0. Si un número cumple ambas condiciones, debe concatenarse en ambos strings. En cada string, después de cada número concatenado debe colocarse el carácter “-”. Al finalizar, mostrar en pantalla ambos strings.
~~~
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
~~~
40. Escribí un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse
~~~
cont=0
cont1=0
while True:
    cad=input("Cadena: ")
    cont1+=1
    for i in cad:
        if i.isdigit():
            cont+=1
    if cad == "*":
        print("Se leyeron {} lineas completas".format(cont1))
        break
    elif cad == "/":
        print ("Aparecen {} digitos en la linea".format(cont))
        cont=0
        cont1=0
~~~
#Sección 3
###Funciones 
41. Escribí una función llamada esPar que reciba como parámetro un número y retorne True si el número es par ó False si es impar. Utilizar esta función en un programa que solicite al usuario el ingreso de 10 números y que luego muestre, por separado, la suma de todos los pares y la suma de todos los impares.
~~~
def esPar(num):
    return True if num%2==0 else False

i=0
par=0
im=0
while i<10:
    a=float(input("Numero: "))
    if esPar(a) == True:
        par+=a
    else:
        im+=a
    i+=1
print("Suma de los pares: {}\nSuma de los impares: {}".format(par,im))
~~~
42. Escribí una función llamada sumatoriaDigitos que reciba como parámetro un número y retorne la suma de todos sus dígitos, reutilizando la estrategia utilizada en el ejercicio 36. Finalmente, escribir un algoritmo que solicite al usuario ingresar varios números hasta que ingrese el número 100, con el cual cortará la repetición. Por cada número, mostrar la suma de sus dígitos, para lo cual se llamará a la función sumatoriaDigitos.
~~~
def sumatoriaDigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s

a=0
while a!=100:
    a = int(input("Escribi un numero: "))
    if a==100:
        break
    else:
        print("Suma de los digitos: ",sumatoriaDigitos(a))
~~~
43. Escribí un programa que permita al usuario ingresar números enteros. La repetición terminará cuando el usuario ingrese un número para el cual la suma de sus dígitos sea mayor que 1000 ó múltiplo de 5. Finalmente, mostrar cuántos números impares ingresó el usuario antes de cortar la repetición. Reutilizar las funciones esPar y sumatoriaDigitos implementadas en los ejercicios anteriores.
~~~
def esPar(num):
    return True if num%2==0 else False

def sumatoriaDigitos(num):
    s=0
    while num>0:
        s=s+num%10
        num=num//10
    return s

c=0
while True:
    a =int(input("Escribi un numero: "))
    if sumatoriaDigitos(a)%5==0 or sumatoriaDigitos(a)>1000:
        break
    elif esPar(a)==False:
        c+=1
print(c)
~~~
44. Escribí una función que reciba un string y retorne True si es un palíndromo (esto es, si se lee igual de izquierda a derecha o de derecha a izquierda), False en caso contrario. Utilizar esta función en un programa que permita al usuario ingresar palabras hasta que ingrese la palabra “fin” (suponer que todas las palabras son en minúsculas o todas en mayúsculas, de forma consistente). Al finalizar, mostrar la cantidad de palíndromos ingresados.
~~~
def palindromo(pal):
    return (True if pal==pal[::-1] else False)

p=""
cant=0
while p!='fin':
    p=input("Cadena: ")
    if palindromo(p)== True:
        cant+=1
print("Cantidad de Palindromos: ",cant)
~~~
45. Escribí un programa que permita al usuario ingresar números enteros hasta que ingrese uno cuyo dígito inicial sea el 9 (el cual no se procesará). Una vez terminada la repetición, mostrar cuántos de los números que el usuario ingresó tienen sólo dos divisores (para esto es posible reutilizar parte de la estrategia elaborada en el ejercicio 25).
~~~
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
~~~