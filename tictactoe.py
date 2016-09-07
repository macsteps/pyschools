#!/usr/bin/env python

def check_horizontal(player, moves):
  for i in range(0, 3):
    if moves[i][0] == player and moves[i][1] == player and moves[i][2] == player:
      return "'%s' wins (horizontal)." % player

def check_vertical(player, moves):
  for i in range(0, 3):
    if moves[0][i] == player and moves[1][i] == player and moves[2][i] == player:
      return "'%s' wins (vertical)." % player

def check_diagonal(player, moves):
  #print "%s %s %s" % (moves[2][0], moves[1][1], moves[0][2])
  if moves[0][0] == player and moves[1][1] == player and moves[2][2] == player:
    return "'%s' wins (diagonal)." % player
  elif moves[2][0] == player and moves[1][1] == player and moves[0][2] == player:
      return "'%s' wins (diagonal)." % player


def tictactoe(moves):
  players = ['X', 'O']
  for player in players:
    hor = check_horizontal(player, moves)
    if hor != None:
      return hor
      break
    ver = check_vertical(player, moves)
    if ver != None:
      return ver
      break
    dia = check_diagonal(player, moves)
    if dia != None:
      return dia
      break
  return "Draw."

print tictactoe([('X', ' ', 'O'), 
                   (' ', 'O', 'O'), 
                   ('X', 'X', 'X') ])
#    "'X' wins (horizontal)."
print tictactoe([('X', 'O', 'X'), 
                ('O', 'X', 'O'), 
                ('O', 'X', 'O') ])
#    'Draw.'
print tictactoe([('X', 'O', 'O'), 
                ('X', 'O', ' '), 
                ('O', 'X', ' ') ])
#    "'O' wins (diagonal)."
print tictactoe([('X', 'O', 'X'), 
                ('O', 'O', 'X'), 
                ('O', 'X', 'X') ])
#    "'X' wins (vertical)."
