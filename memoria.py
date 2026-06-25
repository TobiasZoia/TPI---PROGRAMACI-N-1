from guardado import guardar_puntaje

def memoria():

    import random
    import time

    palabras = [
        "SOL", "CASA", "PERRO", "FLOR", "LUNA", "TOMATE",
        "JABON", "ELEFANTE", "TORTUGA", "CAMA", "SILLA",
        "CAMPERA", "CARGADOR", "SANDIA", "CELULAR", "ESPEJO",
        "GOMA", "CONEJO", "COMIDA", "AGUA", "TENEDOR",
        "AUTO", "PELOTA", "GATO", "MANZANA", "LIBRO",
        "COLECTIVO", "TERMO", "EQUIPO", "ANILLO", "PELICULA"
    ]

    mensajes = [
        "¡Excelente!",
        "¡Muy bien!",
        "¡Bravo!",
        "¡Genial!",
        "¡Sigue así!",
        "¡Fabuloso!",
        "¡Espléndido!",
        "¡Sorprendente!"
    ]

    def mostrar_menu():
        print("\n==============================")
        print("      JUEGO DE MEMORIA")
        print("==============================")
        print("1 - Jugar")
        print("0 - Salir (Puede hacerlo en cualquier momento)")

    def mostrar_palabras(lista):
        print("\nMemoriza las palabras:\n")

        for palabra in lista:
            print(palabra)

        time.sleep(5)
        print("\n" * 30)

    def hacer_pregunta(lista):

        correcta = random.choice(lista)

        incorrectas = []

        while len(incorrectas) < 2:
            palabra = random.choice(palabras)

            if palabra not in lista and palabra not in incorrectas:
                incorrectas.append(palabra)

        opciones = [correcta] + incorrectas
        random.shuffle(opciones)

        print("¿Cuál de estas palabras apareció?\n")

        print("1.", opciones[0])
        print("2.", opciones[1])
        print("3.", opciones[2])
        print("0. Volver al menú")

        respuesta = input("\nIngrese una opción (1-3): ")

        if respuesta == "0":
            return -1
        if respuesta == "1":
            elegida = opciones[0]
        elif respuesta == "2":
            elegida = opciones[1]
        elif respuesta == "3":
            elegida = opciones[2]
        else:
            return False
        return elegida == correcta

    opcion = ""
    while opcion != "0":
        try:
            mostrar_menu()
            opcion = input("\nSelecciona una opción: ")

            if opcion == "0":
                return -1
            elif opcion == "1":

                nombre = input("Ingrese su nombre: ")
                if nombre == "0":
                    return -1
                puntos = 0

                for ronda in range(1, 7):

                    print("\n==========")
                    print("RONDA", ronda)
                    print("==========")

                    seleccion = random.sample(palabras, 4)
                    mostrar_palabras(seleccion)
                    resultado = hacer_pregunta(seleccion)

                    if resultado == -1:
                        guardar_puntaje("puntaje_memoria.txt", nombre, puntos)
                        return puntos
                    if resultado:
                        print(random.choice(mensajes))
                        puntos += 10
                    else:
                        print("Respuesta incorrecta.")

                    print("Puntaje:", puntos)

                print("\n===================")
                print("Juego terminado")
                print("===================")
                print("Puntaje final:", puntos)

                guardar_puntaje("puntaje_memoria.txt", nombre, puntos)
                return puntos

            else:
                print("\nOpción incorrecta.")

        except ValueError:
            print("\nError: Debe ingresar un número.")