"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 5GB
	Price 0
	
	_____________________________
	**It's Support 4GB File Rename**
	**VIP 1 ** 
	Daily  Upload  limit 20GB
	Price Rs 25 🇮🇳/🌎 0.40$  per Month
	
	**VIP 2 **
	Daily Upload limit 1O0GB
	Price Rs 40  🇮🇳/🌎 0.6$  per Month
	
	
	Pay Using Upi I'd ```ultrabots.famc@idfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aaajats")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/ajak4405")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
