def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("-" * 13)
    for i, fila in enumerate(tablero, start=1):
        print("|", end="")
        for j, valor in enumerate(fila, start=1):
            print(f" {valor} |", end="")
        print("\n" + "-" * 13)

def validar_movimiento(tablero, fila, columna):
    return 1 <= fila <= 3 and 1 <= columna <= 3 and tablero[fila - 1][columna - 1] == " "

def realizar_movimiento(tablero, fila, columna, simbolo):
    tablero[fila - 1][columna - 1] = simbolo

def comprobar_ganador(tablero, simbolo):
    for i in range(3):
        if all(tablero[i][j] == simbolo for j in range(3)) or all(tablero[j][i] == simbolo for j in range(3)):
            return True
    return all(tablero[i][i] == simbolo for i in range(3)) or all(tablero[i][2 - i] == simbolo for i in range(3))

def comprobar_empate(tablero):
    return all(tablero[i][j] != " " for i in range(3) for j in range(3))

def jugar_tres_en_linea():
    print("==================================")
    print(" Tres en Línea (Tic Tac Toe) Game ")
    print("          Designed by 4leX-42      ")
    print("==================================\n")

    tablero = crear_tablero()
    mostrar_tablero(tablero)

    nombre_jugador1 = input("Ingrese el nombre del Jugador 1: ")
    nombre_jugador2 = input("Ingrese el nombre del Jugador 2: ")

    jugadores = [nombre_jugador1, nombre_jugador2]
    simbolos = ["X", "O"]

    turno = 0

    while True:
        jugador_actual = jugadores[turno % 2]

        print(f"\nTurno de {jugador_actual}")
        fila = int(input("Introduce la fila (1, 2 o 3): "))
        columna = int(input("Introduce la columna (1, 2 o 3): "))

        if validar_movimiento(tablero, fila, columna):
            realizar_movimiento(tablero, fila, columna, simbolos[turno % 2])
            mostrar_tablero(tablero)

            if comprobar_ganador(tablero, simbolos[turno % 2]):
                print(f"¡Enhorabuena! {jugador_actual} ha ganado el juego.")
                break
            elif comprobar_empate(tablero):
                print("El juego ha terminado en empate.")
                break

            turno += 1
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")

if __name__ == "__main__":
    jugar_tres_en_linea()