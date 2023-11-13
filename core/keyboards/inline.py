from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardBuilder, KeyboardButton
from aiogram import types
from aiogram.types.web_app_info import WebAppInfo



def get_the_menu(id: str = None) -> InlineKeyboardMarkup:
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.add(InlineKeyboardButton(text='Margarita', callback_data=f'{id}'))
    keyboard_builder.add(InlineKeyboardButton(text='Pepperoni', callback_data=f'{id}'))
    keyboard_builder.add(InlineKeyboardButton(text='Hawaii', callback_data=f'{id}'))
    keyboard_builder.add(InlineKeyboardButton(text='Carbonara', callback_data=f'{id}'))
    keyboard_builder.adjust(2, 2)
    return keyboard_builder.as_markup()


# def get_web_app() -> InlineKeyboardMarkup:
#     keyboard_builder = InlineKeyboardBuilder()
#     keyboard_builder.add(InlineKeyboardButton(text='Order', web_app=WebAppInfo(url='https://alinaberens19.github.io/aiogram_pizza_web_app/')))
#     keyboard_builder.adjust()
#     return keyboard_builder.as_markup()


def get_web_app():
    keyboard_builder = ReplyKeyboardBuilder()
    keyboard_builder.add(KeyboardButton(text='Order', web_app=WebAppInfo(url='https://alinaberens19.github.io/aiogram_pizza_web_app/')))
    keyboard_builder.adjust()
    markup = keyboard_builder.as_markup()
    markup.resize_keyboard = True
    markup.one_time_keyboard = True
    markup.selective = True
    markup.input_field_placeholder = 'Order'

    return markup
    