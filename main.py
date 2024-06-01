from pyrogram import Client
from pyrogram import filters
import config

app = Client(
    "all_tag_tg_bot",
    api_id=config.API_ID, api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

@app.on_message(filters.text)
async def echo(client, message):
    if '@all' in message.text:
        if len(message.text) > 4:
            if message.text[4] != ' ':
                return

        usernames_string = ''
        async for member in app.get_chat_members(message.chat.id):
            if member.user.username != 'all_tag_tg_bot':
                usernames_string += '@' + member.user.username + ' '
        print(usernames_string)

        await app.send_message(chat_id=message.chat.id, text=usernames_string)
        print(message.text)

app.run()

