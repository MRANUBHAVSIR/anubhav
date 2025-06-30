
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
import datetime

BOT_TOKEN = "7735919972:AAF7BrpGyV6Qn2RSW0XtuJrz6m-n3VfXoNA"
CHAT_ID = 6079776226

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Motivational messages and images
messages = [
    "🌞 Good morning Anubhav! Naya din, naya chance. Rise & Rule!",
    "💪 Apne sapne poore karne ka waqt aa gaya hai. Start strong today!",
    "🎯 Focused mind. Fearless heart. Let’s go!",
    "🔥 Tumhara aaj ka effort, kal ki jeet banega. Keep pushing!",
    "🧘‍♂️ Shaant dimag aur strong irade = unbeatable day!"
]

images = [
    "https://i.imgur.com/oYiTqum.jpeg",
    "https://i.imgur.com/Ta0oEDN.jpeg",
    "https://i.imgur.com/xZQw7E1.jpeg",
    "https://i.imgur.com/3xH6F77.jpeg",
    "https://i.imgur.com/dl9W9mi.jpeg"
]

quotes = [
    "“Push yourself, because no one else is going to do it for you.”",
    "“You are stronger than you think.”",
    "“Discipline is doing it even when you don’t feel like it.”",
    "“Great things take time. Don’t give up.”"
]

# Command Handlers
def motivate(update, context):
    update.message.reply_text(random.choice(messages))

def image(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=random.choice(images))

def focus(update, context):
    update.message.reply_text("📚 30 minutes. No phone. Just pure focus. Let's go!")

def quote(update, context):
    update.message.reply_text(random.choice(quotes))

def status(update, context):
    update.message.reply_text("✅ Bot is active and tracking your growth, Anubhav 💼")

def mood(update, context):
    mood = update.message.text.split(" ")[1].lower()
    if mood == "happy":
        update.message.reply_text("Awesome! Keep that smile, champ 😄")
    elif mood == "low":
        update.message.reply_text("It’s okay to feel low. You’ve survived 100% of your worst days 💪")
    elif mood == "stressed":
        update.message.reply_text("Breathe in. Hold. Breathe out. Repeat. You’ve got this, Anubhav 🌿")
    else:
        update.message.reply_text("Tell me how you're feeling: /mood happy | low | stressed")

# Weekly report every Sunday
def weekly_report(context):
    now = datetime.datetime.now()
    if now.weekday() == 6:  # Sunday
        context.bot.send_message(chat_id=CHAT_ID, text="📊 Weekly Report: You did well this week! Let’s keep the energy going 💯")

# Reminders (study + gratitude)
def send_reminders(context):
    now = datetime.datetime.now()
    if now.hour == 7:
        context.bot.send_message(chat_id=CHAT_ID, text="📚 Study Time: Start with 30 mins of full focus on BST or Accounts.")
    elif now.hour == 21:
        context.bot.send_message(chat_id=CHAT_ID, text="🌙 Night Reflection: Ek cheez likho jo aaj acchi lagi.")

# Registering handlers
dispatcher.add_handler(CommandHandler("motivate", motivate))
dispatcher.add_handler(CommandHandler("image", image))
dispatcher.add_handler(CommandHandler("focus", focus))
dispatcher.add_handler(CommandHandler("quote", quote))
dispatcher.add_handler(CommandHandler("status", status))
dispatcher.add_handler(CommandHandler("mood", mood))

# Schedule jobs
job_queue = updater.job_queue
job_queue.run_repeating(send_reminders, interval=3600, first=0)
job_queue.run_repeating(weekly_report, interval=3600, first=0)

updater.start_polling()
