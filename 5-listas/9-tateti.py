tablero = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

for i in range(9):

    for j in range(3):
        print(tablero[j])
    print("-------------------")

    print(f"Jugador {(i%2)+1}:")
    x = input("Coordenada x:")
    y = input("Coordenada y:")
    x = int(x)
    y = int(y)

    if (i % 2) == 0:
        tablero[x][y] = "X"
    else:
        tablero[x][y] = "O"