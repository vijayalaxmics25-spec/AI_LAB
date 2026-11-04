board = [" "] * 9

def display():
    print()
    for i in range(0, 9, 3):
        print("|".join(board[i:i+3]))
        if i < 6:
            print("-----")

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for w in wins:
        if all(board[i] == player for i in w):
            return True
    return False

def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if " " not in board:
        return 0

    if is_max:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

def computer_move():
    best = -100
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"

print("TIC TAC TOE")
print("You are X, Computer is O")

while True:
    display()

    pos = int(input("Enter position (1-9): ")) - 1

    if pos < 0 or pos > 8 or board[pos] != " ":
        print("Invalid position! Try again.")
        continue

    board[pos] = "X"

    if check_winner("X"):
        display()
        print("You win!")
        break

    if " " not in board:
        display()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        display()
        print("Computer wins!")
        break

    if " " not in board:
        display()
        print("It's a draw!")
        break