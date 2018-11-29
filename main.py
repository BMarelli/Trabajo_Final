#!/usr/bin/python3
# -*- coding: utf-8 -*-
# from termcolor import colored

# Representamos a una matriz de n columnas y filas como:
# maze: list(list(int))
# Por ejemplo:
# [[0, 0, 0, 0, 0, 0],
#  [1, 1, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1, 1],
#  [1, 1, 0, 0, 1, 1],
#  [1, 1, 0, 1, 1, 1],
#  [1, 1, 0, 0, 2, 1]]


# parse_maze: file -> maze
# Recibe un archivo
# Devuelve un maze
def parse_maze(f):
    maze = []

    for line in f.readlines():
        line = line.strip("\n")

        maze.append(line.split(" "))

    return maze


# posible_action: maze (int, int) -> list((int, int))
# Recibe un maze una tupla de int
# Los elementos de la tuplas representan la fila y la columna dentro del
# laberinto
# Devuelve una lista de tuplas que representan las coordenadas a la cuales
# nos podemos mover
# Tenemos como prioridad devolver primero la posibilidades de mover hacia
# abajo o hacia la derecha. Luego consideramos a para arriba y la izquierda
def posible_action(maze, position):
    candidates = []
    size = len(maze)

    if (position[0] != size - 1 and
       maze[position[0] + 1][position[1]] != 1 and
       maze[position[0] + 1][position[1]] != -1):
        candidates.append((position[0] + 1, position[1]))

    if (position[1] != size - 1 and
       maze[position[0]][position[1] + 1] != 1 and
       maze[position[0]][position[1] + 1] != -1):
        candidates.append((position[0], position[1] + 1))

    if (position[0] != 0 and
       maze[position[0] - 1][position[1]] != 1 and
       maze[position[0] - 1][position[1]] != -1):
        candidates.append((position[0] - 1, position[1]))

    if (position[1] != 0 and
       maze[position[0]][position[1] - 1] != 1 and
       maze[position[0]][position[1] - 1] != -1):
        candidates.append((position[0], position[1] - 1))

    return candidates


# solve_maze: maze -> list((int, int))
# Recibe un maze
# Devuelve una lista con tuplas que representan coordenadas
# Esta lista contiene las coordenadas espesificas que resuelven el maze
def solve_maze(maze):
    solve = False
    situations = []
    actual_position = (0, 0)

    while not solve:
        candidates = posible_action(maze, actual_position)
        nActions = len(candidates)
        nSituations = len(situations)

        if (nActions > 1):
            maze[actual_position[0]][actual_position[1]] = -1
            situations.append(actual_position)
            actual_position = candidates[0]

        elif (nActions == 0):
            maze[actual_position[0]][actual_position[1]] = -1
            actual_position = situations[nSituations - 1]

        else:
            maze[actual_position[0]][actual_position[1]] = -1
            actual_position = candidates[0]

        element_in_maze = maze[actual_position[0]][actual_position[1]]
        if element_in_maze == 2:
            solve = True

    return situations

if __name__ == "__main__":
    print("Trabajo Practico Final")
    print("Bautista Marelli")

    done = False

    maze = [[0, 0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 2, 1]]

    print(solve_maze(maze))
    # while not done:
    #     print("Primero revise la documentacion sobre como ingresar el maze")

    #     filename = input(">>> Ingresa el nombre del archivo: ")
    #     try:
    #         with open(filename, "r") as f:
    #             maze = parse_maze

    #     except FileNotFoundError:
    #         print(colored("El archivo no existe!", color="red"))
        
    #     solve_maze(maze)
