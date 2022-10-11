import EmikoRobot
import logging
from pyrogram import Client, idle
from pyrogram import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "bot",
    api_id=EmikoRobot.API_ID,
    api_hash=EmikoRobot.API_HASH,
    bot_token=EmikoRobot.BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="EmikoRobot"),
)


if __name__ == "__main__":
    print("Starting the String Generator Bot...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"@{uname} started successfully !")
    idle()
    app.stop()
    print("Bot stopped. Bye !")
