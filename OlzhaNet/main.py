from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup

from telegram.ext import *
from datetime import datetime

print("Bot started...")

now = datetime.now()

token='1837495475:AAGIHm-nKj3GdFZkfEhJLTYaB12EHfaCjtM'

def start_command(update, context):
    user = update.message.from_user

    if (now.hour>=0 and now.hour<6 ):
        update.message.reply_text('Қайырлы түн😇 {} {}'.format(user['first_name'], user['last_name']))
    if (now.hour>=6 and now.hour<12):
        update.message.reply_text('Қайырлы таң😇 {} {}'.format(user['first_name'], user['last_name']))
    if (now.hour>=12 and now.hour<18):
        update.message.reply_text('Қайырлы күн😇 {} {}'.format(user['first_name'], user['last_name']))
    if (now.hour>=18 and now.hour<=23):
        update.message.reply_text('Қайырлы кеш😇 {} {}'.format(user['first_name'], user['last_name']))

#___Қосымша мәтін
    update.message.reply_text('Менің есімім Азықанов Талғат🤠 және менің чат-ботыма қош келдіңіз🤗')

#___Батырмаларды қосу
    text = "Instagram-ға тіркелу"
    callback = "https://www.instagram.com/azyqanovtalgat/"

    keyboard = []
    keyboard.append([InlineKeyboardButton(text, url=callback)])
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Тіркеліп болған соң, сізге тегін чек-лист беремін!', reply_markup=reply_markup)

#____Қосымша құжаттарды кірістіру
    attachment="https://www.dropbox.com/s/8dfrniil873oj2x/Anonymous.pdf?dl=0"
    context.bot.sendDocument(update.effective_chat.id, attachment)


def help_command(update, context):
    update.message.reply_text('Егер көмек керек болса келесі номер бойынша хабарласыңыз: +77716938913 ')



def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Сәлем", "Hi", "Привет"):
        return "Сәлем бердік!"
    if user_message in ("Бастау"):
        return "Қызмет түрін таңдаңыз"

    return "Сізді түсінбедім /"


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))



    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()




main()
