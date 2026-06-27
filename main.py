from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN="8232656263:AAELnFMa0WRcHhBF7d8n2pnbGgXS7J0nApw"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào! Bot HiFami đã hoạt động.")

app=Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot đang chạy...")
app.run_polling()