import asyncio
import logging

from aiogram import types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from config import BOT_TOKEN, DP, ADMIN_CHAT_ID
from consts import UserDataStates, START, BUILDING, CORPUS, SPORT_COMPLEXES, DORMS

logging.basicConfig(level=logging.INFO)

async def cmd_start(message: types.Message):
    await message.answer("Выберите вариант:", reply_markup=START)

async def found_or_lost(message: types.Message, state: FSMContext):
    await state.update_data(found_or_lost=message.text.lower())
    await message.answer("Где нашли/потеряли?", reply_markup=BUILDING)

async def building(message: types.Message, state: FSMContext):
    await state.update_data(building=message.text.lower())
    if message.text.lower() == "другое":
        await state.set_state(UserDataStates.building)
        await message.answer("Введите где потеряли:")
    elif message.text.lower() == "не помню":
        await state.set_state(UserDataStates.building)
        await message.answer("Напишите место, где потеряли:")
    elif message.text.lower() in ["корпус", "спорт комплексы", "общежитие"]:
        if message.text.lower() == "корпус":
            await message.answer("В каком корпусе?", reply_markup=CORPUS)
        elif message.text.lower() == "спорт комплексы":
            await message.answer("В каком спорт комплексе?", reply_markup=SPORT_COMPLEXES)
        elif message.text.lower() == "общежитие":
            await message.answer("В каком общежитии?", reply_markup=DORMS)
    await state.set_state(UserDataStates.photo_and_text)
    await message.answer("Пожалуйста, отправьте фото и текст.")

async def handle_building(message: types.Message, state: FSMContext):
    await state.update_data(corp=message.text)
    await state.set_state(UserDataStates.photo_and_text)
    await message.answer("Пожалуйста, отправьте фото и текст.")

async def handle_photo_text(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_info = f"{message.from_user.full_name} (@{message.from_user.username})"
    found_or_lost = data.get('found_or_lost', 'неизвестно')
    building = data.get('building')
    corp = data.get('corp')
    texto = message.caption if message.caption else message.text
    photo = message.photo[-1].file_id if message.photo else None

    if photo and texto:
        await BOT_TOKEN.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo, caption=f"<b>Где {found_or_lost}:</b> {building}, {corp}\n<b>Что {found_or_lost}:</b> {texto}\n<b>Контакт:</b> {user_info}", parse_mode="HTML")
    elif texto:
        await BOT_TOKEN.send_message(chat_id=ADMIN_CHAT_ID, text=f"<b>Где {found_or_lost}:</b> {building}, {corp}\n<b>Что {found_or_lost}:</b> {texto}\n<b>Контакт:</b> {user_info}", parse_mode="HTML")
    elif photo:
        await state.update_data(partial_photo=photo)
        await message.answer("Пожалуйста, отправьте текст.")
        return
    else:
        await message.answer("Пожалуйста, отправьте фото или текст.")
        return

async def handle_additional_input(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photo = data.get('partial_photo')

    if photo and message.caption:
        await BOT_TOKEN.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), {message.caption}")
    elif photo and message.photo:
        new_photo = message.photo[-1].file_id
        await BOT_TOKEN.send_photo(chat_id=ADMIN_CHAT_ID, photo=new_photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), без текста")
    elif photo:
        await BOT_TOKEN.send_photo(chat_id=ADMIN_CHAT_ID, photo=photo, caption=f"{message.from_user.full_name} (@{message.from_user.username}), без текста")
    else:
        await message.answer("Пожалуйста, отправьте текст или еще одно фото.")
        return

    await state.clear()
    await message.answer("Информация успешно отправлена.")
    await cmd_start(message)

async def main():
    @DP.message(Command("start"))
    async def cmd_start_handler(message: types.Message):
        await cmd_start(message)

    @DP.message(F.text.lower() == "нашел")
    async def found_handler(message: types.Message, state: FSMContext):
        await found_or_lost(message, state)

    @DP.message(F.text.lower() == "потерял")
    async def lost_handler(message: types.Message, state: FSMContext):
        await found_or_lost(message, state)

    @DP.message(lambda message: message.text and message.text.lower() in ["гук", "улк", "см/э", "мт", "т", "бмт","казармы", "химлаб", "ск", "измайлово", "м1", "м2", "м3", "№2", "№4", "№5", "№6", "№8", "№9", "№10", "№11", "спектр", "стрела", "не помню", "ступино"])
    async def request_photo_text_handler(message: types.Message, state: FSMContext):
        await handle_building(message, state)

    @DP.message(UserDataStates.photo_and_text)
    async def handle_photo_text_handler(message: types.Message, state: FSMContext):
        await handle_photo_text(message, state)

    @DP.message(UserDataStates.photo_and_text)
    async def handle_additional_input_handler(message: types.Message, state: FSMContext):
        await handle_additional_input(message, state)

    await DP.start_polling(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
