#----------------------------------------------------
# Lab 3: Numerical Tic Tac Toe class
# 
# Author: Connor Li
# Collaborators: Whoever wrote the original lab3.py & lab3_NumTicTacToe.py
# References: None
#----------------------------------------------------

class NumTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3 # number of columns and rows of board
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
                
                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # TO DO: delete pass and print out formatted board
        # e.g. an empty board should look like this:
        #    0   1   2
        # 0    |   |
        #   -----------
        # 1    |   |
        #   -----------
        # 2    |   |


        # print the column numbers
        print("   ", end="")
        for i in range(self.size):
            print(f"{i}".ljust(4), end="")
        print()

        for i in range(self.size):
            firstelement = f"{self.board[i][0]}"
            if self.board[i][0] == 0:
                firstelement = firstelement.replace(str(0), ' ')
            string = [f"{i}".ljust(2 if self.size < 10 else 3) + firstelement.center(3)]
            for j in range(1, self.size):
                newelement = "|"+ f"{self.board[i][j]}".center(3)
                if self.board[i][j] == 0:
                    newelement = newelement.replace(str(0), ' ')
                string += newelement

            print("".join(string))
            # Account for dynamic size horizontally
            if i < self.size - 1:
                print("  " + "----" * (self.size))




    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        return False if self.board[row][col] > 0 else True
    
    
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        # TO DO: delete pass and complete method

        if self.squareIsEmpty(row, col):
            self.board[row][col] = num
            return True

        return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''

        full = True

        for row in self.board:
            for col in row:
                if col == 0:
                    full = False

        return full
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.


        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        # TO DO: delete pass and complete method

        # check for a 0 in any candidate before checking for a winner
        # check if any row adds up to 15
        # check if any column adds up to 15
        # check if either diagonal adds up to 15

        diagonal1 = (self.board[i][i] for i in range(self.size))
        if 0 not in (self.board[i][i] for i in range(self.size)):
            if sum(diagonal1) == 15:
                # checks if the sum of the diagonal from top left to bottom right is 15
                return True

        diagonal2 = (self.board[i][self.size - i - 1] for i in range(self.size))
        if 0 not in diagonal2:
            if sum(diagonal2) == 15:
                # checks if the sum of the diagonal from top right to bottom left is 15
                return True

        for row in self.board:
            if 0 not in row:
                if sum(row) == 15:
                    return True

        for col in range(self.size):
            column = [self.board[row][col] for row in range(self.size)]
            if 0 not in column:
                if sum(column) == 15:
                    return True

        return False
     

if __name__ == "__main__":
    # TEST EACH METHOD THOROUGHLY HERE
    # suggested tests are provided as comments, but more tests may be required
    # start by creating empty board and checking the contents of the board attribute
    myBoard = NumTicTacToe()
    print('Contents of board attribute when object first created:')
    print(myBoard.board)
    # does the empty board display properly?
    myBoard.drawBoard()
    # assign a number to an empty square and display
    print("assign a number to an empty square and display")
    print(myBoard.update(0, 0, 1))
    myBoard.drawBoard()
    # try to assign a number to a non-empty square. What happens?
    print("try to assign a number to a non-empty square. What happens?")
    print(myBoard.update(0, 0, 1))
    myBoard.drawBoard()
    # check if the board has a winner. Should there be a winner after only 1 entry?
    print("check if the board has a winner. Should there be a winner after only 1 entry?")
    myBoard.drawBoard()
    print(myBoard.isWinner())
    # check if the board is full. Should it be full after only 1 entry?
    print("check if the board is full. Should it be full after only 1 entry?")
    print(myBoard.boardFull())
    # add values to the board so that any line adds up to 15. Display
    print("add values to the board so that any line adds up to 15. Display")
    myBoard.update(1, 1, 9)
    myBoard.update(2, 2, 5)
    myBoard.drawBoard()
    # check if the board has a winner
    print("check if the board has a winner")
    print(myBoard.isWinner())
    # check if the board is full
    print("check if the board is full")
    print(myBoard.boardFull())
    # write additional tests, as needed
    print("Make board full, check if board is full")
    for row in range(myBoard.size):
        for col in range(myBoard.size):
            myBoard.board[row][col] = (row * myBoard.size) + col + 1
    myBoard.drawBoard()
    print(myBoard.boardFull())
    