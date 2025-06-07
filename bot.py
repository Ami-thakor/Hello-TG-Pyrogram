from pyrogram import Client, filters

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

app = Client("hello_bot", bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello, World!")

app.run()
