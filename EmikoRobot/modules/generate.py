import html
import random
from EmikoRobot.data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from EmikoRobot import dispatcher
from telegram import ParseMode, Update, Bot
from EmikoRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

from pyrogram.types import Message
from telethon import TelegramClient
from pyrogram import Client, filters
from pyrogram import Client as Client1
from asyncio.exceptions import TimeoutError
from telethon.sessions import StringSession
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
from pyrogram.errors import (
    ApiIdInvalid as ApiIdInvalid1,
    PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1,
    PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1,
    PasswordHashInvalid as PasswordHashInvalid1
)
from telethon.errors import (
    ApiIdInvalidError,
    PhoneNumberInvalidError,
    PhoneCodeInvalidError,
    PhoneCodeExpiredError,
    SessionPasswordNeededError,
    PasswordHashInvalidError
)


ask_ques = "**Pilih String Yang Kamu mau :**"
buttons_ques = [
    [
        InlineKeyboardButton("ᴩʏʀᴏɢʀᴀᴍ", callback_data="pyrogram1"),
        InlineKeyboardButton("ᴩʏʀᴏɢʀᴀᴍ ᴠ2", callback_data="pyrogram"),
    ],
    [
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon"),
    ],
    [
        InlineKeyboardButton("ᴩʏʀᴏɢʀᴀᴍ ʙᴏᴛ", callback_data="pyrogram_bot"),
        InlineKeyboardButton("ᴛᴇʟᴇᴛʜᴏɴ ʙᴏᴛ", callback_data="telethon_bot"),
    ],
]


@Client.on_message(filters.private & ~filters.forwarded & filters.command(["generate", "gen", "string", "str"]))
def main(_, msg):
    msg.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))


def generate(update: Update, context: CallbackContext, bot: Client, msg: Message, telethon=False, old_pyro: bool = False, is_bot: bool = False):
    if telethon:
        ty = "ᴛᴇʟᴇᴛʜᴏɴ"
    else:
        ty = "ᴩʏʀᴏɢʀᴀᴍ"
        if not old_pyro:
            ty += " ᴠ2"
    if is_bot:
        ty += " ʙᴏᴛ"
    msg.reply(f"ᴍᴇɴᴄᴏʙᴀ ᴍᴇᴍᴜʟᴀɪ **{ty}** sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ...")
    user_id = msg.chat.id
    api_id_msg = bot.ask(user_id, "ᴍᴇᴍᴘᴇʀᴏsᴇs sᴛʀɪɴɢ...\n\nᴘᴀsᴛᴇ **ᴀᴘɪ_ɪᴅ** ᴅɪʙᴀᴡᴀʜ.", filters=filters.text)
    if cancelled(api_id_msg):
        return
    try:
        api_id = int(api_id_msg.text)
    except ValueError:
        api_id_msg.reply("**ᴀᴘɪ_ɪᴅ** ʜᴀʀᴜs ʙᴇʀᴜᴘᴀ ᴀɴɢᴋᴀ, ᴍᴇᴍᴜʟᴀɪ ᴜʟᴀɴɢ ᴍᴇᴍʙᴜᴀᴛ sᴛʀɪɴɢ.", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    api_hash_msg = bot.ask(user_id, "ᴘᴀsᴛᴇ **ᴀᴘɪ_ʜᴀsʜ** ᴅɪʙᴀᴡᴀʜ", filters=filters.text)
    if cancelled(api_hash_msg):
        return
    api_hash = api_hash_msg.text
    if not is_bot:
        t = "ᴘᴀsᴛᴇ **ᴘʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ᴅᴇɴɢᴀɴ ᴋᴏᴅᴇ ɴᴇɢᴀʀᴀ. \nᴄᴏɴᴛᴏʜ : `+6287654321`'"
    else:
        t = "ᴘᴀsᴛᴇ **ʙᴏᴛ_ᴛᴏᴋᴇɴ** ᴅɪʙᴀᴡᴀʜ. \nᴄᴏɴᴛᴏʜ : `5432198765:abcdanonymousterabaaplol`'"
    phone_number_msg = bot.ask(user_id, t, filters=filters.text)
    if cancelled(phone_number_msg):
        return
    phone_number = phone_number_msg.text
    if not is_bot:
        msg.reply("ᴍᴇɴᴄᴏʙᴀ ᴍᴇɴɢɪʀɪᴍ ᴏᴛᴘ, ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴅɪᴘᴀsᴛᴇ ᴋᴀʟᴏ ᴜᴅᴀʜ ᴍᴀsᴜᴋ...")
    else:
        msg.reply("ᴍᴇɴᴄᴏʙᴀ ʟᴏɢɪɴ ᴠɪᴀ ʙᴏᴛ ᴛᴏᴋᴇɴ...")
    if telethon and is_bot:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif is_bot:
        client = Client(name="bot", api_id=api_id, api_hash=api_hash, bot_token=phone_number, in_memory=True)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="user", api_id=api_id, api_hash=api_hash, in_memory=True)
    client.connect()
    try:
        code = None
        if not is_bot:
            if telethon:
                code = client.send_code_request(phone_number)
            else:
                code = client.send_code(phone_number)
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        msg.reply("**ᴀᴩɪ_ɪᴅ** ᴅᴀɴ **ᴀᴩɪ_ʜᴀsʜ** ᴋᴀᴍᴜ ᴛɪᴅᴀᴋ ᴄᴏᴄᴏᴋ ᴅᴇɴɢᴀɴ ᴋᴏᴍʙɪɴᴀsɪ ᴛᴇʟᴇɢʀᴀᴍ ᴀᴘᴘ. \n\nᴜʟᴀɴɢɪ ᴅᴀʀɪ ᴀᴡᴀʟ ʟᴀɢɪ ᴀᴊᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        msg.reply("ɴᴏᴍᴏʀ **ᴩʜᴏɴᴇ_ɴᴜᴍʙᴇʀ** ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ ᴅɪᴛᴇʟᴇɢʀᴀᴍ.\n\nᴜʟᴀɴɢ ʟᴀɢɪ ᴄᴏʙᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    try:
        phone_code_msg = None
        if not is_bot:
            phone_code_msg = bot.ask(user_id, "ᴘᴀsᴛᴇ **ᴏᴛᴩ** ʏᴀɴɢ ᴜᴅᴀʜ ᴅɪᴛᴇʀɪᴍᴀ ᴅɪʙᴀᴡᴀʜ.\nᴊɪᴋᴀ ᴏᴛᴩ sᴇᴘᴇʀᴛɪ  `12345`, \nɴᴀɴᴛɪ ᴋɪʀɪᴍɴʏᴀ ᴅɪʙᴇʀɪ sᴘᴀsɪ ᴋᴀʏᴀ ɢɪɴɪ `1 2 3 4 5`.", filters=filters.text, timeout=600)
            if cancelled(phone_code_msg):
                return
    except TimeoutError:
        msg.reply("ᴡᴀᴋᴛᴜ ʜᴀʙɪs.\n\nᴜʟᴀɴɢ ᴋᴇᴍʙᴀʟɪ ʟᴀɢɪ ᴀᴊᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return
    if not is_bot:
        phone_code = phone_code_msg.text.replace(" ", "")
        try:
            if telethon:
                client.sign_in(phone_number, phone_code, password=None)
            else:
                client.sign_in(phone_number, code.phone_code_hash, phone_code)
        except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
            msg.reply("ᴏᴛᴘ **sᴀʟᴀʜ.**\n\nᴜʟᴀɴɢ ʟᴀɢɪ ᴀᴊᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
            msg.reply("ᴏᴛᴘ **ᴋᴀᴅᴀʟᴜᴀʀsᴀ**\n\nᴜʟᴀɴɢ ʟᴀɢɪ ᴀᴊᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
            return
        except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
            try:
                two_step_msg = bot.ask(user_id, "ᴘᴀsᴛᴇ **ᴠᴇʀɪꜰɪᴋᴀsɪ ᴅᴜᴀ ʟᴀɴɢᴋᴀʜ** ᴩᴀssᴡᴏʀᴅ ᴅɪʙᴀᴡᴀʜ.", filters=filters.text, timeout=300)
            except TimeoutError:
                msg.reply("ᴡᴀᴋᴛᴜ ʜᴀʙɪs.\n\nᴜʟᴀɴɢ ʟᴀɢɪ ᴀᴊᴀ.", reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
            try:
                password = two_step_msg.text
                if telethon:
                    client.sign_in(password=password)
                else:
                    client.check_password(password=password)
                if cancelled(api_id_msg):
                    return
            except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
                two_step_msg.reply("ᴩᴀssᴡᴏʀᴅ ᴅɪʙᴀᴡᴀʜ.\n\nᴜʟᴀɴɢ ʟᴀɢɪ ᴀᴊᴀ.", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
                return
    else:
        if telethon:
            client.start(bot_token=phone_number)
        else:
            client.sign_in_bot(phone_number)
    if telethon:
        string_session = client.session.save()
    else:
        string_session = client.export_session_string()
    text = f"**sᴇʟᴀᴍᴀᴛ, {ty} sᴛʀɪɴɢ sᴇssɪᴏɴ** \n\n`{string_session}` \n\n**ɢᴇɴᴇʀᴀᴛᴇᴅ ʙʏ :** @someddarbot\n **ɴᴏᴛᴇ :** ɢᴜɴᴀᴋᴀɴ ᴅᴇɴɢᴀɴ ʙɪᴊᴀᴋ ᴅᴀɴ ᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴊᴏɪɴ @somedsupport"
    try:
        if not is_bot:
            client.send_message("me", text)
        else:
            bot.send_message(msg.chat.id, text)
    except KeyError:
        pass
    client.disconnect()
    bot.send_message(msg.chat.id, "ʙᴇʀʜᴀsɪʟ ᴍᴇᴍʙᴜᴀᴛ {} sᴛʀɪɴɢ sᴇssɪᴏɴ.\n\nᴊᴀɴɢᴀɴ ʟᴜᴘᴀ ᴄᴇᴋ ᴘᴇsᴀɴ ᴛᴇʀsɪᴍᴘᴀɴ ᴀᴛᴀᴜ sᴀᴠᴇᴅ ᴍᴇssᴀɢᴇ ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ sᴛʀɪɴɢ sᴇssɪᴏɴ! \n\n**sᴛʀɪɴɢ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ʙʏ** @kenapatagdar".format("ᴛᴇʟᴇᴛʜᴏɴ" if telethon else "ᴩʏʀᴏɢʀᴀᴍ"))


def cancelled(msg):
    if "/cancel" in msg.text:
        msg.reply("**ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴛʀɪɴɢ!**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif "/restart" in msg.text:
        msg.reply("**sᴜᴋsᴇs ᴍᴇʀᴇsᴛᴀʀ ʙᴏᴛ!**", quote=True, reply_markup=InlineKeyboardMarkup(Data.generate_button))
        return True
    elif msg.text.startswith("/"):  # Bot Commands
        msg.reply("**ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs ʙᴇʀᴊᴀʟᴀɴ**", quote=True)
        return True
    else:
        return False
    
    
    GENERATE_HANDLER = DisableAbleCommandHandler("generate", generate, run_async=True)
    
    dispatcher.add_handler(GENERATE_HANDLER)
    
    __mod_name__ = "String"
    __command_list__ = [
    "generate", "string" ]
    __handlers__ = [ GENERATE_HANDLER ]
    
    
     
