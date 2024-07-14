#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 10:35:25 2024

@author: sarvar
"""

game_tactikasi="""
Bu tic toc toe uyin kurinishi
----------------------------------------|

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9
---|---|---

-----------------------------------------|

1-qoida :: 1-dan 9- gacha bulgan sonlarni kiritng



"""


signup_list=[ ]
for i in range(9):
    signup_list.append(' ')

def print_board():

    board=f"""
        {signup_list[0]}  | {signup_list[1]} |  {signup_list[2]}
        ---|---|---
        {signup_list[3]}  | {signup_list[4]} |  {signup_list[5]}
        ---|---|---
        {signup_list[6]}  | {signup_list[7]} |  {signup_list[8]}
        ---|---|---

        """
    print(board)
index_list=[ ]
def take_input(player_name):
    while True:
       x=int(input(f"{player_name}--"))
       x-=1
       if 0<=x<10:
           if x in index_list:
               print('Bu joy band boshqa joy toping::')
               continue
           
           index_list.append(x)
           return x
       print('iltimos 1-9 oraligidagi sonni kiriting')

def result(player_one, player_two):
    # Assuming signup_list is a list representing the Tic-Tac-Toe board
    if (signup_list[0] == signup_list[1] == signup_list[2] == 'X' or 
        signup_list[3] == signup_list[4] == signup_list[5] == 'X' or 
        signup_list[6] == signup_list[7] == signup_list[8] == 'X' or
        signup_list[0] == signup_list[3] == signup_list[6] == 'X' or 
        signup_list[1] == signup_list[4] == signup_list[7] == 'X' or 
        signup_list[2] == signup_list[5] == signup_list[8] == 'X' or 
        signup_list[0] == signup_list[4] == signup_list[8] == 'X' or 
        signup_list[2] == signup_list[4] == signup_list[6] == 'X'):

        print(f"{player_one} Siz yutdingiz !")
        quit('rahmat uyin ucun')
    
    elif (signup_list[0] == signup_list[1] == signup_list[2] == 'O' or 
        signup_list[3] == signup_list[4] == signup_list[5] == 'O' or 
        signup_list[6] == signup_list[7] == signup_list[8] == 'O' or
        signup_list[0] == signup_list[3] == signup_list[6] == 'O' or 
        signup_list[1] == signup_list[4] == signup_list[7] == 'O' or 
        signup_list[2] == signup_list[5] == signup_list[8] == 'O' or 
        signup_list[0] == signup_list[4] == signup_list[8] == 'O' or 
        signup_list[2] == signup_list[4] == signup_list[6] == 'O'):

        print(f"{player_two} siz yutdingiz !")
        quit("rahmat uyin ucun")
        
        

def main():
    print('Xush kelibsiz Tic-Toc-Toe uyiniga')
    player_one=input('1-uyinchi name kiriting::')
    player_two=input('2-uyinchi name kiriting::')
    print(f'Xush kelibsz {player_one} and {player_two}')
    print(game_tactikasi)
    print(f'{player_one} siz X-da uynaysz')
    print(f'{player_two} siz O-da uynaysz')
    input("O'yinga start berish uchun enterni bosing::")
    print_board()
    for i in range(9):
        if i%2==0:
            index=take_input(player_one)
            signup_list[index]='X'
        else:
            index=take_input(player_two)
            signup_list[index]='O'

        
     
        print_board()
        result(player_one,player_two)
    print('Durrang!! dustlik galaba qozondi')      
main()
