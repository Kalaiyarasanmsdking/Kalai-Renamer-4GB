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
	await message.reply_text(f"𝘼𝙗𝙤𝙪𝙩 𝙈𝙚:\n\n👉🏻𝙏𝙤𝙩𝙖𝙡 𝙐𝙨𝙚𝙧𝙨: {total_user()}\n\n👉🏻𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧: @MsdKalai07\n\n👉🏻𝙁𝙤𝙧 𝙋𝙡𝙖𝙣 𝙐𝙥𝙜𝙧𝙖𝙙𝙚: @MsdKalai07\n\n👉🏻𝘽𝙤𝙩 𝙐𝙥𝙙𝙖𝙩𝙚𝙨: <a href='https://t.me/Kalaibots'> 𝙆𝙖𝙡𝙖𝙞 𝘽𝙤𝙩𝙨 </a>\n\n👉🏻𝙏𝙤𝙩𝙖𝙡 𝙍𝙚𝙣𝙖𝙢𝙚𝙙 𝙁𝙞𝙡𝙚𝙨: {total_rename}\n\n👉𝙏𝙤𝙩𝙖𝙡 𝙎𝙞𝙯𝙚 𝙍𝙚𝙣𝙖𝙢𝙚𝙙: {humanbytes(int(total_size))}\n\n👉𝙎𝙚𝙧𝙫𝙚𝙧: 𝙃𝙚𝙧𝙤𝙠𝙪\n\n👉𝘿𝙖𝙩𝙖𝙗𝙖𝙨𝙚: 𝙈𝙤𝙣𝙜𝙤 𝘿𝘽\n\n𝐓𝐡𝐚𝐧𝐤 𝐘𝐨𝐮 𝐅𝐨𝐫 𝐔𝐬𝐢𝐧𝐠 𝐌𝐞",quote=True)
