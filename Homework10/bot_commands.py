from telegram import Update
from telegram.ext import ContextTypes
import datetime

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Бот может выполнять одну\
    из следующих арифметических операций\
    с двумя числами:\n\
+, -, *, /\n\nПримеры записи:\n\
"2+2"\n"6-9"\n"5*8"\n"10/2"\n"(-5+9j)/(6-2j)"')
    
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"{datetime.datetime.now().time()};\
{update.effective_user.username};{update.effective_user.id};{update.message.text}\n")