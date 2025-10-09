#Ejemplo 1

# Variable global
mensaje = "Hola desde fuera"

def funcion_principal():
    # Variable local
    saludo = "Hola desde dentro"

    def funcion_interna():
        # Variable no local
        nonlocal saludo
        saludo = "Modificado desde función interna"
        print("Dentro de interna:", saludo)

    funcion_interna()
    print("Dentro de principal:", saludo)

funcion_principal()
print("Fuera de todo:", mensaje)


####################################################################################

#Ejemplo 2

# Variable global
mensaje_global = "Hola desde el ámbito global"

def funcion_externa():
    mensaje_local = "Hola desde el ámbito local"

    def funcion_interna():
        nonlocal mensaje_local  # Accede a la variable de la función externa
        global mensaje_global   # Accede a la variable global

        mensaje_local = "Modificado desde función interna"
        mensaje_global = "Modificado desde función interna también"

        print("Dentro de funcion_interna:")
        print("mensaje_local:", mensaje_local)
        print("mensaje_global:", mensaje_global)

    funcion_interna()

    print("Dentro de funcion_externa:")
    print("mensaje_local:", mensaje_local)

funcion_externa()

print("Fuera de todas las funciones:")
print("mensaje_global:", mensaje_global)
