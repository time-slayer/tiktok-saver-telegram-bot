import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    start_message = f"👋 Welcome, {user.mention_html()}\n" \
                    "📨 Send me a TikTok link and I’ll return the media\n" \
                    "🔗 Just paste a TikTok URL here and I’ll do the rest"
    await update.message.reply_html(start_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_message = "📌 <b>How to use this bot:</b>\n\n" \
                   "➊ Copy a link to any TikTok video or photo post\n" \
                   "➋ Send it here\n" \
                   "➌ Get the video or photo gallery with no watermark"
    await update.message.reply_html(help_message)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='Sorry, I didn\'t understand that command.',
    )


def main():
    load_dotenv()
    bot_token = os.getenv("TEST_BOT_TOKEN")
    application = ApplicationBuilder().token(bot_token).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))

    application.add_handler(MessageHandler(filters.COMMAND, unknown))

    application.run_polling()


if __name__ == '__main__':
    main()
