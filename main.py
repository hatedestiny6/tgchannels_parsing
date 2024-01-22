from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from config import RECEIVER_1, RECEIVER_2

app = Client("basic", api_id=20443042,
             api_hash="149625d78505443528abdd6fe02519a9")


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


app.run()
