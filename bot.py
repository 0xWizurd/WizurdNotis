from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

# Telegram Bot Token (replace with your token)
BOT_TOKEN = "7721831643:AAG88-36ESUrAE9-FmD6vXiT82Gz3qP_18o"

# Chat IDs
SOURCE_CHAT_ID = -1002396313378  # Replace with the source chat ID
TARGET_CHAT_ID = -1002264069335  # Replace with the target chat ID

# Allowed usernames to forward messages from
ALLOWED_SENDERS = [1163373079]

# Initialize Flask app and Telegram bot
app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

@app.route("/", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id

    # Check if the message is from the source chat
    if chat_id == SOURCE_CHAT_ID:
        sender_username = update.message.from_user.username

        # Check if the sender is allowed
        if sender_username in ALLOWED_SENDERS:
            # Forward the message to the target chat
            bot.send_message(chat_id=TARGET_CHAT_ID, text=update.message.text)
    
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
