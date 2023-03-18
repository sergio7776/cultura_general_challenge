import os
from random import *

def borrar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Funcion para imprimir la pregunta junto con las opciones    
def imprimir_opciones(datos, opciones):
    print(datos[0])
    print()
    print("A)", opciones[0])
    print("B)", opciones[1])
    print("C)", opciones[2])
    print("D)", opciones[3])
    print()


# Funcion para eliminiar dos opciones 
def __disminuirOpciones__(datos, opciones): 

    letras = ['A', 'B', 'C', 'D']
    pos_correcta = opciones.index(datos[1])
    n_random = randint(2, 4)
    pos_alternativa = opciones.index(datos[n_random])

    print(datos[0])
    print()
    if pos_correcta > pos_alternativa:
        print(f"{letras[pos_alternativa]}) {datos[n_random]}")
        print(f"{letras[pos_correcta]}) {datos[1]}")
    else:
        print(f"{letras[pos_correcta]}) {datos[1]}")
        print(f"{letras[pos_alternativa]}) {datos[n_random]}")     
    print()
    

# Funcion para calcular la probabilidad de que se devuelva una respuesta correcta o incorrecta    
def listaProbabilidades(correcto, incorrecto):
    probabilidades = []
    i = 0
    while (i < correcto):
        if (i < incorrecto):
            probabilidades.append("I")
        probabilidades.append("C")
        i += 1
    return probabilidades           

# Funcion para llamar a un amigo a que nos recomiende que respuesta elegir
def __llamarAmigo__(datos, opciones):

    #Probabilidades de que el amigo este:
    probabilidades = listaProbabilidades(70, 30)

    #"Suerte" es un numero aleatorio, que obtiene el valor del mismo numero indexado de la lista.
    #Si el valor es "C", la respuesta del amigo sera correcta, de lo contrario, no.
    suerte = randint(0, 99)
    suerte = probabilidades[suerte]

    print()
    print("Respuesta de tu amigo: ")
    if suerte == "C":
        print()
        print("Me parece que la opcion correcta es... " + datos[1])
        print()
    else:
        opcionErronea = randint(2, 4)
        print()
        print("Me parece que la opcion correcta es... " + datos[opcionErronea])
        print()
    imprimir_opciones(datos, opciones)
    
# Funcion para pedir opinion al publico acerca de que respuesta elegir
def __OpinionPublico__(datos, opciones):
    probabilidades = listaProbabilidades(70, 30)

    suerte = randint(0, 99)
    suerte = probabilidades[suerte]

    print()
    print("Opinión del público: ")
    if suerte == "C":
        print()
        print(str(randint(60, 100)) + "% del publico cree que: " + datos[1] + " es la opción correcta.")
        print()
    else:
        opcionErronea = randint(2, 4)
        print()
        print(str(randint(50, 70)) + "% del publico cree que: " + datos[opcionErronea] + " es la opcion correcta.")
        print()
        
    imprimir_opciones(datos, opciones)
    
# Funcion para validar la eleccion del comodin
def ingreso_numero_comodin():

    try:
        respuesta = int(input("Respuesta: "))
                
        while not (respuesta > 0) or not (respuesta < 5):
            print("Valor inválido. Intente nuevamente.")
            respuesta = int(input("Respuesta: "))

        borrar_consola()
        return respuesta
    
    except ValueError:
    
        print("Valor invalido.")
        ingreso_numero_comodin()
        
# Funcion para elegir el comodin a usar
def escogerComodin(datos, opciones):
    print("-".center(50, "-"))
    print("¿Que comodin prefieres usar?")


    print()
    print("1 - ELIMINA DOS OPCIONES")
    print("2 - LLAMA A UN AMIGO")
    print("3 - QUE OPINA EL PUBLICO?")
    print("4 - CANCELAR")
    print()
    seleccion = ingreso_numero_comodin()

    
    if seleccion == 1:         
        __disminuirOpciones__(datos, opciones)  

    elif seleccion == 2:
        __llamarAmigo__(datos, opciones)

    elif seleccion == 3:
        __OpinionPublico__(datos, opciones)
            
    elif seleccion == 4:
        imprimir_opciones(datos, opciones)



