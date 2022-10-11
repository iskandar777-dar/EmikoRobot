from EmikoRobot import SUPPORT_CHAT
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
def must_join_channel(bot: Client, msg: Message):
    if not SUPPORT_CHAT:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(SUPPORT_CHAT, msg.from_user.id)
        except UserNotParticipant:
            if SUPPORT_CHAT.isalpha():
                link = "https://t.me/" + SUPPORT_CHAT
            else:
                chat_info = await bot.get_chat(SUPPORT_CHAT)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/ba582d379f2586f227d66.png", caption=f"Gabung Group dibawah dulu lalu coba /string lagi!",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 Gabung Group Sini 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the SUPPORT_CHAT chat : {SUPPORT_CHAT} !")
