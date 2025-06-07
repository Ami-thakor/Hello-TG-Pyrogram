from pyrogram import Client, filters
import time, os
# Replace with your bot token
API_ID = 28160559
API_HASH = "ca5085c3f41b16df46dbeebed6e56081"

BOT_TOKEN = "5696074673:AAFSjLPwlYT6usWNs4e5XGFqe94PSq9PK98"

app = Client("hello_bot", bot_token=BOT_TOKEN, api_id=API_ID,
    api_hash=API_HASH)

@app.on_message(filters.command("ping"))
async def ping_handler(client, message):
    start = time.time()
    m = await message.reply_text("Pinging...")
    end = time.time()
    latency = round((end - start) * 1000)  # in milliseconds
    await m.edit_text(f"🏓 Pong! `{latency}ms`")


@app.on_message(filters.command("start"))
async def start_handler(client, message):
    await message.reply("Hello, World!")

app.run()
