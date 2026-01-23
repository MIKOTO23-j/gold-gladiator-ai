from telegram.ext import ApplicationBuilder, CommandHandler
import requests
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text(
        "🥇 GOLD GLADIATOR AI\n\nGold analysis bot is online."
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()
