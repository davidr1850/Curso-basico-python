# Declaramos una variable
calificacion = input("Introduce tu calificacion a la AZ-900: ")

calificacion =int(calificacion)    # Preguntamos si la calificacion es menor a 700
if calificacion < 700 :
    print("Vees, por no estudiar") # si es menor a 700, muestra esto
elif calificacion > 1000 :
    print("MIENTEEES!!!! no puedes sacar mas de mil")
else : # Si no se cumple el if anterior, pasa a esta linea
    print("Felicidades, pasa por tu certificado") # Se ejecuta si ninguno de lo if se cumple

# Verificddor de mayoria de edad
edad = input("Introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad <= 100 :
    print("Biemvenido al mamitas")
elif edad > 100 :
    print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0 :
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")

# En Python NO HAY SWTICH CASE
