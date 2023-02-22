import os
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit , usertype,addpre
ADMIN = int(os.environ.get("ADMIN", 1478641169))
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["warn"]))
async def warn(c, m):
        if len(m.command) >= 3:
            try:
                user_id = m.text.split(' ', 2)[1]
                reason = m.text.split(' ', 2)[2]
                await m.reply_text("User Notfied Sucessfully")
                await c.send_message(chat_id=int(user_id), text=reason)
            except:
                 await m.reply_text("User Not Notfied Sucessfully 😔") 


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["addpremium"]))
async def buypremium(bot, message):
	await message.reply_text("𝐒𝐞𝐥𝐞𝐜𝐭 𝐘𝐨𝐮𝐫 𝐏𝐥𝐚𝐧 𝐅𝐫𝐨𝐦 𝐁𝐞𝐥𝐨𝐰 👇🏻",quote=True,reply_markup=InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("VIP",callback_data = "vip") ]]))
        			

@Client.on_callback_query(filters.regex('vip'))
async def vip(bot,update):
	id = update.message.reply_to_message.text.split("/addpremium")
	user_id = id[1].replace(" ", "")
	inlimit  = 10737418240000
	uploadlimit(int(user_id),10737418240000)
	usertype(int(user_id),"VIP")
	addpre(int(user_id))
	await update.message.edit("⚡️ 𝙐𝙨𝙚𝙧 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡𝙡𝙮 𝙐𝙥𝙜𝙧𝙖𝙙𝙚𝙙 𝙏𝙤 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝙐𝙨𝙚𝙧 ⭐️")
	await bot.send_message(user_id,"⚡️ 𝙃𝙚𝙮 𝙪𝙧 𝙣𝙤𝙬 𝙪𝙥𝙜𝙧𝙖𝙙𝙚𝙙 𝙩𝙤 𝙑𝙄𝙋 𝙪𝙨𝙚𝙧 𝙘𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙥𝙡𝙖𝙣 𝙝𝙚𝙧𝙚 👉🏻 /myplan")
	
@Client.on_callback_query(filters.regex('dft'))
async def dft(bot,update):
	id = update.message.reply_to_message.text.split("/resetpower")
	user_id = id[1].replace(" ", "")
	inlimit = 2147483648
	uploadlimit(int(user_id), 2147483648)
	usertype(int(user_id),"**Free**")
	addpre(int(user_id))
	await update.message.edit("𝘿𝙖𝙞𝙡𝙮 𝘿𝙖𝙩𝙖 𝙡𝙞𝙢𝙞𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙧𝙚𝙨𝙚𝙩 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙨𝙛𝙪𝙡𝙡𝙮 😐\n𝙏𝙝𝙞𝙨 𝙖𝙘𝙘𝙤𝙪𝙣𝙩 𝙝𝙖𝙨 𝙙𝙚𝙛𝙖𝙪𝙡𝙩 2 𝙂𝘽 𝙧𝙚𝙣𝙖𝙢𝙞𝙣𝙜 𝙘𝙖𝙥𝙖𝙘𝙞𝙩𝙮 😊")
	await bot.send_message(user_id,"𝙔𝙤𝙪𝙧 𝘿𝙖𝙞𝙡𝙮 𝘿𝙖𝙩𝙖 𝙡𝙞𝙢𝙞𝙩 𝙝𝙖𝙨 𝙗𝙚𝙚𝙣 𝙧𝙚𝙨𝙚𝙩 𝙨𝙪𝙘𝙘𝙚𝙨𝙨𝙨𝙛𝙪𝙡𝙡𝙮 😐\n\n𝙘𝙝𝙚𝙘𝙠 𝙮𝙤𝙪𝙧 𝙥𝙡𝙖𝙣 𝙝𝙚𝙧𝙚 👉 /myplan\n- 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 𝘼𝙙𝙢𝙞𝙣 🧑🏻‍🦱<a href='https://t.me/mrmalik_offl'>**Mr Malik**</a>🧑🏻‍🦱")

