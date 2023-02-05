from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.ext import filters, MessageHandler
import bot_commands as bc
import operation_logic as ol

app = ApplicationBuilder().token("6027370048:AAG5iEc2z4ZSDEG4jwtYs5Ivk9Eof2nh78I").build()

app.add_handler(CommandHandler("help", bc.help))
app.add_handler(CommandHandler("info", bc.info))
app.add_handler(MessageHandler(filters.TEXT, ol.parse))
print('Запущен!')
app.run_polling()