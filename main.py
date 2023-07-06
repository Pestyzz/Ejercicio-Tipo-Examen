#Importamos la librería numpy para hacer uso del array requerido en la rúbrica.
import numpy as np
from datetime import date

""" FUNCIONES DEL PROGRAMA """

#Función que valida el ingreso de opciones del menú.
def menu_options():
    while True:
        try:
            print("\tINMOBILIARIA CASA FELIZ\n\nMenu Principal:")
            userOption = int(input("1.Comprar Departamento\n2.Mostrar departamentos disponibles\n3.Ver listado de compradores\n4.Mostrar ganancias totales\n5.Salir\n>>Ingrese un dígito: "))
            
            if userOption in range(1, 6):
                return userOption
            else:
                print("Opción no válida.")
        except ValueError:
            print("Caracter inválido.")

#Función que hace la validación del ingreso de datos que haga el usuario al comprar.
def user_input(message, piso=False, tipo=False, run=False):
    while True:
        try:
            userInput = input(message)
            #Validación ingreso número de piso
            if piso == True:
                if userInput.isdigit() == True:
                    userInput = int(userInput)
                else:
                    raise ValueError
                
                if userInput in range(1,11):
                    pass
                else:
                    print("Número de piso inválido.")
                    continue
            #Validación ingreso tipo de piso A,B,C,D
            elif tipo == True:
                userInput = userInput.upper()
                
                if userInput.isalpha() == False:
                    raise ValueError
                elif userInput not in ["A", "B", "C", "D"]:
                    print("Tipo inválido.")
                    continue
            #Validación ingreso run
            elif run == True:
                userInput = userInput.upper()
                
                if len(userInput) != 12:
                    print("Formato inválido.")
                    continue
                elif userInput[2] != "." or userInput[6] != "." or userInput[10] != "-":
                    print("Formato inválido.")
                    continue
                elif userInput[11] not in ['0', '1', '2', '3', '4', '5', '6', '9', 'K']:
                    print("Formato inválido.")
                    continue
            return userInput
        except ValueError:
            print("Caracter inválido.")
            
def comprar_dep():
    while True:
        print("Precios:\n-Tipo A: 3.800 UF\n-Tipo B: 3.000 UF\n-Tipo C: 2.800 UF\n-Tipo D: 3.500 UF ")
        piso = user_input("Ingrese el número del piso (1 al 10): ", piso=True)
        tipo = user_input("Ingrese el tipo de piso: ", tipo=True)
        
        #Utilización de la función ord(), lo que hace básicamente es devolver el valor numérico correspondiente al código Unicode de un carácter.
        tipo = ord(tipo)

        if matrizDep[piso-1, tipo-65] == "X":
            print("No está disponible.")
            continue
        else:
            matrizDep[piso-1, tipo-65] = "X"
            
        run = user_input("Ingrese su RUN (XX.XXX.XXX-X): ", run=True)
        #Se reemplaza el formato con el que se ingresó para registrarlo en la lista con el formato requerido en la rúbrica.
        run = run.replace('-', '').replace('.', '').replace(run[-1], '')
        
        listaCompradores.append(run)
        return
    
def mostrar_deps():
    print("\n      |     Tipo      ")
    print("PISOS +---------------")
    print("      | A | B | C | D ")
    print("------+---+---+---+---")
    for i in range(9, -1, -1):
        print(f"{i+1:5d} | {matrizDep[i, 0]:1s} | {matrizDep[i, 1]:1s} | {matrizDep[i, 2]:1s} | {matrizDep[i, 3]:1s} ")
        print("------+---+---+---+---")
    print("")

def mostrar_ventas():
    cantA = int(0)
    cantB = int(0)
    cantC = int(0)
    cantD = int(0)
    
    for i in range(10):
        if matrizDep[i, 0] == "X":
            cantA += 1
        if matrizDep[i, 1] == "X":
            cantB += 1
        if matrizDep[i, 2] == "X":
            cantC += 1
        if matrizDep[i, 3] == "X":
            cantD += 1
            
    cantTotal = cantA + cantB + cantC + cantD
    sumTotal = cantA * 3800 + cantB * 3000 + cantC * 2800 + cantD * 3500
    print("\nTipo de Departamento | Cantidad | Total")
    print("---------------------+----------+------")
    print(f"Tipo A 3.800 UF      | {cantA:4d}     | {cantA*3800} UF")
    print("---------------------+----------+------")
    print(f"Tipo B 3.000 UF      | {cantB:4d}     | {cantB*3000} UF")
    print("---------------------+----------+------")
    print(f"Tipo C 2.800 UF      | {cantC:4d}     | {cantC*2800} UF")
    print("---------------------+----------+------")
    print(f"Tipo D 3.500 UF      | {cantD:4d}     | {cantD*3500} UF")
    print("---------------------+----------+------")
    print(f"TOTAL                | {cantTotal:4d}     | {sumTotal} UF")
    print("---------------------+----------+------\n")
    
def ver_compradores():
    listaCompradores.sort()
    print("Lista Compradores\n")
    for i in listaCompradores:
        print(f"{i} ")
        print("------------")
    print("")
        
def salir():
    print(f"Saliendo...\nBastián Ñiripil\n{date.today()}")
    menu = 0
    return
    
""" PROGRAMA PRINCIPAL """
menu = int(1)

#10 Representa la cantidad total de pisos y 4 los tipos de departamento por piso.
matrizDep = np.empty((10, 4), dtype=object)
matrizDep.fill("")
#El método fill(), rellena los espacios vacíos con un espacio vacío ""

listaCompradores = []

while menu == 1:
    userOption = menu_options()
    
    match userOption:
        case 1:
            mostrar_deps()
            comprar_dep()
        case 2:
            mostrar_deps()
        case 3:
            ver_compradores()
        case 4:
            mostrar_ventas()
        case 5:
            menu = salir()