from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *
import emoji


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(emoji.emojize(f'Привет, {update.effective_user.first_name}!\n'
                                        'Спасибо, что решил посетить меня :smiling_face_with_open_hands:\n\n '
                                        'Чтобы увидеть список команд, введи /help'))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n/time - Текущее время\n/calc - Калькулятор\n/help - Перечень команд')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def calc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    msg = msg.replace('/calc ', '')
    replace_msg = msg.replace('^', "**")
    await update.message.reply_text(f'{msg} = {eval(replace_msg)}')