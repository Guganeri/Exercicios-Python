#Desafio Udemy criação do Jogo da Velha em Python
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('   |   |   ')
    print(' '+board[7]+' | '+board[8]+' | '+board[9])
    print('   |   |   ')
    print('-------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-------------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    pass
def player_input():
    input()
    market = ''
    while not (market == 'X' or market == 'O'):
        market = input('Player1: Você quer ser X ou O?').upper()
    if market == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def placa_marker(board, marker, position):
    board[position] = marker



display_board([" ", " "," ", " ", " "," ", " "," ", " ", " "])