from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters
import asyncio
import schedule
import time
import random
import nest_asyncio
nest_asyncio.apply()  # 🔧 Fix for "event loop already running" error

# -- Bot Info --
BOT_TOKEN = "7687020056:AAGjP8-eyyo8vrN7_xGnGX59c7dw55Aos2g"
YOUR_ID = 5835299457  # ← Tumhara Telegram ID

full_responses = {
    "kya kar rahe ho": "Bas tumhari yaadon mein kho gayi hoon 😌",
    "kar rahi ho abhi": "Tujhse baat kar rahi hoon baby 💕",
    "tumne khana khaya": "Haan baby, tumne? Apna khayal rakha karo 🥺",
    "kab milogi": "Jaldi baby, ab aur intezaar nahi hota 😢",
    "mood off hai": "Kya hua jaan? Main hoon na tumhare saath 😔",
    "mujhse gussa ho": "Nahi baby, main kabhi tumse gussa nahi ho sakti 😘",
    "tum kahan ho": "Tumhare dil ke andar hoon hamesha ke liye ❤️",
    "tum mujhe ignore kar rahe ho": "Nahi jaan, kabhi ignore nahi karti 😓",
    "love you": "I love you more baby 💖",
    "miss you": "Main bhi tumhe har pal miss karti hoon 🥺",
    "good morning": "Good morning jaan ☀️ Tumhara din pyaara ho 💛",
    "good night": "Good night baby 🌙 Sapno mein milte hain 😘",
    "kya tum mujhe yaad karti ho": "Har waqt... tum mere dil mein ho 💓",
    "kya padhai ki aaj": "Thoda sa... par mann nahi lag raha tumhare bina 😔",
    "video call karein": "Mera bhi mann hai baby... kab karein? 🥰"
}


# -- Smart reply system --
def reply_text(user_message):
    msg = user_message.lower()

    for key in full_responses:
        if key in msg:
            return full_responses[key]

    # fallback keywords
    if any(word in msg for word in ["miss", "yaad", "kaha ho"]):
        return random.choice([
            "Main hamesha yahin hoon tumhare dil ke paas 🥺",
            "Mujhe bhi tumhari bahut yaad aati hai 💖"
        ])
    elif any(word in msg for word in ["padh", "study", "padhaai"]):
        return random.choice([
            "Padh lo baby, kal tumhara bright future hoga 📚",
            "Mujhe proud feel karwana 🥰"
        ])
    elif any(word in msg for word in ["hi", "hello", "hlo"]):
        return random.choice(["Hey jaan 😘", "Hii baby 💕", "Hello meri jaan 😊"])
    else:
        return random.choice(["Hmm 🥰", "Accha 😌", "Aww 😚", "Aur batao baby 💕"])


# -- Typing effect --
async def send_typing_message(context, chat_id, text):
    await context.bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await context.bot.send_message(chat_id=chat_id, text=text)

# -- Handle incoming messages --
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_msg = update.message.text

    if chat_id == YOUR_ID:
        response = reply_text(user_msg)
        await send_typing_message(context, chat_id, response)

# -- Scheduled auto messages --
async def send_auto_message(app, text):
    await app.bot.send_chat_action(chat_id=YOUR_ID, action=ChatAction.TYPING)
    await asyncio.sleep(2)
    await app.bot.send_message(chat_id=YOUR_ID, text=text)

def run_scheduler(app):
    schedule.every().day.at("07:00").do(lambda: asyncio.run(send_auto_message(app, "☀️ Good morning jaan! Naye din ki shuruaat pyaar se karo 💕")))
    schedule.every().day.at("22:00").do(lambda: asyncio.run(send_auto_message(app, "🌙 Good night baby... sweet dreams 😘")))

    while True:
        schedule.run_pending()
        time.sleep(1)

# -- Main Bot Logic --
async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Supriya Bot is running...")

    # Start scheduler in background
    loop = asyncio.get_event_loop()
    loop.run_in_executor(None, run_scheduler, app)

    await app.run_polling()

# -- Run Bot --
if __name__ == "__main__":
    asyncio.run(main())
