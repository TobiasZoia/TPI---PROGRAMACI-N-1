def guardar_puntaje(nombre_archivo, nombre, puntaje):

    puntajes = {}

    try:
        archivo = open(nombre_archivo, "r")

        for linea in archivo:
            datos = linea.strip().split(" - ")
            puntajes[datos[0]] = int(datos[1])

        archivo.close()

    except FileNotFoundError:
        print("Archivo nuevo creado:", nombre_archivo)

    # Si es nuevo jugador o mejoró su puntaje
    if nombre not in puntajes:
        puntajes[nombre] = puntaje

    elif puntaje > puntajes[nombre]:
        puntajes[nombre] = puntaje

    archivo = open(nombre_archivo, "w")

    for jugador, puntos in puntajes.items():
        archivo.write(jugador + " - " + str(puntos) + "\n")

    archivo.close()