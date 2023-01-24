countPuz = 0


# prints the board to console
def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print("%2d" % board[i][j], end=" ")
        print()


def solve(board, n):
    global countPuz
    while n < 26:
        for row in range(5):
            for col in range(5):
                if isValid(board, row, col, n):
                    board[row][col] = n + 1
                    solve(board, n + 1)
                    board[row][col] = 0
        break
    if n == 25:
        printBoard(board)
        print("Puzzle is solved")
        countPuz += 1
        return True


def isValid(board, row, col, n):
    if board[row][col] != 0:
        return False
    try:
        if board[row + 2][col + 2] == n:  # checking top left diagonal move
            if 0 < (row + 2) < 5:
                if 0 < (col + 2) < 5:
                    # print("valid top left move")
                    return True
    except IndexError:
        pass
    try:
        if board[row + 2][col - 2] == n:  # checking top right diagonal move
            if 0 <= (row + 2) < 5:
                if 0 <= (col - 2) < 5:
                    # print("valid top right move")
                    return True
    except IndexError:
        pass
    try:
        if board[row - 2][col + 2] == n:  # checking bottom left diagonal move
            if 0 <= (row - 2) < 5:
                if 0 <= (col + 2) < 5:
                    # print("valid bottom left move")
                    return True
    except IndexError:
        pass
    try:
        if board[row - 2][col - 2] == n:  # checking bottom right diagonal move
            if 0 <= (row - 2) < 5:
                if 0 <= (col - 2) < 5:
                    # print("valid bottom right move")
                    return True
    except IndexError:
        pass
    try:
        if board[row + 3][col] == n:  # checking line up move
            if 0 <= (row + 3) < 5:
                if 0 <= (col) < 5:
                    # print("valid line up move")
                    return True
    except IndexError:
        pass
    try:
        if board[row - 3][col] == n:  # checking line down move
            if 0 <= (row - 3) < 5:
                if 0 <= (col) < 5:
                    # print("valid line down move")
                    return True
    except IndexError:
        pass
    try:
        if board[row][col + 3] == n:  # checking line left move
            if 0 <= (row) < 5:
                if 0 <= (col + 3) < 5:
                    # print("valid line left move")
                    return True
    except IndexError:
        pass
    try:
        if board[row][col - 3] == n:  # checking line right move
            if 0 <= (row) < 5:
                if 0 <= (col - 3) < 5:
                    # print("valid line right move")
                    return True
    except IndexError:
        pass
    return False


def solveBoard():
    global countPuz
    board = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    printBoard(board)

    # for i in range(5):
    # for j in range(5):
    #  isValid(board,i,j,2)
    solve(board, 1)
    print("Number of solutions: ", countPuz)


solveBoard()
