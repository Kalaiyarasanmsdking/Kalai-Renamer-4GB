import os 
from pyrogram import Client, filters
token = os.environ.get('TOKEN','5973374893:AAE8zwUb1aNLi3FcadGxfmlQ2x5cMrBRueY')
botid = token.split(':')[0]
from helper.database import botdata, find_one, total_user
from helper.progress import humanbytes
@Client.on_message(filters.private & filters.command(["about"]))
async def start(client,message):
	botdata(int(botid))
	data = find_one(int(botid))
	total_rename = data["total_rename"]
	total_size = data["total_size"]
	await message.reply_text(f"š¼šš¤šŖš© šš:\n\nšš»šš¤š©šš” ššØšš§šØ: {total_user()}\n\nšš»šæšš«šš”š¤š„šš§: @MsdKalai07\n\nšš»šš¤š§ šš”šš£ šš„šš§ššš: @MsdKalai07\n\nšš»š½š¤š© šš„ššš©ššØ: <a href='https://t.me/Kalaibots'> ššš”šš š½š¤š©šØ </a>\n\nšš»šš¤š©šš” ššš£šš¢šš ššš”ššØ: {total_rename}\n\nššš¤š©šš” šššÆš ššš£šš¢šš: {humanbytes(int(total_size))}\n\nšššš§š«šš§: ššš§š¤š šŖ\n\nššæšš©ššššØš: šš¤š£šš¤ šæš½\n\nšš”šš§š¤ ššØš® ššØš« šš¬š¢š§š  šš",quote=True)
