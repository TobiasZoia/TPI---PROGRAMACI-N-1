#Importa el juego o programa
from JUEGO1_ORDENAR_PALABRAS import ordenar_palabras
from trivia import trivia_de_geografia
from pasa_palabra import pasa_palabra
from Calculadora import calculadora

#Procedimiento para mostrar los puntajes ordenados
def mostrar_puntajes(puntajes):
    print("========== PUNTAJES =========")
    for juego, puntaje in puntajes.items():
        print(juego, ":", puntaje)

#Procedimiento para mostrar el menú y seleccionar los juegos, los case, claves del diccionario y prints del menú se van a ir actualizando a medida que se carguen los nuevos juegos
def menu():
    puntajes = {"Ordena Palabras": 0, "Trivia de Geografia": 0, "Juego 3": 0, "Pasa Palabra": 0, "Calculadora": 0}
    opcion = -1
    while opcion != 0:
        print("==============================")
        print("PLAY.IN - PLATAFORMA EDUCATIVA")
        print("==============================")
        print("Elija una opción")
        print("1 - Ordena la palabra")
        print("2 - Trivia de Geografia")
        print("3 - Juego 3")
        print("4 - Pasa Palabra")
        print("------------------------------------")
        print("5 - Calculadora")
        print("------------------------------------")
        print("6 - Ver puntajes")
        print("0 - Salir")
        print("====================================")
        try:
            opcion = int(input("Ingrese una opción: "))
            while opcion < 0 or opcion > 6:
                opcion = int(input("Ingrese una opción válida: "))
        except ValueError:
            print("Debe ingresar un número.")
            opcion = -1

        match opcion:
            case 1:
                puntajes["Ordena Palabras"]= ordenar_palabras()
            case 2:
                puntajes["Trivia de Geografia"]= trivia_de_geografia()
            case 3:
                puntajes["Juego 3"]=juego3()
            case 4:
                puntajes["Pasa Palabra"]= pasa_palabra()
            case 5:
                puntajes["Calculadora"]=calculadora()
            case 6:
                mostrar_puntajes(puntajes)
            case 0:
                print("Gracias por jugar")
#Ejecutar el menú                
menu()