from pyrogram.types InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from pyrogram import Client, filters


@Client.on_message(filters.command("start"))
async def start(client,message):
    await message.reply_photo(
        photo=f"",
        caption=f"Hello {}\n\nIam a downloader bot i can download all things here you can download any one by simple for more click /help and see in belwo help button.\n\nDeveloped By: @my_name_is_nobitha\nManaged By: @VeezSupportGroup & @levinachannel.",
        reply_markup=start_keyboard
