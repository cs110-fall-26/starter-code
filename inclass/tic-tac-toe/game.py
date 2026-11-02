def num_input(prompt):
    while True:
        choice = input(prompt)
        if choice.isdigit():
            return int(choice)
        print("Not a number, try again")

def print_board(board):
    for row in board:
        for col in row:
            print(col, end=" ")
        print()


def setup():
    board = []
    # TODO Setup the board to add each row as its own list
    # Each row should contain an "_" for each column
    return board

def can_mark(board, row, col):
    # TODO Check if the position at that row and column is unmarked yet. Return True if unmarked, False otherwise
    return False

def mark_pos(board, row, col, marker):
    # TODO Given the position is available, mark the location 
    return 

def check_horizontal(board):
    # TODO Check if there is a horizontal win; if there is a winner, return the winner.
    return None

def check_vertical(board):
    # TODO Check if there is a vertical win; if there is a winner, return the winner.
    return None 

def check_diagonal(board):
    # TODO Check if there is a diagonal win; if there is a winner, return the winner.
    return None

def check_tie(board):
    # TODO Check if a tie occurred, return True if a tie happened
    return False

def main():
    board = setup()
    players = ["x", "o"]
    for turn in range(9):
        pass

    # TODO Print out the board using the `print_board` function and pass in the board itself.
    
    # TODO Print out who's turn it is : If the turn is even, player 1 will go. If the turn is odd, player 2 will go.
    # TODO Ask user input for row and column
    # TODO Check if input values are valid, should be within the range of 0-2 for row and column.
    # TODO Check if position can be marked, mark the position if possible. 
    # TODO If position is already taken or invalid, ask the user to enter a valid location
    # TODO After each turn, check if a win has occurred.
    # TODO If a win has occurred, stop the game and print out who won or whether a tie happened.


if __name__ == "__main__":
    main()

