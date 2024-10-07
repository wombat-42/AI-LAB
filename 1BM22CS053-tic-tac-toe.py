import random

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def check_winner(board, mark):
    for row in board:
        if all([spot == mark for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == mark for row in range(3)]):
            return True
    if all([board[i][i] == mark for i in range(3)]) or all([board[i][2-i] == mark for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([spot != " " for row in board for spot in row])

def get_available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def ai_move(board):
    available_moves = get_available_moves(board)
    
    for move in available_moves:
        board[move[0]][move[1]] = "O"
        if check_winner(board, "O"):
            return
        board[move[0]][move[1]] = " "
    
    for move in available_moves:
        board[move[0]][move[1]] = "X"
        if check_winner(board, "X"):
            board[move[0]][move[1]] = "O"
            return
        board[move[0]][move[1]] = " "
    
    if board[1][1] == " ":
        board[1][1] = "O"
        return
    
    for move in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        if board[move[0]][move[1]] == " ":
            board[move[0]][move[1]] = "O"
            return
    
    move = random.choice(available_moves)
    board[move[0]][move[1]] = "O"

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = True

    while True:
        print_board(board)

        if player_turn:
            while True:
                try:
                    row = int(input("Enter row (0, 1, 2): "))
                    col = int(input("Enter column (0, 1, 2): "))
                    
                    if row not in [0, 1, 2] or col not in [0, 1, 2]:
                        print("Invalid input! Please enter numbers between 0, 1, or 2.")
                        continue
                    
                    if board[row][col] == " ":
                        board[row][col] = "X"
                        break
                    else:
                        print("Invalid move! That spot is already taken.")
                except ValueError:
                    print("Invalid input! Please enter valid integers for row and column.")
        else:
            ai_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("Player wins!")
            break
        elif check_winner(board, "O"):
            print_board(board)
            print("AI wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        player_turn = not player_turn

if __name__ == "__main__":
    play_game()

OUTPUT


 | | 
-----
 | | 
-----
 | | 
-----
Enter row (0, 1, 2): 0
Enter column (0, 1, 2): 0
X| | 
-----
 | | 
-----
 | | 
-----
X| | 
-----
 |O| 
-----
 | | 
-----
Enter row (0, 1, 2): 2
Enter column (0, 1, 2): 2
X| | 
-----
 |O| 
-----
 | |X
-----
X| |O
-----
 |O| 
-----
 | |X
-----
Enter row (0, 1, 2): 2
Enter column (0, 1, 2): 3
Invalid input! Please enter numbers between 0, 1, or 2.
Enter row (0, 1, 2): 1
Enter column (0, 1, 2): 2
X| |O
-----
 |O|X
-----
 | |X
-----
X| |O
-----
 |O|X
-----
O| |X
-----
AI wins!