import telepot
import os
import settings
import producthunt_rss

token = os.environ.get("TELEGRAM_TOKEN")
TelegramBot = telepot.Bot(token)


def display_help():
    return "Heya!\nWanna see 10 latest products from Product Hunt?\nYou can use command 'feed' for that!"


def display_ph_feed():
    items = producthunt_rss.parse_producthunt_rss()
    result = ""
    for item in items:
        result += '%s (%s)\n' % (item['title'], item['link'])

    return result.encode('ascii', errors='ignore')


def display_dont_understand():
    return "Sorry, i don't understand :(\nI'm not as smart as Siri (yet)"


def get_latest_offset():
    offset = 0
    # w+ just in case file doesn't exists
    config_file = open('config.txt', 'w+')
    config_line = config_file.readline()
    if config_line:
        try:
            offset = int(config_line)
        except ValueError:
            pass
    config_file.close()

    return offset


def save_latest_offset(offset):
    config_file = open('config.txt', 'w')
    config_file.write(str(offset))
    config_file.close()


# Getting latest offset
latest_offset = get_latest_offset()

while True:
    updates = TelegramBot.getUpdates(latest_offset)
    for update in updates:
        message_text = update['message']['text']
        chat_id = update['message']['chat']['id']
        if message_text == 'help' or message_text == '/start':
            TelegramBot.sendMessage(chat_id, display_help())
        elif message_text == 'feed':
            TelegramBot.sendMessage(chat_id, display_ph_feed())
        else:
            TelegramBot.sendMessage(chat_id, display_dont_understand())
        latest_offset = int(update['update_id']) + 1
        save_latest_offset(latest_offset)
