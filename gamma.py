import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.filters.state import State, StatesGroup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.fsm.context import FSMContext

logging.basicConfig(level=logging.INFO)
bot = Bot(token="7137476088:AAG2GrP94NS5PredenfFEn5NdkJ--INed9E")
dp = Dispatcher()

class UserData(StatesGroup):
    found_or_lost = State()
    building = State()
    corp = State()
    photo_and_text = State()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="нашел"), types.KeyboardButton(text="потерял")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите категорию"
    )
    await message.answer("Выберите вариант:", reply_markup=keyboard)

@dp.message(F.text.lower() == "нашел")
async def found(message: types.Message, state: FSMContext):
    await state.update_data(found_or_lost="нашел")
    kb = [
        [types.KeyboardButton(text="корпус"),
         types.KeyboardButton(text="ступино")],
        [types.KeyboardButton(text="спорт комплексы")],
        [types.KeyboardButton(text="общежитие"),
         types.KeyboardButton(text="другое"),
         types.KeyboardButton(text="не помню")],
        [types.KeyboardButton(text="назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Где нашли?", reply_markup=keyboard)

@dp.message(F.text.lower() == "потерял")
async def lost(message: types.Message, state: FSMContext):
    await state.update_data(found_or_lost="потерял")
    kb = [
        [types.KeyboardButton(text="корпус"),
         types.KeyboardButton(text="ступино")],
        [types.KeyboardButton(text="спорт комплексы")],
        [types.KeyboardButton(text="общежитие"),
         types.KeyboardButton(text="другое"),
         types.KeyboardButton(text="не помню")],
        [types.KeyboardButton(text="назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите способ подачи"
    )
    await message.answer("Где потеряли?", reply_markup=keyboard)

@dp.message(F.text.lower() == "корпус")
async def corpus(message: types.Message, state: FSMContext):
    await state.update_data(building="корпус")
    kb = [
        [types.KeyboardButton(text="гук"),
         types.KeyboardButton(text="улк"),
         types.KeyboardButton(text="см/э")],
        [types.KeyboardButton(text="мт"),
         types.KeyboardButton(text="т")],
        [types.KeyboardButton(text="казармы")],
        [types.KeyboardButton(text="химический"),
         types.KeyboardButton(text="назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите корпус:"
    )
    await message.answer("В каком корпусе?", reply_markup=keyboard)

@dp.message(F.text.lower() == "спорт комплексы")
async def sport(message: types.Message, state: FSMContext):
    await state.update_data(building="спорт комплексы")
    kb = [
        [types.KeyboardButton(text="ск"),
        types.KeyboardButton(text="измайлово")],
        [types.KeyboardButton(text="м1"),
        types.KeyboardButton(text="м2"),
        types.KeyboardButton(text="м3")],
        [types.KeyboardButton(text="назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите спорт комплекс:"
    )
    await message.answer("В каком спорт комплексе?", reply_markup=keyboard)

@dp.message(F.text.lower() == "общежитие")
async def dorms(message: types.Message, state: FSMContext):
    await state.update_data(building="общежитие")
    kb = [
        [types.KeyboardButton(text="№2"),
         types.KeyboardButton(text="№4"),
         types.KeyboardButton(text="№5"),
         types.KeyboardButton(text="№6")],
         [types.KeyboardButton(text="№8"),
         types.KeyboardButton(text="№9"),
         types.KeyboardButton(text="№10"),
         types.KeyboardButton(text="№11")],
         [types.KeyboardButton(text="спектр"),
         types.KeyboardButton(text="стрела")],
         [types.KeyboardButton(text="назад")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите общежитие:"
    )
    await message.answer("В каком общежитии?", reply_markup=keyboard)

@dp.message(lambda message: message.text and message.text.lower() == "другое")
async def other(message: types.Message, state: FSMContext):
    await state.update_data(building="другое")
    await state.set_state(UserData.building)
    await message.answer("Введите где потеряли:")

@dp.message(UserData.building)
async def handle_building(message: types.Message, state: FSMContext):
    await state.update_data(corp=message.text)
    await state.set_state(UserData.photo_and_text)
    await message.answer("Пожалуйста, отправьте фото и текст.")

@dp.message(lambda message: message.text and message.text.lower() == "не помню")
async def dont_remember(message: types.Message, state: FSMContext):
    await state.update_data(building="не помню")
    await state.set_state(UserData.building)
    await message.answer("Напишите место, где потеряли:")

@dp.message(F.text.lower() == "назад")
async def back(message: types.Message):
    kb = [
        [types.KeyboardButton(text="нашел"), types.KeyboardButton(text="потерял")],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие:"
    )
    await message.answer("Выберите вариант:", reply_markup=keyboard)

@dp.message(lambda message: message.text and message.text.lower() in ["гук", "улк", "см/э", "мт", "т", "казармы", "химический", "ск", "измайлово", "м1", "м2", "м3", "№2", "№4", "№5", "№6", "№8", "№9", "№10", "№11", "спектр", "стрела", "не помню", "ступино"])
async def request_photo_text(message: types.Message, state: FSMContext):
    await state.update_data(corp=message.text.lower())
    await state.set_state(UserData.photo_and_text)
    await message.answer("Пожалуйста, отправьте фото и текст одновременно.")

@dp.message(UserData.photo_and_text)
async def handle_photo_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_info = f"{message.from_user.full_name} (@{message.from_user.username})"
    found_or_lost = data.get('found_or_lost', 'неизвестно')
    building = data.get('building')
    corp = data.get('corp')
    texto = message.caption if message.caption else message.text
    photo = message.photo[-1].file_id if message.photo else None

    if photo and texto:
        await bot.send_photo(chat_id="-1002077091455", photo=photo, caption=f"*Где {found_or_lost}:* {building}, {corp}\n*Что {found_or_lost}:* {texto}\n*Контакт:* {user_info}", parse_mode="Markdown")
    elif texto:
        await bot.send_message(chat_id="-1002077091455", text=f"*Где {found_or_lost}:* {building}, {corp}\n*Что {found_or_lost}:* {texto}\n*Контакт:* {user_info}", parse_mode="Markdown")
    elif photo:
        await state.update_data(partial_photo=photo)
        await message.answer("Пожалуйста, отправьте текст.")
        return
    else:
        await message.answer("Пожалуйста, отправьте фото или текст.")
        return

    await state.clear()
    await message.answer("Информация успешно отправлена.")
    await cmd_start(message)

@dp.message(UserData.photo_and_text)
async def handle_additional_input(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo = data.get('partial_photo')
    
    if photo and message.caption:
        await bot.send_photo(chat_id="-1002077091455", photo=photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), {message.caption}")
    elif photo and message.photo:
        new_photo = message.photo[-1].file_id
        await bot.send_photo(chat_id="-1002077091455", photo=new_photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), без текста")
    elif photo:
        await bot.send_photo(chat_id="-1002077091455", photo=photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), без текста")
    else:
        await message.answer("Пожалуйста, отправьте текст или еще одно фото.")
        return
    
    await state.clear()
    await message.answer("Информация успешно отправлена.")
    await cmd_start(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
