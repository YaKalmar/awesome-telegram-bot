import telepot
import os
import settings

token = os.environ.get("TELEGRAM_TOKEN")
TelegramBot = telepot.Bot(token)
print TelegramBot.getMe()
