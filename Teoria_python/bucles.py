#En el bucle siguiente decimos que para i, que toma el primer lugar tome la variable
for i in range(5):  
    print (i+1)
#En este caso decimos que para la variable nos de un rango de cinco valores, y el print es para que nos ensene la ecuacion que le ponemos; es decir en este caso en vez de empezar en el 0 pues empezaria por el 1 ya que 0+1 es 1 y asi hasta ocupar 5 posiciones.

for i in range(5):  
    print (f"{i} ", end="misisipi")
#Con esto le decimos que para la funcion i imprima misisipi despues de cada salida dentro del rango

#Suma numeros
suma = 0 #Acumulador 
ini = int (input("inicio: "))
fin = int (input("fin: "))
#Definimos las variables

for i in range(ini, fin+1):
    print(i)
    suma = suma + i
print("\nSuma:",suma)

# #while
numero = int(input("Introduce un numero(0 para terminar):"))

while numero != 0: #A la que se encuentre un 0 cierra el programa.
    print ("Has introducido:", numero)
    numero = numero = int(input("Introduce un numero(0 para terminar):"))

print ("Fin del programa")

