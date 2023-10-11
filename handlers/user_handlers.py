from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import start_keyboard, game_keyboard
from services.services import users
from aiogram import Router, F

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    user_id = message.from_user.id
    if not users.is_user_exist(user_id):
        users.add_user(user_id)

    await message.answer(LEXICON_RU['/start'], reply_markup=start_keyboard)
    await message.answer(LEXICON_RU['ask_for_game'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(LEXICON_RU['/help'])


@router.message(Command(commands='stat'))
async def process_stat_command(message: Message):
    user_id = message.from_user.id
    user = users.get_user_by_id(user_id)
    await message.answer(LEXICON_RU['/stat'](user))


@router.message(F.text == LEXICON_RU['yes_btn'])
async def process_start_game_command(message: Message):
    user_id = message.from_user.id
    user = users.get_user_by_id(user_id)
    user.in_game = True
    await message.answer(f"{LEXICON_RU['yes_btn_answer']}\n"
                         f"{LEXICON_RU['rounds'](user)}", reply_markup=game_keyboard)


@router.message(F.text == LEXICON_RU['no_btn'])
async def process_start_game_command(message: Message):
    await message.answer(LEXICON_RU['no_btn_answer'])
