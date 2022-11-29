import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "5711444830:AAFWygViv4a0Tbu9WRZJfcVaiOAmv3TaZYA")

API_ID = int(os.environ.get("API_ID", "23560088"))

API_HASH = os.environ.get("API_HASH", "999c01704d5c417749a98f4b8785fe88")

STRING = os.environ.get("STRING", "BQEOqKoAqQvHmoAVkpuXZhnXcV2AmZtcoGp0-qXuEQmWpd5zsTwZlAuPEHSmbsOjb3wkBXJzkoqg7S5oeFou7-zUoa1SAu776tTxIk8YORVJ6nNU9HY_X_1gnNJlUZ4zV-MxnA_wFWY9k8HTlTSzNPpUkNjo7i16ZbMWjv9Fh1U2Q5NzIGzWjcK1RIB2oUw-g5E6wys-U5b4DrnlCnOVZje6c_nB0Jpx4X2YJjJH0ZUui9KPXnbHIjd_QM0QYYSPoS5odI3McXxEAjSfII2GYjPlHjhT-hMH2irFCehq3MU8DhsVGgiY0WgPhbJL6qYrctnUP43hQvr1jN4gFFvdmD6L4zMNcgAAAABvJ4dUAA")


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
