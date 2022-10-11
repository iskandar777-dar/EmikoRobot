import html
import random
from EmikoRobot.data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from EmikoRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EmikoRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

# Start Message
def string(update: Update, context: CallbackContext, bot: Client, msg: Message):
    args = context.args
    user = bot.get_me()
    mention = user.mention
    bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )
    
STRING_HANDLER = DisableAbleCommandHandler("string", string, run_async=True)

dispatcher.add_handler(STRING_HANDLER)
