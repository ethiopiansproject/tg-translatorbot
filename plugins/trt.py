from pyrogram import Client as bot, filters
from Bot.buttons import trt_btn
from Bot.languages import lang

@bot.on_message (filters.private & ~filters.command (["start", "broadcast"]))
async def trt_ (c, m):

  await m.reply (m.text, quote = True, reply_markup = trt_btn)
