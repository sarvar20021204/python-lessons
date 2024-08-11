#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 09:23:49 2024

@author: sarvar
"""

from krillotinsozlar import to_cyrillic,to_latin
import telebot


bot = telebot.TeleBot("7476019617:AAFyHBDUMd9IaZLL0gsr7AcLpXbfAfduHjM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob='Assalomu alaykum Xush kelibsz'
    javob+='\n Matn kiriting'
    bot.reply_to(message, javob)
    
@bot.message_handler(commands=['help'])

def send_welcome(message):
    bot.reply_to(message, 'Bu bot faqat Kril Lotin Alifbosi uchun ishlaydi')

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    
    bot.reply_to(message, javob)

bot.infinity_polling()