PLAYER_ONE = "X"
PLAYER_TWO = "O"
PLAYER_NONE = " "
TIE = "TIE"


def game():
  board = [PLAYER_NONE for i in range(9)]
  number_grid = [str(i) for i in range(1, 10)]
  draw_board(number_grid)
  print("notaðu númerinn hérna fyrir ofan til að velja reit")
  winner = check_if_game_is_over_loops(board)
  player_one = True
  while winner == PLAYER_NONE:
    answer = input("\n reitur: ")
    if answer not in number_grid:
      print("notaðu númer frá 1-9 og nota tölu sem hefur verið notuð")
      continue
    if player_one == True:
      board[int(answer) - 1] = PLAYER_ONE
      player_one = False
    else:
      board[int(answer) - 1] = PLAYER_TWO
      player_one = True
    number_grid.remove(answer)
    draw_board(board)
    winner = check_if_game_is_over_loops(board)
  if winner == TIE:
    print("jafntefli")
  else:
    print(winner + " er sigurvegarinn")
    
def draw_board(board):
  print(f" {board[0]} | {board[1]} | {board[2]}")
  print("-----------")
  print(f" {board[3]} | {board[4]} | {board[5]}")
  print("-----------")
  print(f" {board[6]} | {board[7]} | {board[8]}")

# ekki þetta
def check_if_game_is_over(board):
  # check if either player has won and return the player that won
  # check if 1st square is not empty
  if board[0] != PLAYER_NONE:
    # check if 1st row is matching
    if board[0] == board[1] == board[2]:
      return board[0]
    # check if 1st column is matching
    if board[0] == board[3] == board[6]:
      return board[0]
    # check if left diagonal is matching
    if board[0] == board[4] == board[8]:
      return board[0]
  # check if 2nd column is matching
  if board[1] == board[4] == board[7] != PLAYER_NONE:
    return board[1]
  # check if 3rd square is not empty
  if board[2] != PLAYER_NONE:
    # check if 3rd column is matching 
    if board[2] == board[5] == board[8]:
      return board[2]
    # check if right diagonal is matching
    if board[2] == board[4] == board[6]:
      print("win")

      return board[2]
  # check if 2nd row is matching
  if board[3] == board[4] == board[5] != PLAYER_NONE:
    return board[3]
  # check if 3rd row is matching
  if board[6] == board[7] == board[8] != PLAYER_NONE:
    return board[6]
  # check if the game has tied
  if PLAYER_NONE not in board:
    return TIE
  # the game is not finished
  return PLAYER_NONE

def check_if_game_is_over_loops(board):
  # check rows
  for i in range(3):
    if board[0 + 3 * i] == board[1 + 3 * i] == board[2 + 3 * i] != PLAYER_NONE:
      return board[0 + 3 * i]
  # check columns
  for i in range(3):
    if board[0 + i] == board[3 + i] == board[6 + i] != PLAYER_NONE:
      return board[0 + i]
  # check diagonal
  for i in range(2):
    if board[0 + 2 * i] == board[4] == board[8 - 2 * i] != PLAYER_NONE:
      return board[4]
  # check if the game has tied
  if PLAYER_NONE not in board:
    return TIE
  # the game is not finished
  return PLAYER_NONE



if __name__ == "__main__":
  game()