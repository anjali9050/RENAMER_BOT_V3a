import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5552531861:AAFIAB4cR8-OZMuQxR3Wi4IgBi5mTX_gfIs")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQDDu_I83eU-6C5YAT_slJQCK6dneR5JVRsEcuJknJkMYBuPqvPi68k0JSpCYbb9nhTGWWxtOfXVBZHWinNbhinvSBcHvhOTz7XsWxmw8oX2fQJKEM3MB2Jd2-pGqu5R19I40G_agAZssP3GQNh_4tkldM93nLrCgInFd7M74unogupAnbchFb5tk_FHdA5StapFBI5V5EAruciBs3ZS4Vj2JKSEBeByVjjoWLCyiSfjSZ1otSkSLeH_4_DbbaJT2XGTnBginNWlwCIE8Mqt7yPJ7qDNFlF1Y9xWVYH489AfOZNf_72futOEc0Xjep9Xg1KRRVgjL-z1L9l6zAkawwg_AAAAAG8nh1QA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
