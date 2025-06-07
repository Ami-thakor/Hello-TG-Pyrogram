# Use a slim Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pyrogram tgcrypto

# Run the bot
CMD ["python", "bot.py"]
