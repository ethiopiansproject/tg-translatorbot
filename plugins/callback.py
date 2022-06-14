from pyrogram import Client as bot, filters
from Bot.buttons import trt_btn
from Bot.config import lang_list
from googletrans import Translator

@bot.on_callback_query ()
async def callback_ (c, m):

  if m.data == "close":
    await m.message.delete()
  elif m.data in lang_list:
    try:
      trt = Translator()
      if not m.message.reply_to_message:
        await m.answer (lang.reply ("msg_not_found"))
      else:
        await m.message.edit_text (trt.translate (dest = m.data, text = m.message.reply_to_message.text).text, reply_markup = trt_btn)
    except Exception as e:
      print (e)
  else:
    pass
