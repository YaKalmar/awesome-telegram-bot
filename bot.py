import telepot
import os
import settings
import producthunt_rss

token = os.environ.get("TELEGRAM_TOKEN")
TelegramBot = telepot.Bot(token)
print TelegramBot.getMe()


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