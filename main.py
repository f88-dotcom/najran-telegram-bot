from telegram.ext import Application, CommandHandler

# هذه الدالة للرد على /start
async def start(update, context):
    await update.message.reply_text("أهلاً! أنا بوت تذكير. جرب تكتب: /remind")

# هذه الدالة المسؤولة عن ضبط التوقيت
async def set_reminder(update, context):
    await update.message.reply_text("تمام! سأذكرك بعد 10 ثوانٍ.")
    # تشغيل المنبه
    context.job_queue.run_once(send_message, 10, chat_id=update.effective_chat.id)

# هذه هي الرسالة التي ستصلك
async def send_message(context):
    await context.bot.send_message(chat_id=context.job.chat_id, text="تذكير: حان وقت المهمة!")

if __name__ == '__main__':
    import os
    TOKEN = os.environ.get("TOKEN")
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("remind", set_reminder))
    
    print("البوت يعمل الآن... جرب تكتب /remind في تيليجرام")
    app.run_polling()
