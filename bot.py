#basic google translator bot
import os
from telegram import*
from telegram.ext import*
from googletrans import Translator

bot_token = os.getenv[BOT_TOKEN]
def start(update,context):
 user_info = update.effective_user
 update.message.reply_markdown_v2(f'ሠላም ውድ {user_info.mention_markdown_v2()} የተለያዩ ቋንቋዎችን ወደ አማርኛ መቶርጎም እችላለው😊\nየፈለጋችሁትን ፅፈት ላኩልኝ፣መልካም ግዜ🤗')
           
def translate_text(update,context):
    id = update.message.chat_id
    user_msg = update.message.text
    translator = Translator()
    translation = translator.translate(user_msg,dest='am')
    context.bot.sendChatAction(update.message.chat_id, 'typing')
    update.message.reply_html(f'''
<b>{translation.text}</b> 
<code>\nPowered by @The_ep </code>''',quote=True)
   
updater = Updater(os.getenv("BOT_TOKEN"))

dp = updater.dispatcher
dp.add_handler(CommandHandler('start',start))
dp.add_handler(MessageHandler(Filters.text,translate_text))
updater.start_polling()
updater.idle()
