#e02.py

# Partiendo de:

# frase = "Python es divertido"
frase = "Python es divertido"
buscar = "Python"
# haz que el programa:

#     Muestre la frase en minúsculas.
print("frase en minusculas:", frase.lower())

#     Muestre su longitud.
print("Nº de letras:", len(frase))

#     Compruebe si contiene la palabra "python" sin distinguir mayúsculas y minúsculas.
if buscar.lower() in frase.lower():
    print("¡¡Sí está!!")
else:
    print("No está")

#     Muestre la frase al revés.

print(frase[::-1])

