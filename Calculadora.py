

def solucion(expresion):    
    
    # Listas donde se guardan los números y operadores de la expresión
    numeros = []
    operadores = []   
    # Variables sin uso actualmente
    acumulado = 0
    indicador_negativo = 0    
    # Número que se va armando dígito a dígito
    numero_actual = 0
    # Contador para recorrer la expresión carácter a carácter
    contador = 0
    # Acumula caracteres para formar números negativos (ej: "-5")
    simbolo = ""

    while contador < len(expresion):
        # Tomamos el carácter actual y lo agregamos al símbolo acumulado
        caracter = expresion[contador]
        simbolo += caracter
        # caracter ahora apunta al símbolo acumulado, no al carácter solo
        caracter = simbolo

        if verificar_es_numero(caracter):
            # Si el símbolo acumulado es un número, lo concatenamos al número actual
            numero_actual = concatenar_numero(numero_actual, caracter)
            # Reseteamos el símbolo para el próximo carácter
            simbolo = ""
           
        elif verificar_operador(caracter):  
            # Si el operador anterior también es operador (o estamos al inicio),
            # significa que es el signo de un número negativo, lo acumulamos
            if verificar_operador(expresion[contador-1]) or contador == 0:
                simbolo = caracter                 
            else:
                # Si no, el número actual está completo, lo guardamos
                numeros.append(numero_actual)
                # Guardamos el operador
                operadores.append(caracter)
                # Reseteamos para el próximo número
                numero_actual = 0
                simbolo = ""

        contador += 1
            
    # Si no se encontró ningún número, la expresión no es válida
    if numeros == []:        
        raise ValueError

    # Agregamos el último número que quedó pendiente
    numeros.append(numero_actual)
    # Resolvemos la expresión con las listas de números y operadores
    return resolver_expresion(numeros, operadores)

def resolver_expresion(lista_numeros, operadores):
    
    # Primera pasada: multiplicación y división
    # Inicializamos el contador en 0 para recorrer la lista de operadores
    contador = 0
    while contador < len(operadores):
        # Si el operador actual es multiplicación o división (mayor precedencia)
        if operadores[contador] in ("*", "/"):
            # Tomamos los dos números que rodean al operador
            numero_a = lista_numeros[contador]
            numero_b = lista_numeros[contador + 1]

            # Resolvemos la operación entre esos dos números
            resultado = resolver_operacion(operadores[contador], numero_a, numero_b)
            
            # Reemplazamos numero_a con el resultado en la misma posición
            lista_numeros[contador] = resultado
            # Eliminamos numero_b ya que fue consumido en la operación
            lista_numeros.pop(contador + 1)
            # Eliminamos el operador ya que también fue consumido
            operadores.pop(contador)
            # No incrementamos el contador porque al hacer pop
            # el siguiente elemento ya quedó en la posición actual
            
        else:
            # Si no es * ni /, avanzamos al siguiente operador
            contador += 1

    #Segunda Pasada:
    #Misma situacion que en la parte superior
    contador = 0
    while contador < len(operadores):
        if operadores[contador] in ("+", "-"):
            numero_a = lista_numeros[contador]
            numero_b = lista_numeros[contador + 1]

            resultado = resolver_operacion(operadores[contador], numero_a, numero_b)
            lista_numeros[contador] = resultado
            lista_numeros.pop(contador + 1)
            operadores.pop(contador)
        else:
            contador += 1

    return lista_numeros[0]

def suma(a,b):  return a+b

def resta(a,b): return a-b

def division(a,b):
    #Inicializamos variables utiles
    resultado = 0
    negativo = False
    # Verificamos si uno de los numeros tiene un simbolo negativo
    if a < 0:
        negativo = not negativo
    if b < 0:
        negativo = not negativo
    # Independientemente de que uno o dos o ninguno sea negativo, buscamos el absoluto para tener certeza
    a,b = abs(a),abs(b)
    #Verificamos si  se quiere realizar una division por 0, si es 0 damos un error.
    if b == 0:
        raise ZeroDivisionError
    # En caso de que no haya una division por cero, realizamos la division
    else:
        while a >= b:
            a -= b
            resultado += 1
    # Una vez hecha, le volvemos a dar su simbolo si es negativo, si no, se devuelve positivo.
    if negativo:
        return -resultado
    else:
        return resultado

def multiplicacion(a,b):
    #Inicializamos variables utiles
    resultado = 0
    negativo = False
    # Verificamos si uno de los numeros tiene un simbolo negativo
    if a < 0:
        negativo = not negativo
    if b < 0:
        negativo = not negativo
    # Independientemente de que uno o dos o ninguno sea negativo, buscamos el absoluto para tener certeza
    a,b = abs(a),abs(b)
    #Verificamos si  se quiere realizar una division por 0, si es 0 damos un error.
    if b == 0 or a == 0:
        return 0
    # En caso de que no haya una division por cero, realizamos la division
    else:
        for x in len(b):
            resultado += a
            
    # Una vez hecha, le volvemos a dar su simbolo si es negativo, si no, se devuelve positivo.
    if negativo:
        return -resultado
    else:
        return resultado

def resolver_operacion(operacion,numero_a,numero_b):
    match operacion:
        case "+":
           return suma(numero_a,numero_b)
        case "-":
            return resta(numero_a,numero_b)
        case "/":
            return division(numero_a,numero_b)
        case "*":
           return multiplicacion(numero_a,numero_b)
        case _:
            print("Operacion no permitida")

def concatenar_numero(acumulado,nuevo_digito):
    # Convertimos el caracter dado a un int
    nuevo_digito = int(nuevo_digito)
    #Si el numero es negativo, convertimos el nuevo digito en negativo.
    if acumulado < 0:
        nuevo_digito *= -1
    # Verificamos si el numero comienza, si comienza se devuelve solamente el valor del digito dado
    if acumulado == 0:
        return nuevo_digito
    # Si no, movemos el acumulado un digito a la izquierda y le sumamos el nuevo digito, dando el numero final
    return (acumulado*10)+nuevo_digito


def verificar_operador(operador):
    #Verifica si operador es un operador
    match operador:
        case "+":
            return True
        case "-":
            return True
        case "/":
            return True
        case "*":
            return True
        case _:
            return False

def verificar_es_numero(caracter):
    match caracter:
        case "0":
            return True
        case "1":
            return True
        case "2":
            return True
        case "3":
            return True
        case "4":
            return True
        case "5":
            return True
        case "6":
            return True
        case "7":
            return True
        case "8":
            return True
        case "9":
            return True
        case "-1":
            return True
        case "-2":
            return True
        case "-3":
            return True
        case "-4":
            return True
        case "-5":
            return True
        case "-6":
            return True
        case "-7":
            return True
        case "-8":
            return True
        case "-9":
            return True
        case _:
            return False



def menu_calculadora():
    expresion = ""
    while expresion != "salir":
        print("Si desea salir, ingrese salir.")

        #Pedimos la expresion al usuario y luego la convertimos en minuscula para verificar si quiere salir.
        expresion = input("Ingresa la expresion: ")
        expresion = expresion.lower()
        
        #Si no quiere salir, se llama a la funcion de solucion para poder darle la respuesta, en caso de error se, maneja con un except y se da el motivo.
        try:
            print(f"El resultado de {expresion} es {solucion(expresion)}")
        except ValueError:
            if expresion != "salir":
                print(f"{expresion} no es un ejercicio matematico")
        except ZeroDivisionError:
            print(f"{expresion} tiene una division por 0, por cual no es valida.")
        
