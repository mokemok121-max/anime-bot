import os
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "naruto" in text:
        await update.message.reply_text("Naruto: https://myanimelist.net/anime/20/Naruto")
    elif "attack on titan" in text:
        await update.message.reply_text("Attack on Titan: https://myanimelist.net/anime/16498/Shingeki_no_Kyojin")
    elif "one piece" in text:
        await update.message.reply_text("One Piece: https://myanimelist.net/anime/21/One_Piece")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
