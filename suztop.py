#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 07:26:21 2024

@author: sarvar
"""
"""Suz top uyini"""

import random
from words import wordlar

print(wordlar)


def get_word():
    word=random.choice(wordlar)
    while "-" in word or " " in word:
        word=random.choice(wordlar)
    return word.upper()


def desplay(user_letters,word):
    
    user_display=' ' 
    for letter in word:
        if letter in user_letters.upper():
            user_display += letter
        else:
            user_display += '-'
            
    return user_display


def play():
    
    word=get_word()
    word_letters=set(word)
    print(word)
    user_letters=''
    
    print(f'Men {len(word)} xonali suz uyladm uni topishga harakat qiling!!')
    
    
    while word_letters:
        
        print(desplay(user_letters, word))
        if user_letters:
            print(f"Шу вақтгача киритган ҳарфларингиз: {user_letters}")
            
        letter=input('soz kiriting::').upper()
        
        if letter in user_letters:
            print("Bu harfni oldin kiriitgansz iltimos boshqa harf kiriting::")
            
            continue
        elif letter in word:
            word_letters.remove(letter)
            print(f'bu harfni tugri topdizz {letter}')
        else:
            print('bunday harf yuq')
            
        user_letters+=letter
    print(f"Tabriklayman siz {word} suzini {len(user_letters)} ta urinishda topdizz")
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            