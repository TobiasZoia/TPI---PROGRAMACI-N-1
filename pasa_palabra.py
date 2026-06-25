from guardado import guardar_puntaje

def pasa_palabra():
    import time

    def mostrar_preguntas(letra):
        print("\nLetra:", letra)
        print(preguntas[letra][0])
        print("1 - Responder")
        print("2 - Pasapalabra")
        print("3 - Salir")
        print("0 - Volver al menú")

    def mostrar_rosco(rosco):
        for fila in rosco:
            for elemento in fila:
                print(elemento, end=" ")
            print()

    def mostrar_tiempo(inicio):
        restante = 180 - int(time.time() - inicio)
        if restante < 0:
            restante = 0
        print("Tiempo restante:", restante, "segundos")

    def verificar(letra, respuesta, preguntas):
        respuestas_validas = preguntas[letra][1]

        for respuesta_correcta in respuestas_validas:
            if respuesta.lower().strip() == respuesta_correcta:
                return 1

        return 0

    def quedan_preguntas(estados):
        for letra in estados:
            if estados[letra] == 0 or estados[letra] == 3:
                return 1
        return 0

    def actualizar_rosco(rosco, estados):
        for i in range(len(rosco)):
            for j in range(len(rosco[i])):
                letra = rosco[i][j]
                if letra in estados:
                    if estados[letra] == 1:
                        rosco[i][j] = "✓"
                    elif estados[letra] == 2:
                        rosco[i][j] = "✗"
                    elif estados[letra] == 3:
                        rosco[i][j] = "?"

    rosco = [
        [" "," "," "," ","A","B","C"," "," "," "," "],
        [" "," "," ","Z"," "," "," ","D"," "," "," "],
        [" "," ","Y"," "," "," "," "," ","E"," "," "],
        [" ","X"," "," "," "," "," "," "," ","F"," "],
        ["W"," "," "," "," "," "," "," "," "," ","G"],
        ["V"," "," "," "," "," "," "," "," "," ","H"],
        ["U"," "," "," "," "," "," "," "," "," ","I"],
        ["T"," "," "," "," "," "," "," "," "," ","J"],
        ["S"," "," "," "," "," "," "," "," "," ","K"],
        [" ","R"," "," "," "," "," "," "," ","L"," "],
        [" "," ","Q"," "," "," "," "," ","M"," "," "],
        [" "," "," ","P"," "," "," ","N"," "," "," "],
        [" "," "," "," ","","O","Ñ"," "," "," "," "]
    ]

    preguntas = {
        "A": ["los animales que viven debajo del agua son...", ["acuaticos"]],
        "B": ["ciencia que estudia los seres vivos", ["biologia"]],
        "C": ["ciudad o localidad principal de un pais", ["capital"]],
        "D": ["animales que vivieron en la era prehistorica", ["dinosaurio", "dinosaurios"]],
        "E": ["cuando una figura geométrica que tiene todos sus lados iguales se considera", ["equilatero"]],
        "F": ["conjunto de plantas de una region", ["flora"]],
        "G": ["rama de la ciencia que estudia el origen y composicion de la tierra, esta vinculada la geografia", ["geologia"]],
        "H": ["ciencia social que estudia, analiza e interpreta los acontecimientos del pasado", ["historia"]],
        "I": ["porcion de la tierra rodeada de agua, puede ser grande o pequeña", ["isla"]],
        "J": ["planeta mas grande de nuestro sistema solar", ["jupiter"]],
        "K": ["unidad de medida que equivale a mil gramos", ["kilos", "kilo", "kilogramos", "kilogramo"]],
        "L": ["satelite natural de la tierra", ["luna"]],
        "M": ["tipo de energia renovable que usa el movimiento de las mareas del mar para generar energias", ["mareomotriz"]],
        "N": ["vapor de agua concentrado en el cielo", ["nubes", "nube"]],
        "Ñ": ["ave corredora muy grande, parecida al avestruz, que vive en América del Sur.", ["ñandu"]],
        "O": ["la capa que cubre la tierra es conocida como la capa de...", ["ozono"]],
        "P": ["objeto redondo que se usa para los deportes, ejemplo, futbol", ["pelota"]],
        "Q": ["ciencia en la que se estudia la materia, su composicion, propiedades y las reacciones que experimenta", ["quimica"]],
        "R": ["operacion matematica que consiste en reducir o mostrar la diferencia de cantidad entre dos o mas numeros", ["resta", "restar"]],
        "S": ["grupo de individuos que conviven organizadamente en un territorio determinado", ["sociedad"]],
        "T": ["figura geometrica equilatera de tres lados", ["triangulo"]],
        "U": ["contiene galaxias, sistemas solares y muchas estrellas", ["universo"]],
        "V": ["deporte donde la pelota no puede tocar el suelo y el campo esta dividido en medio por una red", ["voley"]],
        "W": ["mujer en ingles", ["woman"]],
        "X": ["instrumento musical de percusión formado por láminas de madera o metal que se golpean con baquetas", ["xilofono"]],
        "Y": ["como se dice tu/vos en ingles", ["you"]],
        "Z": ["animal iconico del famoso cuento El Principito", ["zorro"]]
    }

    estados = {}
    for letra in preguntas:
        estados[letra] = 0

    print("=====================================================================================================================")
    print("PASAPALABRA GENERAL")
    print("=====================================================================================================================")
    print("REGLAS")
    print("- puedes pasar (2) o responder las preguntas (1)")
    print("- tienes 3 minutos (180 segundos)")
    print("- escribe 0 en cualquier momento para volver al menú")

    nombre = input("Ingrese su nombre: ")

    if nombre == "0":
        return -1

    puntaje_juego4 = 0
    inicio = time.time()
    seguir = 1

    while seguir == 1 and quedan_preguntas(estados) == 1:

        if time.time() - inicio >= 180:
            print("\nTiempo agotado")
            seguir = 0

        else:

            actualizar_rosco(rosco, estados)

            print("\n==============================")
            mostrar_rosco(rosco)
            print("==============================")

            print("Puntaje:", puntaje_juego4)
            mostrar_tiempo(inicio)

            for letra in preguntas:

                if seguir == 1:
                    if estados[letra] == 0 or estados[letra] == 3:
                        mostrar_preguntas(letra)
                        opcion = input("Opción: ")

                        if opcion == "0":
                            guardar_puntaje(
                                "puntaje_pasapal.txt", nombre, puntaje_juego4)
                            return puntaje_juego4

                        while opcion != "1" and opcion != "2" and opcion != "3":
                            print("opcion invalida, seleccione un numero")
                            mostrar_preguntas(letra)
                            opcion = input("Opcion: ")

                            if opcion == "0":
                                guardar_puntaje("puntaje_pasapal.txt", nombre, puntaje_juego4)
                                return puntaje_juego4

                        if opcion == "1":

                            respuesta = input("Respuesta: ")

                            if respuesta == "0":
                                guardar_puntaje(
                                    "puntaje_pasapal.txt", nombre, puntaje_juego4)
                                return puntaje_juego4
                            if verificar(letra, respuesta, preguntas) == 1:
                                print("Correcto")
                                puntaje_juego4 += 2
                                estados[letra] = 1
                            else:
                                print("Incorrecto")
                                puntaje_juego4 -= 1
                                estados[letra] = 2
                        elif opcion == "2":
                            estados[letra] = 3
                        elif opcion == "3":
                            seguir = 0

    print("\nJuego terminado")
    print("Jugador:", nombre)
    print("Puntaje final:", puntaje_juego4)

    guardar_puntaje(
        "puntaje_pasapal.txt", nombre, puntaje_juego4)

    return puntaje_juego4