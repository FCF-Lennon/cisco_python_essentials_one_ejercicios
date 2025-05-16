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