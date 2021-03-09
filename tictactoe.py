import numpy as np


board=['_','_','_','_','_','_','_','_','_']

   
def choose(pos,player_symbol):
     if board[pos-1]=='_':
          board[pos-1]=player_symbol
          board_display()
def tie(palyer):
     result=1
     if ((board[0] != player and board[0] == player) and 
         (board[1] != player and board[1] == player) and  
         (board[2] != player and board[2] == player)):
          result+=1
     if ((board[3] != player and board[3] == player) and 
         (board[4] != player and board[4] == player) and  
         (board[5] != player and board[5] == player)):
          result+=1
     if ((board[6] != player and board[6] == player) and 
         (board[7] != player and board[7] == player) and  
         (board[8] != player and board[8] == player)):
          result+=1   
     if ((board[0] != player and board[0] == player) and 
         (board[3] != player and board[3] == player) and  
         (board[6] != player and board[6] == player)):
          result+=1
     if ((board[1] != player and board[1] == player) and 
         (board[4] != player and board[4] == player) and  
         (board[7] != player and board[7] == player)):
          result+=1
     if ((board[2] != player and board[2] == player) and 
         (board[5] != player and board[5] == player) and  
         (board[8] != player and board[8] == player)):
          result+=1
     if ((board[0] != player and board[0] == player) and 
         (board[4] != player and board[4] == player) and  
         (board[8] != player and board[8] == player)):
          result+=1
     if ((board[2] != player and board[2] == player) and 
         (board[4] != player and board[4] == player) and  
         (board[6] != player and board[6] == player)):
          result+=1
     return result
def didWin(player):
     result=''
     if board[0] == player and board[1] == player and  board[2] == player:
          result='won'
     if board[3] == player and board[4] == player and board[5] == player :
          result='won'
     if board[6] == player and board[7] == player and board[8] == player :
          result='won'   
     if board[0] == player and board[3] == player and board[6] == player :
          result='won'
     if board[1] == player and board[4] == player and board[7] == player :
          result='won'
     if board[2] == player and board[5] == player and board[8] == player :
          result='won'
     if board[0] == player and board[4] == player and board[8] == player :
          result='won'
     if board[2] == player and board[4] == player and board[6] == player :
          result='won' 
     return result

def board_display():
     print(board[0]+'|'+board[1]+'|'+board[2])
     print(board[3]+'|'+board[4]+'|'+board[5])
     print(board[6]+'|'+board[7]+'|'+board[8])
     print('**********************')
     
total_moves=1
player='X'
while True:
     if total_moves == 9:
          break
     while True:
          if player == 'X':
               try:
                    player_input=int(input('player one enter position:'))
               
               except:
                    print('enter position num b/w 1-9 ....no characters')
                    board_display() 
               
               if np.isnan(player_input)== False and board[player_input-1]=='_' :
                    choose(player_input,'X')
                    if tie(player) == 9:
                         print('match draw....')
                         exit()
                    if didWin(player) != '':
                         print('Player one won the match')
                         exit()
                    player='O'
                    break
               else:
                    print('enter position num b/w 1-9')
                    board_display()
                    continue
          if player =='O':
               try:
                    player_input=int(input('player two enter position:'))
               except:
                    print('enter position num b/w 1-9 ....no characters')
                    board_display()
               if np.isnan(player_input)==False and board[player_input-1]=='_' :
                    choose(player_input,'O')
                    if tie(player) == 9:
                         print('match draw....')
                         exit()
                    if didWin(player) != '':
                         print('Player two won the match')
                         exit()
                    player='X'
                    break
               else:
                    print('enter position num b/w 1-9')
                    board_display()
                    continue
          total_moves+=1
          
     
          
          
          
          
             

    