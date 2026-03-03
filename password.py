#Variables

t_mayuscula = False
t_numero = False
t_c_especial = False
arroba = False

password = input("Ingrese su contraseña por favor: ")
correo = input("Ingrese su correo")

#Programa

for email in correo:
    if email == "@" and ".":
        arroba = True

while len (password) < 8:
    print("La contraseña debe tener minimo 8 carcateres")
    confirmar = input("SI desea intentarlo de nuevo escriba 'si':")
    if confirmar == "si":
        password = input("Ingrese nuevamente la constraseña:")
    else:
        print ("Usted no puede seguir ingresando la contraseña")
        break

for codigo in password:
    if codigo.isupper():
        t_mayuscula = True
    if codigo.isnumeric():
        t_numero = True
    if codigo.isalnum():
        t_c_especial = True

if t_mayuscula and t_numero and t_c_especial:
    print("Usted puede ingresar")
else:
    print("Su contraseña debe tener:")
    print("Minimo 8 caracteres")
    print("Minimo 1 mayúscula")
    print("Minimo 1 número")
    print("Minimo 1 carácter especial")