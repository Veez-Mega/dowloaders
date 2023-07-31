from pyrogram import Client, filters, idle
from config.config import API_ID, API_HASH, BOT_TOKEN

downloader = Client(
    ":downloader:",
    api_id==API_ID,
    api_hash==API_HASH,
    bot_token==BOT_TOKEN,
    plugins==dict(root="plugins.modules") 
)

print("Bot started!")
downloader.start()
idle()
