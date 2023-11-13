from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from core.utils.dbconnect import Request
from core.utils.state import State
from core.keyboards.inline import get_web_app

# Define a router
form_router = Router()

# Handler for the /start command
@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    print("Inside the command_start function")
    await state.set_state(State.form)
    await message.answer(
        text='To continue, press the button below',
        reply_markup=get_web_app()
    )


# Handler for messages containing 'web_app_data'
@form_router.message(State.form & F.text.casefold() == "Order")
async def menu(message: Message, state: FSMContext) -> None:
    print("Inside the menu function")
    
    # Simplify the handler for debugging
    await message.answer(
        text=f'Your data: {message.web_app_data.data}'
    )
