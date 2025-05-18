# Comprecion de listas
# Ejemplo

row = []
for white_pawn in range(8):
    # suponiendo que cada numero es una pieza de ajedrez (WHITE_PAWN) y esta lista rellena 
    # una fila del ajedrez
    row.append(white_pawn) 

print(row)

# por compresion de lista

row = [white_pawn for white_pawn in range(8)]
print(row)


# arreglos de dos dimenciones

board = [] # seria un arreglo bidireccional o por terminos algegraicos una matriz 

for i in range(8):
    row = [empty for empty in range(8)]
    board.append(row)

print(board)

# Las listas por compresion tambien pueden ser anidadas
# La parte interna crea una fila, y la parte externa crea una lista de filas.
board = [[i for i in range(8)] for j in range(8)]
print(board)


# agragando las piezas al ajedrez

board[0][0] = "ROOK"
board[0][7] = "ROOK"
board[7][0] = "ROOK"
board[7][7] = "ROOK"
board[4][2] = "KNIGHT"
board[3][4] = "PAWN"

print(board)

# Naturaleza multidimensional de las listas
# en vertical representa el numero de filas
# en horizontal representa el numero de columnas

# supongamos que tienes que registrar la temperatura diariamente, cada una hora
# usamos compresion de lista h para las horas y d para los dias

temps = [[0.0 for h in range(24)] for d in range(31)]
print(temps)

# ahora determinaremos la temperatura promedio mensual del mediodia.
# para ello sumamos la temperatura del medio dia por los 31 dias y la dividimos por 31

total = 0.0

for day in temps: # day es una lista no un escalar
    total += day[11] # como day es una lista se accede al elemento a traves del indice

average = total / 31

print("Temperatura promedio al mediodia: ", average,"°C")

# ahora encuentra la temperatura mas alta de todo el mes

highest = -100.0

for day in temps: # itinera en todas las filas de la matriz
    for temp in day: # itinera en todas las mediciones tomadas en un dia
        if temp > highest: 
            highest = temp

print("La temperatura más alta fue: ", highest, "°C")

# Ahora cuenta los dias en que la temperatura al mediodia fue de al menos 20°C

hot_days = 0

for day in temps:
    if day[11] >= 20.0:
        hot_days += 1

print(hot_days, "fueron los dias calurosos.")

# ahora supongamos que tienes 3 edificios de 15 pisos cada uno y cada piso cuenta con 20 habitaciones
# representalo en una matriz o lista tridimencional
# ocupamos la compresion de lista y agregamos false a cada habitacion para indicar que esta desocupada
rooms = [[[False for h in range(20)] for p in range(15)] for h in range(3)]
print(rooms)

# verifica que x piso tiene habitaciones desocupadas

vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1

print("Habitaciones disponibles en edificio 2, piso 14: ", vacancy)

