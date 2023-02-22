import os 
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup)
token = os.environ.get('TOKEN','5973374893:AAE8zwUb1aNLi3FcadGxfmlQ2x5cMrBRueY')
botid = token.split(':')[0]
ADMIN = int(os.environ.get("ADMIN", "1478641169"))

from helper.database import botdata, find_one, total_user,getid

from helper.progress import humanbytes

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["msusers"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	id = str(getid())
	ids = id.split(',')

	await message.reply_text(f"⚡️ All IDS : {ids}\n\n⚡️ Total User :- {total_user()}\n\n⚡️ Total Renamed File :- {total_rename}\n⚡️ Total Size Renamed :- {humanbytes(int(total_size))}",quote=True,
                             reply_markup= InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Close Menu 🦋", callback_data="cancel")]]) 
                             )
