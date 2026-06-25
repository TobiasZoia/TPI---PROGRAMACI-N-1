#SEGUNDO JUEGO TRIVIA DE GEOGRAFIA 
from guardado import guardar_puntaje 
def trivia_de_geografia():

    niveles = { 1: {"Cuantos continentes hay?": "siete", "En que continente esta Argentina?": "america"}, 2: {"En que pais esta la Torre de Pisa": "italia", "En que pais esta el Obelisco": "argentina"}, 3: {"Capital de Argentina": "buenos aires", "Capital de Francia": "paris"}}

    puntos = 0

    print("==============================================================================")
    print("TRIVIA DE GEOGRAFIA")
    print("==============================================================================")
    print("REGLAS:")
    print("Existen 3 niveles de dificultad con 2 preguntas por cada nivel")
    print("Cada respuesta vale 1 punto")
    print("==============================================================================")
    print("ESCRIBIR LA PALABRA SIN TILDES")
    print("LAS RESPUESTAS SON PALABRAS. ¡NO ESCRIBAS NÚMEROS!")
    print("==============================================================================")
    print("1 - Comenzar juego")
    print("0 - Volver al menu (puedes elegir esta opción en cualquier momento)")

    opcion = input("Ingrese una opcion: ")

    while opcion != "0" and opcion != "1":
        opcion = input("Ingrese una opcion valida: ")

    if opcion == "0":
        return -1

    nombre = input("Ingrese su nombre: ")
    
    if nombre == "0":
        return -1

    for nivel in range(1, 4):

        print("NIVEL", nivel)

        for pregunta, palabra in niveles[nivel].items():

            print("PUNTAJE", puntos)
            print(pregunta)

            respuesta = input("Ingrese la respuesta: ").strip().lower()
            
            if respuesta == "0":
                guardar_puntaje("puntaje_trivia.txt", nombre, puntos)
                return puntos
            if respuesta == palabra:
                puntos += 1
                print("Correcto")
            else:
                print("Incorrecto")

    print("===================================")
    print("Juego terminado")
    print("Puntaje final:", puntos)
    print("===================================")

    if puntos <= 2:
        print("Nivel: Principiante")
    elif puntos <= 4:
        print("Nivel: Explorador")
    else:
        print("Nivel: Experto en Geografia")

    guardar_puntaje("puntaje_trivia.txt", nombre, puntos)

    return puntos