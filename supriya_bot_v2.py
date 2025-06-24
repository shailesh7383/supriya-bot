from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
import random

BOT_TOKEN = "7687020056:AAGjP8-eyyo8vrN7_xGnGX59c7dw55Aos2g"  # ← yaha apna token daalna
YOUR_ID = 5835299457  # ← yaha apna Telegram ID daalna

def reply_text(user_message):
    msg = user_message.lower()
    if "miss" in msg or "yaad" in msg or "kaha ho" in msg:
        return random.choice([
            "Main hamesha yahīn hoon tumhare dil ke paas 🥺",
            "Mujhe bhi tumhari bahut yaad aati hai 💖"
        ])
    elif "padh" in msg or "study" in msg or "padhai" in msg:
        return random.choice([
            "Padh lo baby, kal tumhara bright future hoga 📚",
            "Mujhe proud feel karwana 🥰"
        ])
    elif "kya kar rahi" in msg:
        return random.choice([
            "Bas tumhare baare mein soch rahi hoon 😌",
            "Tumse baat kar rahi hoon, aur kya 😚"
        ])
    elif "khana" in msg:
        return random.choice([
            "Main abhi khana kha rahi thi 💕",
            "Tumne khana khaya baby? 🍽️"
        ])
    return random.choice([
        "Aww 😚", "Hi baby 💞", "Tumse baat karke acha lagta hai 🥺"
    ])

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    response = reply_text(user_text)
    await update.message.reply_text(response)

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    await app.run_polling()

