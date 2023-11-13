from aiogram.fsm.state import State, StatesGroup



class State(StatesGroup):
    form = State()
    choose_dough = State()
    choose_sauce = State()
    choose_cheese = State()
    choose_something_else = State()
    choose_drink = State()
    choose_quantity = State()
    choose_address = State()
    choose_payment = State()
    choose_comment = State()
    order_confirmation = State()

