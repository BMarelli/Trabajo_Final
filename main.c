#include <stdio.h>
#include <string.h>

// MODO DE USO:
// 

// El archivo a recibir (laberinto.txt) debe cumplir con ciertas características:
// - En la primera linea tiene que estar el tamaño que tendra el laberinto.
//   Primero es la cantidad de filas y luego la cantidad de columnas, separados por un espacio
// - Debe separar con titulos a las coordenadas que van a pasar.
//   Estos titulos tienen que ser los siguientes:
//      # MUROS:
//      # ESPACIOS:
//      # OBJETIVO:
//   Seguido de los titulos es importante que poner la cantidad de coordenadas que van a introducir
// - Cada linea representa una coordenada
// - Cada elemento de las coordenadas tienen que estar separadas por espacios
// - Importante! El archivo debe finalizar con un salto de línea
// Ejemplo: (archivo: laberinto.txt)
/*
    6 6
    # MUROS:
    22
    1 0
    1 1
    1 2
    1 4
    1 5
    2 0
    2 1
    2 2
    2 4
    2 5
    3 0
    3 1
    3 4
    3 5
    4 0
    4 1
    4 3
    4 4
    4 5
    5 0
    5 1
    5 5
    # OBJETIVO
    1
    5 4

*/
// TODO: Terminar parseFile
int parseFile(char filename){
    FILE * file;
    file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error: El archivo %s no existe!\n", filename);
        return 1;
    }

    char line[10];

    while(fgets(line, 9, file) != NULL) {
        if (strcmp(line, "# MUROS:\n")) {}
    }

    return 0;
}

int main() {

    return 0;
}
