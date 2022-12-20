"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 0GB
	Price 0
	
	_____________________________
	**It's Support 4GB File Rename**
	**VIP 1 ** 
	Daily  Upload  limit 20GB
	Price Rs 40 🇮🇳/🌎 4$  per Month
	
	**VIP 2 **
	Daily Upload limit 1O0GB
	Price Rs 60  🇮🇳/🌎 6$  per Month
	
	
	Pay Using Upi I'd ```ultrabots.famc@idfcbank```
	
	After Payment Send Screenshots Of 
        Payment To Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Aaajats")], 
        			[InlineKeyboardButton("PayPal 🌎",url = "https://www.paypal.me/ajak4406")],
		                [InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
