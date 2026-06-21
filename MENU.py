#Importa el juego o programa
from JUEGO1_ORDENAR_PALABRAS import ordenar_palabras
from trivia import trivia_de_geografia
from pasa_palabra import pasa_palabra
from  Calculadora import menu_calculadora
from memoria import memoria

#Procedimiento para mostrar los puntajes ordenados
def mostrar_puntajes(puntajes):
    print("========== PUNTAJES =========")
    for juego, puntaje in puntajes.items():
        print(juego, ":", puntaje)

#Procedimiento para mostrar el menú y seleccionar los juegos, los case, claves del diccionario y prints del menú se van a ir actualizando a medida que se carguen los nuevos juegos
def menu():
    puntajes = {"Ordena Palabras": 0, "Trivia de Geografia": 0, "Memoria": 0, "Pasa Palabra": 0}
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
                resultado= ordenar_palabras()
                if resultado != -1:
                    puntajes["Ordena Palabras"]= resultado
            case 2:
                resultado= trivia_de_geografia()
                if resultado != -1:
                    puntajes["Trivia de Geografia"]= resultado
            case 3:
                resultado = memoria()
                if resultado != -1:
                    puntajes["Memoria"]=resultado                
            case 4:
                resultado=pasa_palabra()
                if resultado != -1:
                    puntajes["Pasa Palabra"]= resultado
            case 5:
                menu_calculadora()
            case 6:
                mostrar_puntajes(puntajes)
            case 0:
                print("Gracias por jugar")
#Ejecutar el menú
menu()