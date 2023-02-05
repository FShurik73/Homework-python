from telegram import Update
from telegram.ext import ContextTypes
import datetime


async def parse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    msg = update.message.text
    msg = msg.replace(" ", "")
    if "j" in msg:
        ans = calc_complex(msg)
    else:
        ans = calc_real(msg)
    await log(update, ContextTypes.DEFAULT_TYPE, reply=ans)
    print(ans)
    await update.message.reply_text(str(ans))

def calc_real(msg):
    if "*" in msg:
        msg = msg.split("*")
        return float(msg[0])*float(msg[1])
    elif "/" in msg:
        msg = msg.split("/")
        return float(msg[0])/float(msg[1])
    elif "-" in msg:
        msg = msg.split("-")
        return float(msg[0])-float(msg[1])
    elif "+" in msg:
        msg = msg.split("+")
        return float(msg[0])+float(msg[1])


def calc_complex(msg):
    a = complex(msg[msg.find("(")+1:msg.find(")")])
    msg = msg[0:msg.find("(")]+msg[msg.find(")")+1:]
    b = complex(msg[msg.find("(")+1:msg.find(")")])
    msg = msg[0:msg.find("(")]+msg[msg.find(")")+1:]
    if "*" in msg:
        return a*b
    elif "/" in msg:
        return a/b
    elif "-" in msg:
        return a-b
    elif "+" in msg:
        return a+b


async def log(update: Update, context: ContextTypes.DEFAULT_TYPE, reply) -> None:
    file = open('loging.csv', 'a')
    file.write(f"{datetime.datetime.now().time()};{update.effective_user.username};{update.effective_user.id};{update.message.text};{reply}\n")
    file.close()