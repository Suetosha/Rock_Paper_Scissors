from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU
from aiogram import Router

router = Router()


@router.message()
async def process_other_command(message: Message):
    await message.answer(LEXICON_RU['other_handler'])
