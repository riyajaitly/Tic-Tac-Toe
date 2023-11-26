class Board:
    #constructor for class
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size**2)
        self.winner = ""

    #function to get the size
    def get_size(self):
        return len(self.board)

    def get_winner(self):
        #conditions check for winner in row
        if self.board[0] == self.board[1] == self.board[2] != " ":
            return self.board[1]
        elif self.board[3] == self.board[4] == self.board[5] != " ":
            return self.board[4]
        elif self.board[6] == self.board[7] == self.board[8] != " ":
            return self.board[7]
        #conditions check for winner in column
        elif self.board[3] == self.board[0] == self.board[6] != " ":
            return self.board[3]
        elif self.board[1] == self.board[4] == self.board[7] != " ":
            return self.board[4]
        elif self.board[2] == self.board[8] == self.board[5] != " ":
            return self.board[8]
        #conditions check for winner in diagonal
        elif self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[4]
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[4]

    #check if there is a tie
    def checkTie(self):
        for i in range(8):
            if (self.board[i]== ' '):
                return False
        return True

    #put the move on the board
    def set(self,cell,sign):
        self.board[cell] = sign

    #check if the cell is empty
    def isempty(self,cell):
        two_size = self.size**2
        for i in range(two_size):
            if self.board[i] != " ":
                return False

        return True

    #check if the game can end
    def isdone(self):
        done = False

       #conditions check for winner in row
        if self.board[0] == self.board[1] == self.board[2] != " ":
            done = True
        elif self.board[3] == self.board[4] == self.board[5] != " ":
            done = True
        elif self.board[6] == self.board[7] == self.board[8] != " ":
            done = True
        #conditions check for winner in column
        elif self.board[3] == self.board[0] == self.board[6] != " ":
            done = True
        elif self.board[1] == self.board[4] == self.board[7] != " ":
            done = True
        elif self.board[2] == self.board[8] == self.board[5] != " ":
            done = True
        #conditions check for winner in diagonal
        elif self.board[0] == self.board[4] == self.board[8] != " ":
            done = True
        elif self.board[2] == self.board[4] == self.board[6] != " ":
            done = True

        #check is if there is a tie
        elif (self.board[0] == "X" or self.board[0] == "O") and (self.board[1] == "X" or self.board[1] == "O") and (self.board[2] == "X" or self.board[2] == "O") and (self.board[3] == "X" or self.board[3] == "O") and (self.board[4] == "X" or self.board[4] == "O") and (self.board[5] == "X" or self.board[5] == "O") and (self.board[6] == "X" or self.board[6] == "O") and (self.board[7] == "X" or self.board[7] == "O") and (self.board[8] == "X" or self.board[8] == "O"):
             done = True


        return done

    #idsplay board
    def show(self):
        grid_board = [" A"," B"," C"]

        print("  ",end = "")
        print("\n")
        #display first column
        for thing in grid_board:
            print(thing,end = "  ")
        counter = 1
        #for rest of rows and columns
        for i in range(10):
            if i%3 == 0:
                print()
                print(" +---+---+---+")
                if i != 9:
                    print(f"{counter}",end="|")
                    counter += 1
            if i != 9:
                print(f" {self.board[i]} ",end = "|")
        #print("\n")
        