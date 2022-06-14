from pyrogram import Client as bot, filters
from Bot.buttons import start_btn
from Bot.database import db
from Bot.languages import lang

@bot.on_message (filters.private & filters.command ("start"))
async def start_ (c, m):
  if not db.get_user (m.chat.id)["exist"]:
    db.save_user (m.chat.id)
    
  await m.reply (lang.reply ("start"), reply_markup = start_btn)
  
