from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup)
from lexicon.lexicon import LEXICON_RU

start_btn_1 = KeyboardButton(text=LEXICON_RU['yes_btn'])
start_btn_2 = KeyboardButton(text=LEXICON_RU['no_btn'])

start_keyboard = ReplyKeyboardMarkup(keyboard=[[start_btn_1, start_btn_2]], resize_keyboard=True)

game_btn_1 = KeyboardButton(text=LEXICON_RU['rock'])
game_btn_2 = KeyboardButton(text=LEXICON_RU['scissors'])
game_btn_3 = KeyboardButton(text=LEXICON_RU['paper'])

game_keyboard = ReplyKeyboardMarkup(keyboard=[[game_btn_1, game_btn_2, game_btn_3]], resize_keyboard=True)
