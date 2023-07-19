import random

BOARD_LENGTH = 6
BOARD_LETTERS = "ABCDEF"

def draw_board(board):
    for i in range(1, BOARD_LENGTH + 1):
        print("  " + str(i), end=" ") 
    print()
    for letter in BOARD_LETTERS:
        pos = (ord(letter) - 65) * BOARD_LENGTH
        print(letter, end="")
        for number in range(BOARD_LENGTH):
            print(" " + board[pos + number], end=" |")
        print(">")
    

def get_number_from_position(position):
    letter = ord(position[0]) - 65
    number = int(position[1]) - 1
    return number + letter * BOARD_LENGTH 

def start_game():
    board = []

    for i in range(36):
        board.append(" ")

    draw_board(board)

    choices = []

    for number in range(1, BOARD_LENGTH + 1):
        for letter in BOARD_LETTERS:
            choices.append(letter + str(number))

    possible_choices = choices.copy()    

    computer_choices = []

    for i in range(3):
        choice = random.choice(choices)
        # to not allow the computer to select the same choice twice
        while choice in computer_choices:
            choice = random.choice(choices)
        computer_choices.append(choice)

    print("Velkominn í Battle Ships")
    print("Þú hefur þrjú skip, tvö lítil tveggja reita skip og eitt þriggja reita skip")
    # Skip 1
    setja_skip = ""
    while setja_skip not in possible_choices:
        print("notaðu bara lausa reiti frá 1 til " + BOARD_LETTERS[-1] + str(BOARD_LENGTH))
        setja_skip = input("til að setja skip skaltu skrifa stafinn og svo tölunna td (A4, E3, etc) byrjum á litla skipinu, ekki velja " + BOARD_LETTERS[-1] + " dálkinn  val: ")
    skip_pos = get_number_from_position(setja_skip)
    board[skip_pos] = "S"
    board[skip_pos + 1] = "S"
    possible_choices.remove(setja_skip)
    possible_choices.remove(choices[skip_pos + 1])
    draw_board(board)

    # Skip 2
    setja_skip = ""
    while setja_skip not in possible_choices:
        print("notaðu bara lausa reiti frá 1 til " + BOARD_LETTERS[-1] + str(BOARD_LENGTH))
        setja_skip = input("til að setja skip skaltu skrifa stafinn og svo tölunna td (A4, E3, etc) nú hitt litla skipið, ekki velja " + str(BOARD_LENGTH) + " röðina  val: ")
    skip_pos = get_number_from_position(setja_skip)
    board[get_number_from_position(setja_skip)] = "S"
    board[get_number_from_position(setja_skip) + BOARD_LENGTH] = "S"
    draw_board(board)

    # Skip 3
    setja_skip = ""
    while setja_skip not in possible_choices:
        print("notaðu bara lausa reiti frá 1 til " + BOARD_LETTERS[-1] + str(BOARD_LENGTH))
        setja_skip = input("til að setja skip skaltu skrifa stafinn og svo tölunna td (A4, E3, etc) byrjum á litla skipinu, ekki velja " + BOARD_LETTERS[-2] + " og " + BOARD_LETTERS[-1] + " dálkinn  val: ")
    board[get_number_from_position(setja_skip)] = "S"
    board[get_number_from_position(setja_skip) + BOARD_LENGTH] = "S"
    board[get_number_from_position(setja_skip) + BOARD_LENGTH * 2] = "S"
    draw_board(board)

    print("þá erum við tilbúin að byrja")
    return board, computer_choices


def game():
    board, computer_choices = start_game()

game()