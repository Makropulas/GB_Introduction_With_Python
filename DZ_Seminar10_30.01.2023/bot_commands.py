from telegram import Update
from telegram.ext import ContextTypes
from datetime import datetime
from spy import *
import emoji


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(emoji.emojize(f'Привет, {update.effective_user.first_name}!\n'
                                        'Спасибо, что решил посетить меня :smiling_face_with_open_hands:\n\n '
                                        'Чтобы увидеть список команд, введи /help'))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n/time - Текущее время\n/new_year - Дней до нового года\n'
                                    '/calc - Калькулятор\n/help - Перечень команд')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    now = datetime.now().time()
    now.strftime("%H:%M")
    await update.message.reply_text(emoji.emojize(f'Московское время :mantelpiece_clock: {now.strftime("%H:%M:%S")}'))

async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    now = datetime.now()
    new_year = datetime(now.year + 1, 1, 1)
    period = new_year - now
    hours = period.seconds // 3600
    minutes = (period.seconds // 60) % 60
    await update.message.reply_text(emoji.emojize(f':Christmas_tree: Новый год наступит через\n      {period.days} дн. {hours} ч. {minutes} мин. :Santa_Claus_medium-light_skin_tone:'))

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    msg = msg.replace('/calc ', '')
    replace_msg = msg.replace('^', "**")
    await update.message.reply_text(f'{msg} = {eval(replace_msg)}')