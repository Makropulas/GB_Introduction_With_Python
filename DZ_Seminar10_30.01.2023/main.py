from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *



app = ApplicationBuilder().token("TOKENAMANA").build()

print('Бот запущен...')

app.add_handler(CommandHandler("start", hi_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("new_year", new_year_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("help", help_command))

app.run_polling()

print('Бот остановлен')