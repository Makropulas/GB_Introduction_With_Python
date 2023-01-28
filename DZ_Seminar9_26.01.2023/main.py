from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *



app = ApplicationBuilder().token("YOUR_TOKEN").build()

print('Бот запущен...')

app.add_handler(CommandHandler("start", hi_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("calc", calc_command))

app.run_polling()

print('Бот остановлен')