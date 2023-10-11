from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import start_keyboard
from services.services import users
from constants.constants import list_of_variants
from aiogram import Router, F
import random

router = Router()


@router.message(F.text.in_(list_of_variants))
async def process_game_command(message: Message):
    bot_answer = random.choice(list_of_variants)
    user_id = message.from_user.id
    user = users.get_user_by_id(user_id)

    if user.in_game:
        await message.answer(f'{bot_answer}\n{user.check_answer(message.text, bot_answer)}')

        if user.attempts == 0:
            await message.answer(f'{LEXICON_RU["game_is_over"]}\n'
                                 f'{user.get_winner()}')
            user.reset_game()
            await message.answer(LEXICON_RU['ask_for_game'], reply_markup=start_keyboard)
    else:
        await message.answer(f"{LEXICON_RU['you_are_not_in_game']}\n"
                             f"{LEXICON_RU['ask_for_game']}", reply_markup=start_keyboard)




