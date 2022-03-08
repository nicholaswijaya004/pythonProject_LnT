from tkinter import HIDDEN
from random import randint

def menu():
    print('Welcome to Battleship game!!')
    print('1. Play Game')
    print('2. Game Information')
    print('3. Copyright')
    print('4. Exit Game')
    choice = input('Choose Menu: ')
    if choice == "1":
        gameplay()
    elif choice == "2":
        info()
    elif choice == "3":
        copyright()
    elif choice == "4":
        print("Thanks for playing this game!! Hope it'll make your day")
        quit()
    else:
        print('Choose the right number based on the menu')
        menu()

def copyright():
    print('Code made by Nicholas Daniel Wijaya')
    print('Made for LnT Subdivision Regeneration Project Meet 4 Task')

def info():
    print('Symbol mean:')
    print('-: bracket / place already guessed')
    print('X: Target hit / hit a ship')
    print("' ': Available space")


HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
GUESS_BOARD = [[' '] * 8 for x in range(8)]

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    print(' |A|B|C|D|E|F|G|H|')
    print('------------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1
    print('------------------')


def board():
    pass

def create_ships(board):
    for ship in range(5):
        ship_row, ship_col = randint(0,7), randint(0,7)
        while board[ship_row][ship_col] == 'X':
            ship_row, ship_col = randint(0,7), randint(0,7)
        board[ship_row][ship_col] = 'X'

def get_ship_location():
    row = input('Please enter ship row [1-8]: ')
    while row not in '12345678':
        print('Please enter a valid row')
        row = input('Please enter ship row [1-8]: ')
    column = input('Please enter ship column [A-H]: ').upper()
    while column not in 'ABCDEFGH':
        print('Please enter a valid column')
        column = input('Please enter ship column [A-H]: ')
    return int(row)-1, letters_to_numbers[column]

def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

def gameplay():
    create_ships(HIDDEN_BOARD)
    turns = 10
    print_board(HIDDEN_BOARD)
    print_board(GUESS_BOARD)
    while turns > 0:
        if turns == 10:
            print('Welcome to Battleship')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == '-':
            print('You already guessed that')
        elif HIDDEN_BOARD[row][column] == 'X':
            print('Congratulations! You have hit the battleship')
            GUESS_BOARD[row][column] = 'X'
            turns -= 1
        else:
            print('Sorry you missed')
            GUESS_BOARD[row][column] = '-'
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print('Congratulations, you have sunk all the battleships')
            break
        print('You have ' + str(turns) + ' turns remaining')
        if turns == 0:
            print('Sorry you have lost, Game Over')
            break
    menu()

menu()
