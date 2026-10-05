# lógica o booleana
autorizado = True    # el otro valor posible True
print( type(autorizado)  )

# if autorizado==True:  # autorizado==True <=> autorizado 
#     print("Puede pasar")
#     print("segundo")
# else:
#     print("No puede pasar")

# con un = confirmamos con == comparamos

edad = input ("Edad:  ")

print(edad,type(edad))
edad = float(edad) #Con esto cambiamos la condicion, es decir decimos que la edad va a ser igual a float no a lo que estaba que era str
print (edad, type(edad))

if 21 < edad <25:  # esto se puede poner por ser python. En otros lenguajes se pondria 21< edad and edad<25 
    print("Tienes entre 21 y 25")
else:
    print("No estas en el rango de edad requerido")

print (edad + 1)
print (edad *3)

saldo = 10000
edad = 16

if (edad > 18 or saldo > 50000):
    print("Puede apostar")