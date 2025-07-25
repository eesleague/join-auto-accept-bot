from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

BOT_TOKEN = "8135532099:AAF17JHYasDtai_70zAPUkogMjFo_vq05cU"

async def accept_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.chat_join_request.approve()
    user_id = update.chat_join_request.from_user.id
    await context.bot.send_message(
        chat_id=user_id,
        text="धन्यवाद! आपने चैनल Join कर लिया है 🎉\nअब आप prediction updates और gift codes पा सकते हैं!"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(ChatJoinRequestHandler(accept_request))
app.run_polling()
