from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram import Client, filters

start_keyboard = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Commands", callback_data="help"),
       ],[
       InlineKeyboardButton("Group", url="t.me/VeezSupportGroup"),
       InlineKeyboardButton("Updates", url="t.me/levinachannel"),
       ]]
       )
start_keyboard = InlineKeyboardMarkup( [[
       InlineKeyboardButton("Instagram", callback_data="help"),
       ],[
       InlineKeyboardButton("Youtube", callback_data="yt"),
       InlineKeyboardButton("Porn", callback_data="porn"),
       ],[
       InlineKeyboardButton("Movies", callback_data="movies"),
       InlineKeyboardButton("Animes", callback_data="anime"),
       ]]
       )
    


@Client.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_photo(
        photo=f"https://graph.org/file/a9541f28afea293440abf.png",
        caption=f"Hello {message.from_user.mention()}\n\nIam a veez downloader bot i can download all things here you can download any one by simple for more click /help and see in below help button.\n\nDeveloped By: @my_name_is_nobitha\nManaged By: @VeezSupportGroup & @levinachannel.",
        reply_markup=start_keyboard
    )

@Client.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text("Here is the help menu of the bot!", reply_markup=help_keyboard)
