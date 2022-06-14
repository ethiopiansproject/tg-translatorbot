from pyrogram import filters
from Bot.config import admin_id

def admin_filter (_, __, m):

  return m.chat.id == admin_id

admin = filters.create (admin_filter)
