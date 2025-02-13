from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType


START = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нашел"),
            KeyboardButton(text="Потерял"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите вариант:",
)

BUILDING = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Корпус"),
            KeyboardButton(text="Спорт комплексы"),
        ],
        [
            KeyboardButton(text="Общежитие"),
            KeyboardButton(text="Другое"),
            KeyboardButton(text="Не помню"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите место:",
)

CORPUS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="ГУК"),
            KeyboardButton(text="УЛК"),
            KeyboardButton(text="СМ/Э"),
        ],
        [
            KeyboardButton(text="МТ"),
            KeyboardButton(text="Т"),
            KeyboardButton(text="К"),
        ],
        [
            KeyboardButton(text="Казармы"),
            KeyboardButton(text="БМ"),
        ],
        [
            KeyboardButton(text="Химлаб"),
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите корпус:",
)

SPORT_COMPLEXES = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="СК"),
            KeyboardButton(text="Измайлово"),
        ],
        [
            KeyboardButton(text="М1"),
            KeyboardButton(text="М2"),
            KeyboardButton(text="М3"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите спорт комплекс:",
)

DORMS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="№2"),
            KeyboardButton(text="№4"),
            KeyboardButton(text="№5"),
            KeyboardButton(text="№6"),
        ],
        [
            KeyboardButton(text="№8"),
            KeyboardButton(text="№9"),
            KeyboardButton(text="№10"),
            KeyboardButton(text="№11"),
        ],
        [
            KeyboardButton(text="Спектр"),
            KeyboardButton(text="Стрела"),
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите общежитие:",
)