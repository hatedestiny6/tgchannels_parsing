import json

from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto, Photo
from pyrogram.enums import ParseMode

import re

# get data from json file
with open('data.json') as json_file:
    data = json.load(json_file)

app = Client("basic", api_id=data["api_id"],
             api_hash=data["api_hash"])

lm = -1

RECEIVER_1 = data["RECEIVER_1"]
RECEIVER_2 = data["RECEIVER_2"]


def remove_urls(text, replacement_text="[URL_REMOVED]"):
    # Define a regex pattern to match URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Use the sub() method to replace URLs with the specified replacement text
    text_without_urls = url_pattern.sub(replacement_text, text)

    return text_without_urls


def filter_msg(text):
    url = get_urls(text)

    if url:
        for elem in data["links"]:
            if elem in url:
                return False

    return True


def get_urls(text):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    try:
        url = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)[0]

    except IndexError:
        return False

    return url


@app.on_message(filters.channel)
async def log(client, message: Message):
    global lm

    # where the message came from
    source = f"{message.link[:message.link.rfind('/')]}"

    if message.media_group_id:
        if message.media_group_id != lm:
            lm = message.media_group_id

            msg_group = await app.get_media_group(
                chat_id=message.chat.id, message_id=message.id)

            if not filter_msg(msg_group[0].caption):
                return

            msg_group[0].caption = msg_group[0].caption + \
                f"\n\n<a href='{source}'>ИСТОЧНИК</a>" if msg_group[0].caption \
                else f"\n\n<a href='{source}'>ИСТОЧНИК</a>"

            media_group = []

            for msg in msg_group:
                img = InputMediaPhoto(msg.photo.file_id, caption=msg.caption)
                media_group.append(img)

            await app.send_media_group(RECEIVER_1,
                                       media=media_group)

    else:
        if message.text:
            if not filter_msg(message.text):
                return

            message_text = message.text + \
                f"\n\n<a href='{source}'>ИСТОЧНИК</a>"

            await app.send_message(RECEIVER_1,
                                   message_text,
                                   parse_mode=ParseMode.HTML,
                                   disable_web_page_preview=True)

        elif message.caption:
            if not filter_msg(message.caption):
                return

            message_text = message.caption + \
                f"\n\n<a href='{source}'>ИСТОЧНИК</a>"

            await app.send_photo(RECEIVER_1, message.photo.file_id, caption=message_text)

        else:
            message_text = f"\n\n<a href='{source}'>ИСТОЧНИК</a>"
            await app.send_photo(RECEIVER_1, message.photo.file_id, caption=message_text)

    async for msg in app.get_chat_history(RECEIVER_1, limit=1, offset_id=-1):
        lm = -1
        source = f"{msg.link[:msg.link.rfind('/')]}"
        message_link = msg.link

    # send messages to receiver 2
    if message.media_group_id:
        if message.media_group_id != lm:
            lm = message.media_group_id

            msg_group = await app.get_media_group(
                chat_id=message.chat.id, message_id=message.id)

            media_group = []

            for msg in msg_group:
                if msg.caption:
                    ready_txt = [s.strip() for s in remove_urls(
                        msg.caption).strip().split("[URL_REMOVED]")]
                    message_caption = '\n\n'.join(ready_txt)[:150].removesuffix("ИСТОЧНИК").strip() + \
                        f"...\n\n<a href='{source}'>ИСТОЧНИК</a> 👉 " + \
                        f"<a href='{message_link}'>ПОДРОБНОСТИ</a>"

                    await app.send_message(RECEIVER_2,
                                           text=message_caption)
                    return

        else:
            return

    else:
        if message.text:
            ready_txt = [s.strip() for s in remove_urls(
                message.text).strip().split("[URL_REMOVED]")]
            message_text = '\n\n'.join(ready_txt)[:150].removesuffix("ИСТОЧНИК").strip() + \
                f"...\n\n<a href='{source}'>ИСТОЧНИК</a> 👉 " + \
                f"<a href='{message_link}'>ПОДРОБНОСТИ</a>"

            await app.send_message(RECEIVER_2,
                                   message_text,
                                   disable_web_page_preview=True)

        elif message.caption:
            ready_txt = [s.strip() for s in remove_urls(
                message.caption).strip().split("[URL_REMOVED]")]
            message_text = '\n\n'.join(ready_txt)[:150].removesuffix("ИСТОЧНИК").strip() + \
                f"...\n\n<a href='{source}'>ИСТОЧНИК</a> 👉 " + \
                f"<a href='{message_link}'>ПОДРОБНОСТИ</a>"

            await app.send_message(RECEIVER_2, message_text,
                                   disable_web_page_preview=True)


print("Успешный запуск!")
app.run()
