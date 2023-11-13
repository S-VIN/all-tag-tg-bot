from pyrogram import Client
from pyrogram import filters
import settings

app = Client(
    "all_tag_tg_bot",
    api_id=settings.API_ID, api_hash=settings.API_HASH,
    bot_token=settings.BOT_TOKEN
)

@app.on_message(filters.text)
async def echo(client, message):
    usernames_string = ''
    async for member in app.get_chat_members(message.chat.id):
        if member.user.username != 'all_tag_tg_bot':
            usernames_string += '@' + member.user.username + ' '
    print(usernames_string)

    if '@all' in message.text:
        await app.send_message(chat_id=message.chat.id, text=usernames_string)
        print(message.text)

app.run()

