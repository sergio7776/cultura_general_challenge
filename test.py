import os  # Para limpiar la consola
import random  # Para randomizar la seleccion de opciones y preguntas
import csv # Para manipular el archivo 'rankings.csv'
from stock_preguntas import base_de_preguntas # Importar preguntas
import comodines # Importar modulo de comodines

cantidad_preguntas = 10

# Funcion para borrar la consola
def borrar_consola():
    os.system("cls" if os.name == "nt" else "clear")
    
# Funcion para seleccionar una lista aleatoria de 10 preguntas
def crear_lista_preguntas(lista):
    lista_preguntas = []
    random.shuffle(lista)
    for pregunta in range(len(lista)):
        if len(lista_preguntas) == cantidad_preguntas:
            return lista_preguntas
        elif not lista[pregunta] in lista_preguntas:
            lista_preguntas.append(lista[pregunta])

# Funcion para seleccionar una pregunta
def elegir_pregunta(n, lista):
    global opciones, respuesta, pregunta

    pregunta_elegida = lista[n]
    pregunta = pregunta_elegida[0]
    respuesta = pregunta_elegida[1]
    opciones = pregunta_elegida[1:]
    for i in range(4):
        random.shuffle(opciones)
    return pregunta_elegida

# Funcion para imprimir la pregunta elegida
def imprimir_pregunta():
    borrar_consola()
    print(f'Pregunta {n_pregunta + 1}/10')
    print()
    print(pregunta)
    print()
    print("A)", opciones[0])
    print("B)", opciones[1])
    print("C)", opciones[2])
    print("D)", opciones[3])
    print()
    print("Si desea utilizar un comodin, presione la letra 'J'")
    print()

# Funcion para guardar respuesta ingresada
def guardar_respuesta(datos):
    opciones_validas = ["a", "b", "c", "d"]
    while True:
        respuesta_usuario = input("Ingrese la letra de su respuesta: ").lower()
        if respuesta_usuario == 'j':
            comodines.escogerComodin(datos, opciones)
            return guardar_respuesta(datos)
        elif not (respuesta_usuario in opciones_validas):
            print("La respuesta no está entre las opciones válidas, vuelva a intentarlo")
            continue
        break
    print()
    return opciones_validas.index(respuesta_usuario)

# Funcion para actualizar el archivo con los usuarios y sus puntajes
def actualizar_ranking(usuario, puntaje):
    with open("rankings.csv", "a", newline='') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=["usuario", "puntaje"])
        escritor.writerow({"usuario": usuario, "puntaje": puntaje})
        
# Funcion para mostrar lista del ranking de jugadores
def mostrar_ranking():
    jugadores = []
    with open("rankings.csv", "r") as archivo:
            lector = csv.DictReader(archivo)
            print('  Usuario       |       Puntaje  ')
            print()
            for fila in lector:
                jugadores.append(fila)
        
    for jugador in sorted(jugadores, key=lambda jugador: jugador["puntaje"], reverse=True):
        print(f"{jugador['usuario'].center(10)}{jugador['puntaje'].center(35)}")

# Funcion para checkear si un usuario ya ha sido registrado
def usuario_duplicado(usuario):
    with open("rankings.csv", "r") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila["usuario"] == usuario:
                return True
        return False

# Funcion de menu de juego
def menu():
    print("+--------------------------------------+")
    print(" Bienvenidos al JUEGO DE LAS PREGUNTAS! ")
    print("+--------------------------------------+")
    print("    Por favor seleccione una opcion:    ")
    print("    1. Empezar juego                    ")
    print("    2. Rankings                         ")
    print("    3. Salir                            ")
    print("+--------------------------------------+")
    
    while True:
        global usuario
        eleccion = input("Ingrese 1, 2 o 3: ")
        borrar_consola()
        if eleccion == "1":
            while True:
                usuario = input("Ingrese un nombre de usuario: ")
                if usuario_duplicado(usuario):
                    print('Este usuario ya esta tomado, ingrese otro')
                    continue
                elif len(usuario) > 10:
                    print('El maximo de caracteres son 10')
                    continue
                elif len(usuario) < 1:
                    print('El usuario debe contener como minimo 1 caracter')
                    continue
                else:
                    break
            print()
            print(f"Bienvendido {usuario}!")
            print()
            print(f"Tendrás que responder 10 preguntas, buena suerte!")
            print()
            input("PRESIONA ENTER PARA COMENZAR")
            break
            
        elif eleccion == "2":
            mostrar_ranking()
            print()
            while True:
                opcion = input("Ingrese 1 para volver al menu, 2 si quiere salir del juego: ")
                if opcion == '1':
                    jugar()
                elif opcion == '2':
                    quit()
                else:
                    print('Ingrese un numero valido')
                    continue
            
        elif eleccion == "3":
            print("Hasta la proxima!")
            quit()
            
        else:
            print("Ingrese un numero valido")
            continue

# Funcion para comenzar el juego
def jugar():
    menu()
    global n_pregunta
    n_pregunta = 0
    puntaje = 0
    
    lista_preguntas = crear_lista_preguntas(base_de_preguntas)
            
    while True:

        datos = elegir_pregunta(n_pregunta, lista_preguntas)
        imprimir_pregunta()
        
        if opciones[guardar_respuesta(datos)] == respuesta:
            print("Su respuesta es correcta")
            print()
            input("ENTER PARA CONTINUAR")
            puntaje += 1        
        else:
            print("Su respuesta NO es correcta, la correcta es: "+ respuesta)
            print()
            input("ENTER PARA CONTINUAR")
        
        n_pregunta += 1
        
        if n_pregunta == cantidad_preguntas:
            borrar_consola()
            print("El juego ha finalizado")
            print()
            print(f"Su puntaje final fue de: {puntaje}/{cantidad_preguntas} correctas")
            print()
            actualizar_ranking(usuario, puntaje)
            while True:
                opcion = input("Ingrese 1 para volver al menu, 2 si quiere salir del juego: ")
                print()
                if opcion == '1':
                    jugar()
                elif opcion == '2':
                    quit()
                else:
                    print('Ingrese un numero valido')
                    continue
 
jugar()
