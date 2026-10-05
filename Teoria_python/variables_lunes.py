# Variables, asignación (=) y tipos (int, float, str...) 

saldo_total = 254.55  # float si es un numero con demcimales, si es entero es int
email = 'ana@local.com'  # str
print( "saldo_total")
print( saldo_total ) #al no tener comillas se imprime el valor que se guarda en la variable
    # print(email)   # error indentación

# Tipos
print("tipo de email: ", type(email)  )
print("tipo de saldo_total: ", type(saldo_total)  )
edad = 43
print("Tipo de edad", type(edad))
# Variables pueden cambiar de tipo (mejor no hacerlo ya que representas dos cosas en un dato, no es correcto)
email = 4
print( "Tipo email: ", type(email)  )

# print("El email es ", email, " y el saldo es \n", saldo_total, "\n")