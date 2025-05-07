from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, MessageHandler, CommandHandler, ContextTypes, filters
import requests
import replicate

# Set up Replicate client
client = replicate.Client(api_token="r8_KqwQ3hw8NpcqRiWFzjKQHkJwINVbCix37tv4y")

def query_llm(prompt):
    output = client.run(
        "meta/meta-llama-3-8b-instruct",
        input={
            "prompt": prompt,
            "max_new_tokens": 500,  # You can increase this if needed
            "temperature": 0.7,
            "system_prompt": "You are a helpful assistant who talks about composting."
        }
    )
    return "".join(output)

BOT_TOKEN = "7224030614:AAFKMVFH_XixKlFY3jREzAKWW1hf-1S9cKw"  # Replace with your actual bot token

# Simple menu UI
main_menu = ReplyKeyboardMarkup(
    [
        ["🌡 View compost conditions"],
        ["📈 Get compost maturity prediction"],
        ["❓ Learn how to compost better"],
        ["🧠 Chat about compost"]
    ],
    resize_keyboard=True
)

# Track chat mode per user
chat_mode = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_mode[update.effective_chat.id] = False  # Reset chat mode
    await update.message.reply_text(
        "👋 Welcome to CompostBot!\nChoose an option below to get started:",
        reply_markup=main_menu
    )

# Handle user replies and menu options
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_input = update.message.text.strip()

    # If user is in chat mode, forward message to LLM API
    if chat_mode.get(chat_id, False):
        if user_input.lower() in ["exit", "back", "menu"]:
            chat_mode[chat_id] = False
            await update.message.reply_text("🔙 Exiting chat mode. Choose from the menu below:", reply_markup=main_menu)
        else:
            try:
                answer = query_llm(user_input)
                await update.message.reply_text(answer)
            except Exception as e:
                await update.message.reply_text("❌ Failed to reach LLM API.")
        return

    # Handle menu options
    if user_input == "🌡 View compost conditions":
        await update.message.reply_text("📊 Sensor data feature coming soon.")
    
    elif user_input == "📈 Get compost maturity prediction":
        await update.message.reply_text("🧪 Please enter moisture, pH, and EC like this:\n`45.0, 6.8, 0.7`")
    
    elif user_input == "❓ Learn how to compost better":
        await update.message.reply_text("🪱 Composting Tips:\n- Keep moisture ~50%\n- Turn pile weekly\n- Avoid meat/oil")
    
    elif user_input == "🧠 Chat about compost":
        chat_mode[chat_id] = True
        await update.message.reply_text(
            "🧠 You are now chatting with CompostBot AI.\nAsk anything about compost. Type 'exit' to go back."
        )

    else:
        await update.message.reply_text("⚠️ Unknown option. Please choose from the menu.", reply_markup=main_menu)

# Initialize and run the bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
