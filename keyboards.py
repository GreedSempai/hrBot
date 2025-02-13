from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType


START = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="нашел"),
            KeyboardButton(text="потерял"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите вариант:",
)

BUILDING = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="корпус"),
            KeyboardButton(text="спорт комплексы"),
        ],
        [
            KeyboardButton(text="общежитие"),
            KeyboardButton(text="другое"),
            KeyboardButton(text="не помню"),
        ],
        [
            KeyboardButton(text="назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите место:",
)

CORPUS = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="гук"),
            KeyboardButton(text="улк"),
            KeyboardButton(text="см/э"),
        ],
        [
            KeyboardButton(text="мт"),
            KeyboardButton(text="т"),
            KeyboardButton(text="к"),
        ],
        [
            KeyboardButton(text="казармы"),
            KeyboardButton(text="бмт"),
        ],
        [
            KeyboardButton(text="химлаб"),
            KeyboardButton(text="назад"),
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
            KeyboardButton(text="спектр"),
            KeyboardButton(text="стрела"),
        ],
        [
            KeyboardButton(text="назад"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите общежитие:",
)
