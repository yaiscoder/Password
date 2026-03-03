# Variables
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
c_especial = "_$@*!"

t_mayuscula = False
t_numero = False
t_c_especial = False

#Programa

password = input("Ingrese su contraseña por favor: ")

while len (password) < 8:
    print("La contraseña debe tener minimo 8 carcateres")
    confirmar = input("SI desea intentarlo de nuevo escriba 'si':")
    if confirmar == "si":
        password = input("Ingrese nuevamente la constraseña:")
    else:
        print ("Usted no puede seguir ingresando la contraseña")
        break

for codigo in password:
    if codigo in mayusculas:
        t_mayuscula = True
    if codigo in numeros:
        t_numero = True
    if codigo in c_especial:
        t_c_especial = True

if t_mayuscula and t_numero and t_c_especial:
    print("Usted puede ingresar")
else:
    print("Su contraseña debe tener:")
    print("Minimo 8 caracteres")
    print("1 mayúscula")
    print("1 número")
    print("1 carácter especial")