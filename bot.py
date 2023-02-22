import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5973374893:AAE8zwUb1aNLi3FcadGxfmlQ2x5cMrBRueY")

API_ID = int(os.environ.get("API_ID", "17987030"))

API_HASH = os.environ.get("API_HASH", "5af8937f55296f31cfa92e510ece500f")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))

MS_PIC = os.environ.get("MS_PIC", "")
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
