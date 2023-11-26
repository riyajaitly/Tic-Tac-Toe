from board import Board
#giving error
from player import MiniMax, Player, AI

'''Only one player 1 and one player 2 should be uncommented at all times'''
# main program
print("Welcome to TIC-TAC-TOE Game!")
while True:
    board = Board()
    '''Normal Player'''
    player1 = Player("Bob","X")
    '''Uncomment the line below to make player 1 a computer player'''
    #player1 = AI("Bob", "X", board)
    '''Uncomment the line below to make player 1 use backtracking algorithm 
    (minimax) which is used in decision making and game theory to find the
     optimal move for a player, assuming that your opponent also plays 
     optimally'''
    #player1 = MiniMax("Bob", "X", board)
    '''Normal Player'''
    player2 = Player("Alice","O")
    '''Uncomment the line below to make player 2 a computer player'''
    #player2 = AI("Alice", "O", board)
    '''Uncomment the line below to make player 2 use backtracking algorithm 
    (minimax) which is used in decision making and game theory to find the
     optimal move for a player, assuming that your opponent also plays 
     optimally'''
    #player2= MiniMax("Alice", "O", board)

    turn = True
    while True:
        board.show()
        print("\n")
        count = 0
        if turn :
            player1.choose(board)
            turn = False
        else:
            #board.show()
            player2.choose(board)
            turn = True

        if board.isdone():
            break

    board.show()
    if board.get_winner() == player1.get_sign():
        print("\n")
        #giving error
        #print(f"\n{player1.get_name()} is a winner!")
        print("\n" + str(player1.get_name()) + " is a winner!")
    elif board.get_winner() == player2.get_sign():
        print("\n")
        #giving error
        #print(f"\n{player2.get_name()} is a winner!")
        print("\n" + str(player2.get_name()) + " is a winner!")
    else:
        print("\n")
        print("\nIt is a tie!")
    ans = input("Would you like to play again? [Y/N]").upper()
    if ans == "N":
        break

print("\nGoodbye!")

