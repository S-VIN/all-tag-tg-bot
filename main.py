from pyrogram import Client
from pyrogram import filters
import config

app = Client(
    "all_tag_tg_bot",
    api_id=config.API_ID, api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

async def send_message(old_message):
    usernames_string = ''
    async for member in app.get_chat_members(old_message.chat.id):
        if member.user.username != 'all_tag_tg_bot':
            usernames_string += '@' + member.user.username + ' '
    print(usernames_string)

    await app.send_message(chat_id=old_message.chat.id, text=usernames_string)
    print(old_message.text)


@app.on_message(filters.text)
async def echo(client, message):
    words = message.text.split()

    for word in words:
        if word == '@all':
            await send_message(message)
            return

app.run()

