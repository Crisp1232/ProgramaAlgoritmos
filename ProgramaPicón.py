'''
En este programa se realizan tres tipos de ejercicios, en el primero se realizan
operaciones matemáticas básicas, en el segundo realizamos el conteo de la longitud del nombre
y en el tercero cambiamos el tipo de variable
'''
print("+++++++++++++++++++++++++++++++++++++++")
print("\nOperaciones básicas")
#Suma
a = 10 #Variable
b = 15 #Variable

print("\nSuma es igual a:", (a+b)) #Suma de variables usando print

#Resta
c = 23.932 #Variable
d = 14.234 #Variable

print("Resta es igual a:", c-d) #Resta de variables usando print

#Multiplicación

e = 54 #Variable
f = 24 #Variable

print("Multiplicación es igual a:",e*f) #Multiplicación de variables usando print
#División
g = 94.564 #Variable
h = 22.756 #Variable

print("División es igual a:",g/h) #División de variables usando print

print("\n++++++++++++++++++++++++++++++++++++++++")
print("\nEn este programa se hacen operaciones básicas como suma, resta multiplicacion y división"
      " de números enteros y flotantes, almacenandolos en variables")
print("+++++++++++++++++++++++++++++++++++++++++++")

#NOMBRE Y LONGITUD
nombre = "Christopher Santiago Picón Illescas" #Define el nombre con una variable
longitud = len(nombre) #Con la función len, cuento los caracteres de la variable nombre

print("\nCaracteres")
print("\nMi nombre es:",nombre,"\nla longitud es:", longitud)

print("\nEn este programa se guarda en una variable mi nombre y de ahi usando la función len se cuenta el número de caracteres y de ahi los imprime")
print("++++++++++++++++++++++++++++++++++++++++")
print("\nConversión de datos")

#Conversión de datos
uno = 34 #Variable entera
dos = 29.456 #Variable flotante

print("\nTipo del dato original :",type(uno)) #Imprime el tipo de dato
print("Tipo de dato original 2 : ",type(dos)) #Imprime el tipo de dato de la variable 2

convertido = float(uno) #Cambiamos el tipo de variable de entero a flotante
convertido2 = int(dos) #Cambiamos el tipo de variable de flotante a entero

print("++++++++++++++++++++++++++++++++++++++++")

print("Tipo del dato convertido : ", type(convertido)) #Imprime el tipo de dato convertido
print("Tipo de dato convertido 2 :", type(convertido2)) #Imprime el tipo de dato convertido 2
