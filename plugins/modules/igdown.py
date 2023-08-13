from pyrogram import filters, Client
import pyrogram
import requests



@Client.on_message(filters.command("igdown") & filters.regex(r'https?://(?:www\.)?instagram\.com/p/[-_a-zA-Z0-9]+/?'))
def download(client, message):
    print("Received igdown command")
    instagram_post = message.text.split(" ", 1)[1]

    changing_url = instagram_post.split("/")
    url_code = changing_url[4]
    url = f"https://instagram.com/p/{url_code}?__a=1"
    
    try:
        visit = requests.get(url).json()
        checking_video = visit['graphql']['shortcode_media']['is_video']
    except Exception as e:
        print("Error:", e)
        client.send_message(chat_id=message.chat.id, text="Send Me Only Public Instagram Posts ⚡️")
        return
        
    if checking_video:
        try:
            video_url = visit['graphql']['shortcode_media']['video_url']
            print("Downloading video:", video_url)
            client.send_chat_action(chat_id=message.chat.id, action="upload_video")
            client.send_video(chat_id=message.chat.id, video=video_url)
        except Exception as e:
            print("Error downloading video:", e)
            pass
    else:
        try:
            post_url = visit['graphql']['shortcode_media']['display_url']
            print("Downloading photo:", post_url)
            client.send_chat_action(chat_id=message.chat.id, action="upload_photo")
            client.send_photo(chat_id=message.chat.id, photo=post_url)
        except Exception as e:
            print("Error downloading photo:", e)
            pass
