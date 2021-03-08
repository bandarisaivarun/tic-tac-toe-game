import numpy as np

board=['_','_','_','_','_','_','_','_','_']
class tictactoe :
     def init(self):
          self.pos=''
     
     def tictactoe(self,):
          self.pos=int(input('enter pos:'))
          if self.pos!='' and  type(self.pos)== int:
                 self.choose(self.pos) 
          else:
               return(False)
     def choose(self,pos):
          if board[pos-1]=='_':
               board[pos-1]='x'
               self.board()
          else:
               print('position',self.pos,'is occupied')
               self.tictactoe()
     def board(self):
          print(board)
p1=tictactoe()

p2=tictactoe()
count=0
while count < 9:
     def game():
          p1.tictactoe()
          #p2.tictactoe()
     game()
          
          
          
          
             

    