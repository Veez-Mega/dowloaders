from pyrogram import Client, filters, idle
from config.config import API_ID, API_HASH, BOT_TOKEN

downloader = Client(
           ":download:",
           API_ID,
           API_HASH,
           BOT_TOKEN,
           plugins=dict(root="plugins.modules") 
)

print("Bot started!")
downloader.start()
idle()
