from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault




async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Start the bot"),
        BotCommand(command="/help", description="Get help"),
        BotCommand(command="/order", description="Order pizza"),
    ]
    
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())


commands = set_commands