#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 00:20:27 2024

@author: sarvar
"""

"""SON TOP UYINI"""

import random

def sontop(x=10):
    
    tasodifiy_son=random.randint(1,x)
    print(f"1 dan  {x} gacha son uyladm topaolaszmi!!!")
    taxminlar_soni=0
    while True:
        taxminlar_soni+=1
        taxmin=int(input(' son >>>'))
        if taxmin<tasodifiy_son:
            print("Men uylagan son bundan kattaroq harakat qiling!!!")
        elif taxmin>tasodifiy_son:
            print("Men uylagan son bundan kichikroq harakat qiling!!!")
            
        else:
            break
    print(f"Tabriklaymizz siz {taxminlar_soni} ta taxmin bilan topdingiz")
    return taxminlar_soni
        
def sontop_pc(x=10):
    input(f"1 dan {x} gacha son uylang men topaman !!!")
    quyi=1
    yuqori=x
    taxminlar_sonipc=0
    while True:
        taxminlar_sonipc+=1
        if yuqori != quyi:
            taxmin=random.randint(quyi, yuqori)
        else:
            quyi=yuqori
        javob=input(f"siz {taxmin} son uyladingizz - tugri(t)  men uylagan son bundan kaataroq(+)  men uylagan son bundan kichikroq(-) >>>")
        
        if javob == "-":
            yuqori=taxmin-1
        elif javob == "+":
            taxmin=quyi+1
            
        else:
            break
    print(f"Men {taxminlar_sonipc} ta taxmin bilan Topdim")
    return taxminlar_sonipc
       


def play(x=10):
    yana=True
    while yana:
        taxminlar_user=sontop(x)
        taxminlar_pc=sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user < taxminlar_pc:
            print("siz yutdiz")
        else:
            print("Durrang")
            
        yana=int(input("Yana uynayszmi ha(1)/yuq(0)--"))
        
            
            
        
        