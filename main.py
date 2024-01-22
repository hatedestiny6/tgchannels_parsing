import json

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode


# get data from json file
with open('data.json') as json_file:
    data = json.load(json_file)

app = Client("basic", api_id=data["api_id"],
             api_hash=data["api_hash"])

RECEIVER_1 = data["RECEIVER_1"]
RECEIVER_2 = data["RECEIVER_2"]


@app.on_message(filters.channel)
async def log(client, message: Message):
    # where the message came from
    source = f"{message.link[:message.link.rfind('/')]}"

    # for example, the second picture in the message
    # corresponds to this condition
    if not message.text and not message.caption:
        pass

    else:
        # we need to find out does the message contain
        # attachments or is it just text
        if message.text:
            message_text = message.text + \
                f"\n\n<a href='{source}'>ИСТОЧНИК</a>"

        elif message.caption:
            message_text = message.caption + \
                f"\n\n<a href='{source}'>ИСТОЧНИК</a>"

        # send message to the receiver 1
        await app.send_message(RECEIVER_1,
                               message_text,
                               parse_mode=ParseMode.HTML)

        # send messages to receiver 2
        if message.text:
            message_text = '\n'.join(message.text.strip().split("\n")[:2]) + \
                f"...\n\n<a href='{source}'>ИСТОЧНИК</a> 👉 " + \
                f"<a href='{message.link}'>ПОДРОБНОСТИ</a>"

        elif message.caption:
            message_text = '\n'.join(message.caption.strip().split("\n")[:2]) + \
                f"...\n\n<a href='{source}'>ИСТОЧНИК</a> 👉 " + \
                f"<a href='{message.link}'>ПОДРОБНОСТИ</a>"

        await app.send_message(RECEIVER_2,
                               message_text)


print("Успешный запуск!")
app.run()
