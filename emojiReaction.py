import telegram
import random
import emoji
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ApplicationBuilder

# Define your bot's token
TOKEN = '6260669675:AAEOvGALgH2GA38a_HnODfPH1aWwhj9X9bU'

# Create an updater for your bot
# updater = Updater(TOKEN, use_context=True)

# Define a function to handle the /start command
async def start(update, context):
    await context.bot.send_message(chat_id=update.message.chat_id, text='Hi! I am a bot that can respond with emojis. Please send me a name.')

# Define a function to handle messages
async def handle_message(update, context):
    # Get the message text and convert it to lowercase
    message_text = await update.message.text.lower()
    
    # Check if the message text matches a name
    if message_text == 'mandana':
        emojiRes = '❤️'
    elif message_text == 'mobina':
        emojiRes = 'middle finger'
    elif message_text == 'akbar':
        emojiRes = '😎'
    else:
        emojRes = emoji.get_emoji_regexp()
    
    # Send the response with the appropriate emoji
    await context.bot.send_message(chat_id=update.message.chat_id, text=emojiRes)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()


# Add handlers for the /start command and messages
# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(MessageHandler(filters.text, handle_message))

# # Start the bot
# updater.start_polling()
# updater.idle()