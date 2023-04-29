import emoji
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

emojiList = ['😀', '😁', '🤣', '😃', '😄', '😅', '😆', '😉', '😊', '😋', '😎', '😍', '😘', '😗', '🖕','🤗','🫡']

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def emoji_reaction(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    user_txt = message.text.lower()

    if user_txt == 'mandana':
        emojiRes = '❤️'
    elif user_txt == 'mobina':
        emojiRes = '🖕'
    elif user_txt == 'akbar':
        emojiRes = '😎'
    elif user_txt == 'sralak':
        emojiRes = '🫡'
        
    else:
        emojiRes = random.choice(emojiList)
        
    await context.bot.send_message(chat_id= update.message.chat_id, text= emojiRes)

if __name__ == '__main__':
    application = ApplicationBuilder().token('6260669675:AAEOvGALgH2GA38a_HnODfPH1aWwhj9X9bU').build()
    
    start_handler = CommandHandler('start', start)
    reaction_handler = MessageHandler(filters.TEXT, emoji_reaction)


    application.add_handler(start_handler)
    application.add_handler(reaction_handler)
    
    application.run_polling()