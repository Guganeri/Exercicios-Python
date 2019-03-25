#Desafio Udemy criação do Jogo da Velha em Python
import random
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
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player1: Você quer ser X ou O?').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[9] == mark and board[8] == mark and board[7]==mark ) or #VÍTORIA PELO TOPO
            (board[4] == mark and board[5] == mark and board[6]) or        #PELO MEIO
            (board[3] == mark and board[2] == mark and board[1]) or        #POR BAIXO
            (board[7] == mark and board[4] == mark and board[1]) or        #Esquerda
            (board[8] == mark and board[5] == mark and board[2]) or        #Direita
            (board[7] == mark and board[5] == mark and board[3]) or        #Diagonal
            (board[9] == mark and board[5] == mark and board[1])           #Diagonal
    )
def chose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    pass

def space_check(board,position):

    return board[position] == ' '

def full_board_check(board):
    for i in range (0,10):
        if space_check(board, i):
            return False

    return True

def player_choice(board):
    position = ' '
    while position not in '1, 2, 3, 4, 5, 6, 7, 8, ,9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9) ')

    return int(position)

def replay():

    return input('Quer jogar novamente? "sim" ou "nao" '.lower().startswith('s'))

print('Bem vindo ao Jogo da Velha !!')

while True:
    board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = chose_first()
    print(turn+' começa!')

    game_on = True

    if turn == 'Player 1':
        #Vez do jogador 1 !!
        display_board(board)
        position = player_choice(board)
        place_marker(board, player1_marker, position)

        #Checar Vitória
    if win_check(board, player1_marker):
        display_board(board)
        print('Parabéns! Você Venceu !! ')
        game_on = False
    else:
        if full_board_check(board):
            display_board(board)
            print('Empate!')
            break
        else:
            turn = 'Player 2'

    #Vez do jogador 2 !!
    if turn == 'Player 2':
        display_board(board)
        position = player_choice(board)
        place_marker(board, player2_marker, position)
    #Checar vitoria
    if win_check(board, player2_marker):
        display_board(board)
        print('Parabéns! você venceu!')
        game_on = False
    else:
        if full_board_check(board):
            display_board(board)
            print('Empate')
            break
        else:
            turn = 'Player 1'

    if not replay():
        break
