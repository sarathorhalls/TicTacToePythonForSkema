# búum til fall sem prentar út borðið
def draw_board(board):
  print(" " + board[0] + " | " + board[1] + " | " + board[2] + " ") # 1 | 2 | 3
  print("-----------")                                              #-----------
  print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ") # 4 | 5 | 6
  print("-----------")                                              #-----------
  print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ") # 7 | 8 | 9

# búum til fall sem athugar hvort einhver hafi unnið fyrir gefið borð
def check_if_game_is_over(board):
  # athuga raðir (rows)
  for i in range(3):
    if board[0 + 3 * i] == board[1 + 3 * i] == board[2 + 3 * i] != " ":
      return board[0 + 3 * i]
  # athuga dálka (columns)
  for i in range(3):
    if board[0 + i] == board[3 + i] == board[6 + i] != " ":
      return board[0 + i]
  # asthuga skálínur (diagonal)
  for i in range(2):
    if board[0 + 2 * i] == board[4] == board[8 - 2 * i] != " ":
      return board[4]
  # athuga hvort upp hafi komið jafntefli
  if " " not in board:
    return "TIE"
  # ef við endum hérna þá er leikurinn ekki búin
  return " "

# búum til nýtt borð með tómum reitum
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
# búum til borð með tölum á og prentum það fyrir tutorial
number_grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
draw_board(number_grid)
print("notaðu númerinn hérna fyrir ofan til að velja reit")
# núll stillum winner
winner = check_if_game_is_over(board)
# notum boolean gildi til að halda utan um hver á að gera
player_one = True
# búum til while lykkju sem keyrir þangað til að leikurinn er búinn
while winner == " ":
  # spyrjum notandan um hvaða reit notandinn vill nota á borðinu
  answer = input("\n reitur: ")
  # ef notandinn svarar ekki með tölu frá 1 til 9 sem er ekki búið að nota 
  # spyrjum við aftur með continue skipun
  if answer not in number_grid:
    print("notaðu númer frá 1-9 og nota tölu sem hefur verið notuð")
    continue
  # setjum X eða O á borðið miðað við hver er að gera og breytum síðan bool gildinu
  if player_one == True:
    board[int(answer) - 1] = "X"
    player_one = False
  else:
    board[int(answer) - 1] = "O"
    player_one = True
  # tökum númerið burt af listanum af leyfilegum númerum fyrir if á línu 45
  number_grid.remove(answer)
  # teiknum nýja borðið
  draw_board(board)
  # athugum hvort einhver hafi unnið
  winner = check_if_game_is_over(board)
  # leikurinn endar sjálkrafa því winner er ekki lengur " "

# athugum síðan hvort leikurinn hafi endað í jafntefli eða ekki og prentum
# niðurstöður 
if winner == "TIE":
  print("jafntefli")
else:
  print(winner + " er sigurvegarinn")
