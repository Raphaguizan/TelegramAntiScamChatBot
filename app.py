from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Lista de usuários autorizados (pode ser ID ou username)
AUTHORIZED_USERS = [123456789, 987654321]  # substitua pelos seus IDs

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Olá! Você está autorizado.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Acesso negado.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id in AUTHORIZED_USERS:
        texto = update.message.text
        print(f"Mensagem de {user_id}: {texto}")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Você disse: {texto}")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Você não está autorizado a usar este bot.")

app = ApplicationBuilder().token("SEU_TOKEN_AQUI").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Bot rodando...")
app.run_polling()
