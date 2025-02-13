from aiogram import Bot, Dispatcher, types

class UserDataStates(types.StatesGroup):
    found_or_lost = types.State()
    building = types.State()
    corp = types.State()
    photo_and_text = types.State()