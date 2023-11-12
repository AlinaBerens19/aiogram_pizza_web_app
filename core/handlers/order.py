from aiogram import F, Router, html, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from core.utils.dbconnect import Request
from core.utils.commands import set_commands
from core.middleware.settings import settings
from core.utils.dbconnect import Request
from core.utils.state import State
from core.keyboards.inline import get_the_menu, get_web_app



form_router = Router()


@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await state.set_state(State.initial)
    await message.answer(
        text='To continue, press the button below',
        reply_markup=get_web_app()
    )
        
        



             

