#Hecho con IA porque no sabia como hacer para que aparezcan palabras al azar y para que en un cierto tiempo determinado desaparezca
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
    "¡Esplendido!",
    "¡Soprendente!"
]

def mostrar_menu():
    print("\n==============================")
    print("      JUEGO DE MEMORIA")
    print("==============================")
    print("1 - Jugar")
    print("2 - Salir")

def mostrar_palabras(lista):
    print("\nMemoriza las palabras:\n")

    for palabra in lista:
        print(palabra)

    # "Limpia" la pantalla por unos segundos
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

    respuesta = input("\nIngrese una opción (1-3): ")

    if respuesta == "1":
        elegida = opciones[0]
    elif respuesta == "2":
        elegida = opciones[1]
    elif respuesta == "3":
        elegida = opciones[2]
    else:
        return False

    return elegida == correcta

def jugar():
    nombre = input("\nIngrese su nombre: ")

    puntos = 0

    for ronda in range(1, 7):

        print("\n==========")
        print("RONDA", ronda)
        print("==========")

        seleccion = random.sample(palabras, 4)

        mostrar_palabras(seleccion)

        if hacer_pregunta(seleccion):

            print(random.choice(mensajes))
            puntos += 10

        else:
            print("Respuesta incorrecta.")

        print("Puntaje:", puntos)

    print("\n===================")
    print("Juego terminado")
    print("===================")

    print("Jugador:", nombre)
    print("Puntaje final:", puntos)

opcion = ""

while opcion != "2":

    mostrar_menu()

    try:
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            jugar()

        elif opcion == "2":
            print("\n¡Gracias por jugar!")

        else:
            print("\nOpción incorrecta.")

    except ValueError:
        print("\nError: Debe ingresar un número.")