vocal=input("Letra: ")
vocal =vocal.lower()
if len(vocal)>1:
    print("No se puede procesar el dato.")
elif (vocal=='a'or vocal=='e' or vocal=='i'or vocal=='o' or vocal=='u'):
    print("Es vocal")