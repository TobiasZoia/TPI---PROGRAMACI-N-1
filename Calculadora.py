



def solucion(expresion):    
    
    numeros = []
    operadores = []   
    acumulado = 0
    numero_actual = 0    

    for caracter in expresion:
        if verificar_es_numero(caracter):             
            numero_actual = concatenar_numero(numero_actual, caracter)

        elif verificar_operador(caracter):     
            numeros.append(numero_actual)           
            operadores.append(caracter)
            numero_actual = 0
    numeros.append(numero_actual)
    return resolver_expresion(numeros,operadores)
    


def resolver_expresion(lista_numeros,operadores):
    lista_resultados = []
    contador = 1

def resolver_expresion(lista_numeros, operadores):
    # Primera pasada: multiplicación y división
    contador = 0
    while contador < len(operadores):
        if operadores[contador] in ("*", "/"):
            numero_a = lista_numeros[contador]
            numero_b = lista_numeros[contador + 1]
            resultado = resolver_operacion(operadores[contador], numero_a, numero_b)
            lista_numeros[contador] = resultado
            lista_numeros.pop(contador + 1)
            operadores.pop(contador)
            
        else:
            contador += 1

    #Segunda Pasada:
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


def suma(a,b): return a+b

def resta(a,b):return a-b

def division(a,b): return a/b

def multiplicacion(a,b): return a*b

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
    nuevo_digito = int(nuevo_digito)
    if acumulado == 0:
        return nuevo_digito
    return (acumulado*10)+nuevo_digito


def verificar_operador(operador):
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
        case "0":
            return True
        case _:
            return False


while True:
    expresion = input("Ingresa la expresion: ")

    print(solucion(expresion))
