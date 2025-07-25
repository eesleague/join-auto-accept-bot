import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8135532099:AAF17JHYasDtai_70zAPUkogMjFo_vq05cU
"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is Running...")

async def accept_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    await context.bot.send_message(chat_id=update.chat_join_request.from_user.id,
                                   text="✅ आपकी रिक्वेस्ट Accept हो गई है! धन्यवाद ❤️")

if name == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(accept_request))
    print("Bot is running...")
    app.run_polling()
