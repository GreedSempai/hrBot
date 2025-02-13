import os

BOT_TOKEN = None
DB_CREDENTIALS = None

def get_BOT_TOKEN():
    global BOT_TOKEN

    if BOT_TOKEN is None:
        BOT_TOKEN = os.getenv("BOT_TOKEN")

    return BOT_TOKEN

def get_ADMIN_ID():
    global ADMIN_CHAT_ID

    if ADMIN_CHAT_ID is None:
        ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

    return ADMIN_CHAT_ID