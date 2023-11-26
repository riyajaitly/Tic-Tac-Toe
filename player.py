#player class
from audioop import minmax
from random import choice, sample, randint, randrange
from multiprocessing.util import log_to_stderr
from shutil import move
#from this import s
from turtle import pos


class Player:
    #constructor for class
    def __init__(self,name,sign):
        self.name = name
        self.sign = sign

    #defining accessor methods
    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def choose(self,board):
        #dictionary which stores the values of cell
        s = {"A1":0 , "A2" :3,"A3" :6 ,"B1":1 , "B2" :4,"B3" :7,"C1": 2, "C2" :5,"C3" :8}
        while True:
            print("\n")
            #giving error
            cell = input(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
            #check for the validation of the cell
            if cell not in s:
                print("The given input is incorrect. Please rewrite")
                continue
            #determine the value of the cell
            cell = s[cell]
            if cell >= 0 and cell < 9 and board.board[cell] == " ":
                #calling the function to set the sign
                board.set(cell,self.sign)
                break
            else:
                print("\nYou did not choose correctly.")
    
    

class AI(Player):
    def __init__(self,name,sign,board):
        self.name = name
        self.sign = sign
        self.board = board
    
    #defining accessor methods
    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name
    
    def get_board(self):
        return self.board

    def choose(self,board):
        x = 1
        #dictionary to store the values of cell
        s = {"A1":0 , "A2" :3,"A3" :6 ,"B1":1 , "B2" :4,"B3" :7,"C1": 2, "C2" :5,"C3" :8}
        while x == 1:
            cell = randint(0,8)
            if cell >= 0 and cell < 9 and board.board[cell] == " ":
                #calling the function to set the sign
                board.set(cell,self.sign)
                x = 0
                break
            else:
                x = 1

class MiniMax(AI):
    def choose(self, board):
        minmaxscore = -1000
        right_move = 0
        for i in range(9):
            if (board.board[i] == " "):
                board.board[i] = self.sign
                score = MiniMax.minimax(self, board, False)
                board.board[i] = " "
                if (score > minmaxscore):
                    minmaxscore = score
                    right_move = i
                             
        cell = right_move
        board.set(cell, self.sign)

    
    def minimax(self, board, self_player):
        #allows all players to get a chance to play
        if self.sign == "X":
            other_sign = "O"
        else:
            other_sign = "X"

        #determines which player is winner
        if (board.get_winner() == self.sign):
            return 1
        elif (board.get_winner() == other_sign):
            return -1
        elif (board.checkTie()):
            return 0
        #maximizing part
        if (self_player):
            minmaxscore = -1000
            for i in range(9):
                if (board.board[i] == " "):
                        board.board[i] = self.sign
                        score = MiniMax.minimax(self, board, False)
                        board.board[i] = " "
                        if (score > minmaxscore):
                            minmaxscore = score

            return minmaxscore
            
        #minimizing part
        else:
            minmaxscore = 1000
            for i in range(9):
                if (board.board[i] == " "):
                    board.board[i] = other_sign
                    score = MiniMax.minimax(self, board, True)
                    board.board[i] = " "
                    if (score < minmaxscore):
                        minmaxscore = score

            return minmaxscore

