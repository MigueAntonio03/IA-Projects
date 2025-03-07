def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows, columns and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Turno del jugador {current_player}. Elige fila y columna (0, 1, 2):")
        
        try:
            row = int(input("Fila: "))
            col = int(input("Columna: "))
            
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                print("Movimiento no válido, intenta de nuevo.")
                continue
            
            board[row][col] = current_player
            
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"¡El jugador {winner} ha ganado!")
                break
            
            if is_full(board):
                print_board(board)
                print("¡Es un empate!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        except ValueError:
            print("Por favor, ingresa números válidos.")
        except IndexError:
            print("Por favor, elige una fila y columna entre 0 y 2.")

if __name__ == "__main__":
    tic_tac_toe()
