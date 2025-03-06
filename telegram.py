import telebot

# Bot Token
Token = "7721846695:AAGHQfoiF1VDzAEOb1Lu9HKWwJoUBgjDU3E"

bot = telebot.TeleBot(Token)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'NAMASTE! Welcome to the Chatbot for next step -> /help')

# Help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,  
        """
        /start -> Welcome to my channel
        /help -> This particular message
        /Linkedin -> View my LinkedIn Profile
        /github -> View my Projects
        /Resume -> Download my Resume 
        /CoverLetter -> Download my Cover Letter 
        /Portfolio -> View My portfolio 
        /Webhit -> View My website
        """)

# LinkedIn
@bot.message_handler(commands=['Linkedin'])
def linkedin(message):
    bot.reply_to(message, 'Link: https://www.linkedin.com/in/kuldeep-singh-458015234/')

# GitHub
@bot.message_handler(commands=['github'])
def github(message):
    bot.reply_to(message, 'Link: https://github.com/kdkuzey')

# Resume
@bot.message_handler(commands=['Resume'])
def resume(message):
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/14Y1MotwF31HsVLWMnVNwtrj8uht-fgAU?usp=sharing')

# Cover Letter
@bot.message_handler(commands=['CoverLetter'])
def cover_letter(message):
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/1XorDulXpbR09EL1ccKzvguuxyCj2aRf1?usp=sharing')

# Portfolio
@bot.message_handler(commands=['Portfolio'])
def portfolio(message):
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/1x0q9ZMHhui5AJq1Kwf2EEK6gQFGp7RkO?usp=sharing')

# Website
@bot.message_handler(commands=['Webhit'])
def website(message):
    bot.reply_to(message, 'Link: https://drive.google.com/file/d/1d1wx9Obtj0qjzzR2pYuXzIoKlpKIbiDK/view?usp=sharing')

# Polling with error handling
while True:
    try:
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        print(f"Error: {e}")
import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler
file_handler = logging.FileHandler('bot.log')
file_handler.setLevel(logging.INFO)

# Create a console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and set it for the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# Bot Token
Token = "7721846695:AAGHQfoiF1VDzAEOb1Lu9HKWwJoUBgjDU3E"

bot = telebot.TeleBot(Token)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    logger.info('Received start command')
    bot.reply_to(message, 'NAMASTE! Welcome to the Chatbot for next step -> /help')

# Help command
@bot.message_handler(commands=['help'])
def help(message):
    logger.info('Received help command')
    bot.reply_to(message,  
        """
        /start -> Welcome to my channel
        /help -> This particular message
        /Linkedin -> View my LinkedIn Profile
        /github -> View my Projects
        /Resume -> Download my Resume 
        /CoverLetter -> Download my Cover Letter 
        /Portfolio -> View My portfolio 
        /Webhit -> View My website
        """)

# LinkedIn
@bot.message_handler(commands=['Linkedin'])
def linkedin(message):
    logger.info('Received linkedin command')
    bot.reply_to(message, 'Link: https://www.linkedin.com/in/kuldeep-singh-458015234/')

# GitHub
@bot.message_handler(commands=['github'])
def github(message):
    logger.info('Received github command')
    bot.reply_to(message, 'Link: https://github.com/kdkuzey')

# Resume
@bot.message_handler(commands=['Resume'])
def resume(message):
    logger.info('Received resume command')
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/14Y1MotwF31HsVLWMnVNwtrj8uht-fgAU?usp=sharing')

# Cover Letter
@bot.message_handler(commands=['CoverLetter'])
def cover_letter(message):
    logger.info('Received cover letter command')
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/1XorDulXpbR09EL1ccKzvguuxyCj2aRf1?usp=sharing')

# Portfolio
@bot.message_handler(commands=['Portfolio'])
def portfolio(message):
    logger.info('Received portfolio command')
    bot.reply_to(message, 'Link: https://drive.google.com/drive/folders/1x0q9ZMHhui5AJq1Kwf2EEK6gQFGp7RkO?usp=sharing')

# Website
@bot.message_handler(commands=['Webhit'])
def website(message):
    logger.info('Received website command')
    bot.reply_to(message, 'Link: https://drive.google.com/file/d/1d1wx9Obtj0qjzzR2pYuXzIoKlpKIbiDK/view?usp=sharing')

# Polling with error handling
while True:
    try:
        logger.info('Starting bot polling')
        bot.polling(none_stop=True, interval=0)
    except Exception as e:
        logger.error(f"Error: {e}")