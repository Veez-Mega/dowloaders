from pyrogram import filters, Client
import pyrogram
import requests



@Client.on_message(filters.text & ~filters.command("igdown"))
def download(client, message):
    instagram_post = message.text

    if "instagram.com" in instagram_post:
        changing_url = instagram_post.split("/")
        url_code = changing_url[4]
        url = f"https://instagram.com/p/{url_code}?__a=1"
        try:
            visit = requests.get(url).json()
            checking_video = visit['graphql']['shortcode_media']['is_video']
        except:
            client.send_message(chat_id=message.chat.id, text="Send Me Only Public Instagram Posts ⚡️")
            return
        
        if checking_video:
            try:
                video_url = visit['graphql']['shortcode_media']['video_url']
                client.send_chat_action(chat_id=message.chat.id, action="upload_video")
                client.send_video(chat_id=message.chat.id, video=video_url)
            except:
                pass
        else:
            try:
                post_url = visit['graphql']['shortcode_media']['display_url']
                client.send_chat_action(chat_id=message.chat.id, action="upload_photo")
                client.send_photo(chat_id=message.chat.id, photo=post_url)
            except:
                pass
    else:
        client.send_message(chat_id=message.chat.id, text="Kindly Send Me Public Instagram Video/Photo Url")
