from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from Bot.config import lang_list

close_btn = InlineKeyboardButton (text = "close", callback_data = "close:")
start_btn = InlineKeyboardMarkup ([
    [InlineKeyboardButton (text = "group", url = "https://t.me/Ethiopians_project"),
    InlineKeyboardButton (text = "channel", url = "https://t.me/Ethiopiansproject")]
])

trt_btn = []

for i in lang_list:

  trt_btn.append ([InlineKeyboardButton (text = lang_list [i], callback_data = i)])

trt_btn = InlineKeyboardMarkup (trt_btn)
