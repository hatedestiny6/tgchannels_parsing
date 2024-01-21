from pyrogram import Client, filters
from pyrogram.types import Message

app = Client("basic", api_id=20443042,
             api_hash="149625d78505443528abdd6fe02519a9")


@app.on_message(filters.channel)
async def log(client, message: Message):
    # await app.forward_messages(-1002088925993, message.chat.id, message.id)
    source = message.sender_chat.title
    # print("========")
    # print(message.text.markdown)
    # print("Source:", source)
    # print("========")
    # await message.edit_text(message.text + f"\n\nSource: {source}")

    # try:
    # await message.edit_text(message.text + f"\n\nSource: {source}")
    message.text = "PENJS"

    # except TypeError:
    #     print("penis")

    #     message['caption'] message.caption + f"\n\nSource: {source}")

    await app.copy_message(message.chat.id, -1002088925993, message.id)


app.run()
