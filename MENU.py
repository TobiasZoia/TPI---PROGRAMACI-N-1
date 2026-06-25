#Importa el juego o programa
from JUEGO1_ORDENAR_PALABRAS import ordenar_palabras
from trivia import trivia_de_geografia
from pasa_palabra import pasa_palabra
from Calculadora import menu_calculadora
from memoria import memoria

#Procedimiento para mostrar los puntajes ordenados
def mostrar_puntajes():
    archivos = {"Ordena Palabras": "puntaje_ord_pal.txt", "Trivia de Geografia": "puntaje_trivia.txt", "Memoria": "puntaje_memoria.txt", "Pasa Palabra": "puntaje_pasapal.txt"}
    print("========== PUNTAJES =========")
    for juego, puntaje in archivos.items():
        print("\n"+juego)
        try:
            f = open(puntaje, "r")
            print(f.read())
            f.close()
        except FileNotFoundError:
            print(juego, ": Sin puntaje")
#Procedimiento para mostrar el menú y seleccionar los juegos, los case, claves del diccionario y prints del menú se van a ir actualizando a medida que se carguen los nuevos juegos
def menu():
    opcion = -1
    while opcion != 0:
        print("==============================")
        print("PLAY.IN - PLATAFORMA EDUCATIVA")
        print("==============================")
        print("Elija una opción")
        print("1 - Ordena la palabra")
        print("2 - Trivia de Geografia")
        print("3 - Memoria")
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
                ordenar_palabras()                
            case 2:
                trivia_de_geografia()               
            case 3:
                memoria()                              
            case 4:
                pasa_palabra()
            case 5:
                menu_calculadora()
            case 6:
                mostrar_puntajes()
            case 0:
                print("Gracias por jugar")
#Ejecutar el menú
menu()