
from pyrogram import Client
from Bot.config import api_id, api_hash, bot_token

bot = Client (
    api_id = api_id,
    api_hash = api_hash,
    bot_token = bot_token,
    name = "Trtbot",
    plugins = {
        "root": "plugins"
    }
)

bot.run()
