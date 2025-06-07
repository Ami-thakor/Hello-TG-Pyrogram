from pyrogram import Client, filters

# Replace with your bot token
BOT_TOKEN = "5696074673:AAFSjLPwlYT6usWNs4e5XGFqe94PSq9PK98"

app = Client("hello_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello, World!")

app.run()
