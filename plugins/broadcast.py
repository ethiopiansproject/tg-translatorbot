from pyrogram import Client as bot, filters
from Bot.languages import lang
from Bot.database import db
from Bot.filters import admin

@bot.on_message (filters.private & admin & filters.command ("broadcast"))
async def broadcast_ (c, m):
  usr = db.get_all_users ()
  txt = m.text.replace ("/broadcast ", "")

  if txt == m.text:
    await m.reply (lang.reply ("brd_fail"))
  else:
    total = db.get_user()["length"]
    failed = 0
    sent = 0
    msg = await m.reply (lang.reply ("brd"))
    for i in usr:
      try:
        await c.send_message (i["id"], txt)
        sent += 1
      except:
        failed += 1
      finally:
        await msg.edit_text (lang.reply ("brd_msg").format (total, sent, failed))
