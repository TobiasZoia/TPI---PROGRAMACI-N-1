#PRIMER JUEGO ORDENAR PALABRAS, en un diccionario en el que la clave es el nivel y en cada nivel hay otro diccionario dentro con la palabra mezclada (clave) y la palabra ordenada (valor)
def ordenar_palabras():
    niveles = {1: {"gtoa": "gato", "same": "mesa"}, 2: {"saleecu": "escuela", "orrpe": "perro"}, 3: {"darutocomap": "computadora", "calotibibea": "biblioteca"}, 4: {"nrgpaamacioor": "programacion", "ocdriicanio": "diccionario"}, 5: {"drrsleaolaode": "desarrollador", "nidsuvdirae": "universidad"}}
    vidas = 3
    puntaje_juego1 = 0

    print("=====================================================================================================================")
    print("ORDENA LA PALABRA")
    print("=====================================================================================================================")
    print("REGLAS:")
    print("- Tenes que ordenar correctamente la palabra mostrada.")
    print("- Hay 5 niveles con 2 palabras cada uno.")
    print("- Empezas con 3 vidas.")
    print("- Tenes hasta 3 intentos por palabra.")
    print("- Si acertas al primer intento ganas 3 puntos, ganas uno menos por cada error que tengas en la misma palabra palabra.")
    print("- Si fallas los 3 intentos, perdes una vida.")
    print("- Si tus vidas llegan a 0, perdes la partida.")
    print("- Completa todos los niveles para ganar.")
    print("=====================================================================================================================")
    print("IMPORTANTE ESCRIBIR LA PALABRA SIN TILDES")
    print("=====================================================================================================================")
    print("1 - Comenzar juego")
    print("0 - Volver al menú (Puede hacerlo en cualquier momento)")

    opcion=input("Ingrese una opción: ")
    while opcion!="0" and opcion!="1":
        opcion=input("Ingrese una opción valida: ")
    if opcion=="0":
        return -1

    for nivel in range(1, 6):
        print("==========")
        print("NIVEL", nivel)
        print("==========")

        for mezclada, palabra in niveles[nivel].items():
            print("VIDAS:", vidas)
            print("PUNTAJE:", puntaje_juego1)
            print("ORDENA LA PALABRA:")
            print(mezclada)
            intento=1
            aciertos=0

            while intento<=3 and aciertos==0:
                respuesta=input("Ingrese la palabra: ").lower()
                if respuesta=="0":
                    print("gracias por jugar")
                    return puntaje_juego1
                elif respuesta==palabra:
                    puntos=4-intento
                    puntaje_juego1+=puntos
                    print("¡Correcto!")
                    print("Ganaste", puntos, "puntos")
                    aciertos=1
                else:
                    if intento<3:
                        print("Incorrecto")
                        print("Te quedan", 3 - intento, "intentos")
                intento+=1

            if aciertos==0:
                vidas-=1
                print("Perdiste una vida")
                print("La palabra correcta era:", palabra)
                if vidas==0:
                    print("PERDISTE")
                    print("Puntaje final:", puntaje_juego1)
                    return puntaje_juego1
    print("¡FELICITACIONES!")
    print("Llegaste al final")
    print("Puntaje final:", puntaje_juego1)
    return puntaje_juego1