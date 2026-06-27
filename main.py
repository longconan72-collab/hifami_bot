from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "DÁN_TOKEN_MỚI_CỦA_BẠN_VÀO_ĐÂY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Xin chào! Bot HiFami đã hoạt động.")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot đang chạy...")
app.run_polling()