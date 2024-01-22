from pyrogram import Client, filters
from pyrogram.types import Message

from config import RECEIVER_1, RECEIVER_2

app = Client("basic", api_id=20443042,
             api_hash="149625d78505443528abdd6fe02519a9")


@app.on_message(filters.channel)
async def log(client, message: Message):
    # where the message came from
    source = f"https://t.me/c/{message.chat.id}"

    # for example, the second picture in the message
    # corresponds to this condition
    if not message.text and not message.caption:
        pass

    else:
        # we need to find out does the message contain
        # attachments or is it just text
        if message.text:
            message.text = message.text + f"\n\nSource: {source}"

        elif message.caption:
            message.caption = message.caption + f"\n\nSource: {source}"

        # send message to the receiver 1
        await app.send_message(RECEIVER_1,
                               message.text if message.text
                               else message.caption)

        # TODO: send messages to receiver 2

        # message_text =

        # await app.send_message(RECEIVER_2,
        #                        f"{message.text[:2]}..." if message.text
        #                        else f"{message.caption[:2]}...")


app.run()
