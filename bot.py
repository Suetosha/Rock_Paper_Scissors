import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config_data.config import Config, load_config
from handlers import user_handlers, game_handlers, other_handlers


async def set_main_menu(bot: Bot):

    main_menu_commands = [
        BotCommand(command='/stat',
                   description='Статистика'),
        BotCommand(command='/help',
                   description='Помощь'),
        BotCommand(command='/start',
                   description='Cтарт игры')
    ]
    await bot.set_my_commands(main_menu_commands)


async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(game_handlers.router)
    dp.include_router(other_handlers.router)
    dp.startup.register(set_main_menu)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
