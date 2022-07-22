import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import(
    CallbackContext, 
    Updater,
    PicklePersistence, 
    CommandHandler, 
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, cursy_menu_keyboard
from key_buttons import tele_button, button

def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgQAAxkBAAEFNm9ixrOZAQRB8_NpRbfczYT-pfa6AwAC0gwAAvEHOVD6WOBBBtWRtSkE'
    )  
    update.message.reply_text(
        "Добро пожаловать, {username}".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )

COURSE_REGEX = r"(?=("+(tele_button[1])+r"))"
PYTHON_KEY = r"(?=("+(button[0])+r"))"
ZAPIS = r"(?=("+(tele_button[3])+r"))"
LOCATI = r"(?=("+(tele_button[2])+r"))"



def zapisat(update: Update, context:CallbackContext):
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
            chat_id = '@ogogkiwibanana', 
            text = z
        )


def zapis(update: Update, context: CallbackContext):
    
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgQAAxkBAAEFNndixrOmKj6I6o0UiD1vc8YLwEyL0QACkAoAAroh6FO__6iiw4cJkSkE'
    )
    info=re.match(ZAPIS, update.message.text)
    update.message.reply_text(
        text = """
1. Напишите сообщение с "Запись: " и ваше имя.
2. Ваш номер телефона
3. Выберите время удобный вам.
! После отправки всех заполненных бланок Админ вам позвонит.:)
"""
 ) 





def resive_curse_menu(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgQAAxkBAAEFNnFixrOeTgABumeH3YdY2FAUUld12LcAAukKAAKMUelTglLNTjhbwHYpBA'
    )
    update.message.reply_text(
        'Выберите курс',
        reply_markup=cursy_menu_keyboard()
    )

def resive_info(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgQAAxkBAAEFNohixrQLEnqzRXWdq83hIfkLsBy15QACZxAAAhTXgVDxNduO5gS_DykE'
    )
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = 'Location of OGOGO'
    )
    update.message.reply_location(
        # 42.873686482321595, 74.61985231003044
        longitude=74.61985231003044,
        latitude=42.873686482321595,
        reply_to_message_id=msg.message_id
    )




def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='python_mentor'),
            InlineKeyboardButton('Lesson', callback_data='python_lesson'),
        ],
        [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выбери опцию",
        reply_markup=reply_markup
    )


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/umar.jfif', 'rb'),
        )
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/umar.jfif', 'rb'),
            caption="""
n name: Umar
age: 21
expierence: 5 years
work place: Tesla, Google, Apple          
            """
        )
    
    if query.data == 'python_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
    
Расписание:
Каждый день
567890-=098765trchjbknlmm;kvdc

            """

        )
    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
16000 som per month
            """
        )




updater = Updater(TOKEN,persistence=PicklePersistence(filename='bot_data') )
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX), 
    resive_curse_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON_KEY), 
    python_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATI), 
    resive_info
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS),
    zapis
    ))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
    ))



updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
