#!/usr/bin/python3
# -*- coding: utf-8 -*-
from termcolor import colored
import os

# Representamos a una matriz de n columnas y filas, con numeros como:
# maze: list(list(int))
# Por ejemplo:
# [["0", "0", "0", "0", "0", "0"],
# ["1", "1", "1", "0", "1", "1"],
# ["1", "1", "1", "0", "1", "1"],
# ["1", "1", "0", "0", "1", "1"],
# ["1", "1", "0", "1", "1", "1"],
# ["1", "1", "0", "0", "2", "1"]]

# Llamamos a colored(maze) al maze que fue editado con la libreria termcolor

# El archivo con el laberinto tiene que tener la siguiente forma:
# - Cada linea tiene que ser una fila del laberinto
# - Representamos con "1" las paredes
# - Representamos con "0" los espacios en blanco
# - Representamos con "-" los lugares visitados
# - Representamos el objetivo con "2"
# - Cada valor tienen que estar separados con un espacio
# - Importante! El archivo debe finalizar con un salto de línea
# Ejemplo:

# 0 1 0 0 0 1 0 0 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 1 0 1 0 1 0 1 0 1
# 0 0 0 1 0 0 0 1 0 2
#


# parse_maze: file -> maze
# Recibe un archivo
# Devuelve un maze
def parse_maze(f):
    maze = []

    for line in f.readlines():
        line = line.strip("\n")
        maze.append(line.split(" "))

    return maze


# is_near_objective: maze list((int, int)) -> list((int, int))
# Recibe un maze y una lista de tupla
# Esta lista representa una lista de coordenadas las cuales son los lugares que
# podemos visitar
# Devuelve una lista de tuplas
# En el caso de que el objetivo este en unos de esos espacios que podemos
# visitar, devuelve una lista con esa coordenada
# De lo contrario devuelve la lista recibida anteriormente
def is_near_objective(maze, free_spaces):
    spaces = []

    for space in free_spaces:

        if (maze[space[0]][space[1]] == "2"):
            spaces.append(space)

    if len(spaces) == 0:
        return free_spaces

    return spaces


# posible_action: maze (int, int) -> list((int, int))
# Recibe un maze una tupla de int
# Los elementos de la tuplas representan la fila y la columna dentro del
# laberinto
# Devuelve una lista de tuplas que representan las coordenadas a la cuales
# nos podemos mover
# Tenemos como prioridad devolver primero la posibilidades de mover hacia
# abajo o hacia la derecha. Luego consideramos a para arriba y la izquierda
def posible_action(maze, position):
    free_spaces = []
    size = len(maze)

    if (position[0] != size - 1 and
       maze[position[0] + 1][position[1]] != "1" and
       maze[position[0] + 1][position[1]] != "-"):
        free_spaces.append((position[0] + 1, position[1]))

    if (position[1] != size - 1 and
       maze[position[0]][position[1] + 1] != "1" and
       maze[position[0]][position[1] + 1] != "-"):
        free_spaces.append((position[0], position[1] + 1))

    if (position[0] != 0 and
       maze[position[0] - 1][position[1]] != "1" and
       maze[position[0] - 1][position[1]] != "-"):
        free_spaces.append((position[0] - 1, position[1]))

    if (position[1] != 0 and
       maze[position[0]][position[1] - 1] != "1" and
       maze[position[0]][position[1] - 1] != "-"):
        free_spaces.append((position[0], position[1] - 1))

    return is_near_objective(maze, free_spaces)


# color_maze: maze list((int, int)) -> colored(maze)
# Recibe una laberinto y una lista de tuplas
# Las tuplas representan las coordenadas que forman la solucion del laberinto
# Esta funcion cambia el color de los elementos que se encuentran en las
# coordenadas que se encuentran en la lista de tuplas
# Devuelve un colored(maze), para que sea mas facil visualizar el camino
def color_maze(maze, steps):
    for step in steps:
        maze[step[0]][step[1]] = colored(maze[step[0]][step[1]], color="green")

    return maze


# display_maze: maze boolean list((int, int)) -> None
# Recibe un laberinto y el camino hacia la salida y lo muestra
# En el caso que visual sea True, colorea el camino
def display_maze(maze, visual, steps=None):
    if visual:
        maze = color_maze(maze, steps)

    print("\n".join([" ".join(row) for row in maze]))
    print("")


# solve_maze: maze -> list((int, int))
# Recibe un maze
# Devuelve una lista con tuplas que representan coordenadas
# Esta lista contiene las coordenadas espesificas que resuelven el laberinto
# Para poder resolver el maze y no entrar en  lugares visitados, cambia los
# "0" que visito por "-"
def solve_maze(maze, visual):
    solve = False
    actual_position = (0, 0)
    steps = []

    while not solve:
        free_spaces = posible_action(maze, actual_position)
        nActions = len(free_spaces)

        if (nActions == 0):
            nSteps = len(steps)
            maze[actual_position[0]][actual_position[1]] = "-"
            actual_position = steps[nSteps - 1]
            steps.pop(nSteps - 1)

        else:
            maze[actual_position[0]][actual_position[1]] = "-"
            steps.append(actual_position)
            actual_position = free_spaces[0]

        element_in_maze = maze[actual_position[0]][actual_position[1]]

        if element_in_maze == "2":
            steps.append(actual_position)
            solve = True

        if len(steps) == 0:
            print(colored("No se pudo resolver el laberinto", color="red"))
            solve = True

    display_maze(maze, visual, steps)

    return steps


if __name__ == "__main__":
    VISUAL = False
    done = False

    print("Trabajo Practico Final")
    print("Alumno: Bautista Marelli\n")

    op = input("Quieres activar el Modo Visual? 1/0\n")

    while not done:

        print("Primero revise la documentacion sobre como ingresar el archivo")

        filename = input(">>> Ingresa el nombre del archivo: ")
        try:
            with open(filename, "r") as f:
                maze = parse_maze(f)
                display_maze(maze, VISUAL)

                if op == "1":
                    VISUAL = True

                input(">>> Enter para continuar")
                # borramos la pantalla
                os.system('cls' if os.name == 'nt' else 'clear')

                if VISUAL:
                    solve_maze(maze, VISUAL)

                else:
                    print(solve_maze(maze, VISUAL))

                done = True

        except FileNotFoundError:
            print(colored("El archivo no existe", color="red"))
