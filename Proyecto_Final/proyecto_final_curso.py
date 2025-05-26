from random import randrange

# Para mostrar el tablero
def display_board(board):
    print("\n######## Tablero ########")
    print("+-------" * 3, "+", sep="")
    for row in range(3): # Se itinera por cada fila
        print("|       " * 3, "|", sep="")
        for col in range(3): # Se itinera por cada columna
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

# Registramos el movimiento del usuario
def enter_move(board):
    while True:
        move = input("Ingresa tu movimiento (1 a 9): ")
        if not move.isdigit(): # verificamos si la entrada no es un numero
            print("Entrada inválida. Ingresa un número del 1 al 9.")
            continue
        move = int(move)
        if move < 1 or move > 9: # validamos que este en el rango de 1 a 9
            print("Movimiento fuera de rango. Debe estar entre 1 y 9.")
            continue
        # calculamos la fila y la columna segun el numero del movimiento dado
        row = (move - 1) // 3
        col = (move - 1) % 3
        if board[row][col] in ['o', 'x']: # verificamos si la celda esta ocupada
            print("¡Cuadro ocupado! Intenta otra posición.")
        else:
            board[row][col] = 'o' # si la celda esta libre se regista el movimiento del usuario
            break

# funcion para geneerar una lista de celdas libres
def make_list_of_free_fields(board):
    # retornamos una lista de tuplas con las coordenadas de cada celda libre
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] not in ['o', 'x']]

# función para verificar si hay un ganador
def victory_for(board, symbol):
    lines = [
         # Filas
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columnas
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonales
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for line in lines:
        if all(board[r][c] == symbol for r, c in line): # Si todas las celdas de la línea tienen el mismo símbolo
            return 'you' if symbol == 'o' else 'me' # retornamos ganador (usuario o maquina)
    return None # si no hay ganador se retorna none

# función para realizar el movimiento de la máquina
def draw_move(board):
    free = make_list_of_free_fields(board) # optenemos las celdas libres
    if free: # si hay cledas disponibles
        row, col = free[randrange(len(free))]
        board[row][col] = 'x'

board = [[row * 3 + col + 1 for col in range(3)] for row in range(3)]
board[1][1] = 'x' # el primer movimiento de la maquina (en el centro del tablero)

human_turn = True # Inicia el turno del usuario
victor = None # variable para guardar al ganador

while True:
    display_board(board) # Mostramos el tablero
    if human_turn:
        enter_move(board) # el usuario realiza su movimiento
        victor = victory_for(board, 'o') # verificamos si el usuario gano
    else:
        draw_move(board) # la maquina realiza su movimiento
        victor = victory_for(board, 'x') # verificamos si la maquina gano
    if victor is not None or not make_list_of_free_fields(board): # si hay ganador o empate
        break
    human_turn = not human_turn # Cambiamos de turno


display_board(board)

if victor == 'you':
    print("¡Has ganado!")
elif victor == "me":
    print("¡He ganado!")
else:
    print("¡Empate!")