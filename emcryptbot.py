"""EmojiCrypt based Telegram Bot"""

#!/usr/bin/env python

# Import Modules

import logging
import os
import threading
import time
import asyncio
from datetime import datetime

from telegram import __version__ as TG_VER

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

# Import Custom

import emojicrypt

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Global Tokens

TELEGRAM_TOKEN = "TELEGRAM_API_KEY"

# Telegram bot key
tgenv = os.getenv('TELEGRAM_KEY')
if tgenv is None:
    TGKEY = TELEGRAM_TOKEN
else:
    TGKEY = tgenv
print(tgenv)

# Lots of console output
DEBUG = True

# User Session timeout
TIMSTART = 300
TIM = 1

# Defaults
USER = "username"
RUNNING = False
CACHE = None
QCACHE = None
CHAT_LOG = None
BOTNAME = 'bot'
USERNAME = 'user'
CHOICE = 0
# PREV_CHOICE = CHOICE
KEYWORD = 'pass'

# Define a few command handlers. These usually take the two arguments update and
# context.


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    global USER
    USER = update.effective_user
    global CHAT_LOG
    global QCACHE
    global CACHE
    global TIM
    left = str(TIM)
    if TIM == 1:
        CHAT_LOG = None
        CACHE = None
        QCACHE = None
        await update.message.reply_html(
            rf"Hi {USER.mention_html()}!, " +    # type: ignore
            "press [/help] for details . . .",
            reply_markup=ForceReply(selective=True),
        )
        return
    else:
        await update.message.reply_text(
            'I am currently talking to someone else. Can you plea)e wait ' + left + ' seconds?'
        )
        return


async def encrypt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """"Encrypt Method"""
    global CHOICE
    CHOICE = 1
    await update.message.reply_html(
        rf"Enter PLAIN TEXT",  # type: ignore
        reply_markup=ForceReply(selective=True),
    )


async def decrypt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Decrypt Method"""
    global CHOICE
    CHOICE = 2
    await update.message.reply_html(
        rf"Enter CYPHER TEXT",  # type: ignore
        reply_markup=ForceReply(selective=True),
    )


async def keyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Set Keyword"""
    global CHOICE
    #    global PREV_CHOICE
    #    PREV_CHOICE = CHOICE
    CHOICE = 3
    await update.message.reply_html(
        rf"Enter KEYWORD",  # type: ignore
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    await update.message.reply_text(
        '[/reset] resets the conversation,' +
        '\n [/retry] retries the last output,' +
        '\n [/trigger] initiates the fun,' +
        '\n [/encrypt] encrypts a plain text' +
        '\n [/decrypt] decrypts a cipher text'
    )


async def reset(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /reset is issued."""
    global CHAT_LOG
    global CACHE
    global QCACHE
    left = str(TIM)
    if USER == update.message.from_user.id:
        CHAT_LOG = None
        CACHE = None
        QCACHE = None
        await update.message.reply_text('Bot has been reset, send a message!')
        return
    if TIM == 1:
        CHAT_LOG = None
        CACHE = None
        QCACHE = None
        await update.message.reply_text('Bot has been reset, send a message!')
        return
    else:
        await update.message.reply_text(
            'I am currently talking to someone else. Can you please wait ' + left + ' seconds?'
        )
        return


async def retry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /retry is issued."""
    global CHAT_LOG
    global CACHE
    global QCACHE
    left = str(TIM)
    if USER == update.message.from_user.id:
        new = True
        compute = threading.Thread(target=wait_call, args=(
            update, new))
        compute.start()
        return
    if TIM == 1:
        CHAT_LOG = None
        CACHE = None
        QCACHE = None
        await update.message.reply_text('Send a message!')
        return
    else:
        await update.message.reply_text(
            'I am currently talking to someone else. Can you please wait ' + left + ' seconds?'
        )
        return


async def runn(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when a message is received."""
    new = False
    compute = threading.Thread(target=interact_call, args=(
        update, new))
    compute.start()


async def getChoice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get Current CHOICE"""
    await update.message.reply_text("Current CHOICE = " + str(CHOICE))


async def getKeyword(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Get Current KEYWORD"""
    await update.message.reply_text("Current KEYWORD : " + str(KEYWORD))


async def wait(update, new):
    """Wait Method"""
    global USER
    global CHAT_LOG
    global CACHE
    global QCACHE
    global TIM
    global RUNNING
    if USER == "":
        USER = update.message.from_user.id
    if USER == update.message.from_user.id:
        TIM = TIMSTART
        compute = threading.Thread(
            target=interact_call, args=(update, new))
        compute.start()
        if RUNNING is False:
            while TIM > 1:
                RUNNING = True
                time.sleep(1)
                TIM = TIM - 1
        if RUNNING is True:
            CHAT_LOG = None
            CACHE = None
            QCACHE = None
            await update.message.reply_text('Timer has run down, bot has been reset to defaults.')
            RUNNING = False
    else:
        left = str(TIM)
        await update.message.reply_text(
            'I am currently talking to someone else. Can you please wait ' + left + ' seconds?'
        )


def wait_call(update, new):
    """Invoke Wait"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(wait(update, new))


################
# Main functions #
################


def format_prompt(question, chat_log=None):
    """Format Prompt"""
    if chat_log is None:
        chat_log = 'The following is a chat between two users:\n\n'
    now = datetime.now()
    ampm = now.strftime("%I:%M %p")
    t = '[' + ampm + '] '
    return f'{chat_log}{t}{USERNAME}: {question}\n{t}{BOTNAME}:'


def append_answer_to_chat_log(question, answer, chat_log=None):
    """Append to Chat Log"""
    prompt = format_prompt(question, chat_log)
    return f'{prompt} {answer}\n'


def ask(question):
    """Get Answer"""
    global KEYWORD
    #    global CHOICE
    cipher = emojicrypt.EmojiCrypt(KEYWORD)
    if CHOICE == 1:
        answer = cipher.encrypt(question)
    elif CHOICE == 2:
        answer = cipher.decrypt(question)
    elif CHOICE == 3:
        KEYWORD = question
        #        CHOICE = PREV_CHOICE
        answer = "KEYWORD set to :=> " + KEYWORD
    else:
        answer = 'No Response . . .'
    return answer
    # fp = 15 pp= 1 top_p = 1 temp = 0.9


async def interact(update, new):
    """Interact with User"""
    global CHAT_LOG
    global CACHE
    global QCACHE
    print("\n==========START==========\n")
    tex = update.message.text
    text = str(tex)
    if new is True:
        if DEBUG is True:
            print("Chat_Log CACHE is...")
            print(CACHE)
            print("Question CACHE is...")
            print(QCACHE)
        CHAT_LOG = CACHE
        question = QCACHE
    else:
        question = text
        QCACHE = question
        CACHE = CHAT_LOG
    # update.message.reply_text('Computing...')
    try:
        answer = ask(question)
        if DEBUG is True:
            print("Input :\"" + question)  # type: ignore
            print("\nOutput :\n" + answer)  # type: ignore
            print("\n====================\n")
        await update.message.reply_text(answer)
        CHAT_LOG = append_answer_to_chat_log(
            question, answer, CHAT_LOG)  # type: ignore
        if DEBUG is True:
            # Print the chat log for debugging
            print('-----PRINTING CHAT LOG-----\n')
            print(CHAT_LOG)
            print('-----END CHAT LOG-----\n')
        if CHOICE == 3:
            await update.message.reply_html(
                rf"Choose [/encrypt] or, [/decrypt]",  # type: ignore
                reply_markup=ForceReply(selective=True),
            )
    except Exception as e:
        errstr = str(e)
        print('\nException ::\n' + errstr)
        await update.message.reply_text('Please WAIT !')


def interact_call(update, new):
    """Invole Interact"""
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(interact(update, new))


async def error(update: Update):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused ERROR !', update)


def main() -> None:
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("trigger", keyword))
    application.add_handler(CommandHandler("encrypt", encrypt))
    application.add_handler(CommandHandler("decrypt", decrypt))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("reset", reset))
    application.add_handler(CommandHandler("retry", retry))
    application.add_handler(CommandHandler("getChoice", getChoice))
    application.add_handler(CommandHandler("getKeyword", getKeyword))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, runn))

    # on non command i.e message - echo the message on Telegram
    #    application.add_handler(MessageHandler(
    #        filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()
