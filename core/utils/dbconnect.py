from aiogram import Bot, Dispatcher, types



class Request:
    def __init__(self, connector):
        self.connector = connector