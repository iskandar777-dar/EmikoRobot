from pyrogram.types import Message
from pyrogram import Client, filters

from EmikoRobot import OWNER_ID
from EmikoRobot.modules.db import SESSION
from EmikoRobot.modules.db.users_sql import Users, num_users

def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()

def _stats(_, msg: Message):
    users = num_users()
    msg.reply(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)

STATS_HANDLER = DisableAbleCommandHandler("stats", stats, run_async=True)

dispatcher.add_handler(STATS_HANDLER)
