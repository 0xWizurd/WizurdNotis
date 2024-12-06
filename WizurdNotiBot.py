from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    MessageHandler,
    filters,
    CallbackContext,
)

# Replace with your bot token
BOT_TOKEN = "7721831643:AAG88-36ESUrAE9-FmD6vXiT82Gz3qP_18o"
SOURCE_CHAT_ID = -1002396313378  # Replace with the source chat ID
TARGET_CHAT_ID = -1002264069335  # Replace with the target chat ID

# List of user IDs to monitor
MONITORED_USERS = [1163373079]  # Replace with the user IDs of accounts to monitor

async def forward_message(update: Update, context: CallbackContext):
    # Check if the message is from the source chat and from a monitored user
    if update.effective_chat.id == SOURCE_CHAT_ID and update.effective_user.id in MONITORED_USERS:
        # Forward the message to the target chat
        await context.bot.forward_message(
            chat_id=TARGET_CHAT_ID,
            from_chat_id=update.effective_chat.id,
            message_id=update.message.message_id
        )

def main():
    # Initialize the bot application
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Add a message handler to monitor messages
    app.add_handler(
        MessageHandler(
            filters.Chat(SOURCE_CHAT_ID) & filters.User(user_id=MONITORED_USERS),
            forward_message
        )
    )

    # Start the bot
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
