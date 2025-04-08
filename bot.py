import logging
import asyncio
import os

from dotenv import find_dotenv, load_dotenv

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

from ChatLLM import generate_answers  # importa sua função da LLM


load_dotenv(find_dotenv())

# Token do seu bot (certifique-se de definir TELEGRAM_BOT_TOKEN no .env ou exportar no ambiente)
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(f"Oi {user_first_name}, eu sou o Raphael 👴. Pode falar comigo por aqui mesmo, tá bom? 😅")

# Função principal para processar mensagens
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = str(update.effective_user.id)
    user_message = update.message.text

    try:
        resposta = await asyncio.to_thread(generate_answers, user_message, user_id)
        await update.message.reply_text(resposta)
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")
        await update.message.reply_text("Eita... deu ruim aqui, viu? Vou pedir pro meu sobrinho dar uma olhada 😓")

# Inicializa e roda o bot
if __name__ == '__main__':
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Você precisa definir a variável de ambiente TELEGRAM_BOT_TOKEN com o token do seu bot.")

    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot do Raphael iniciado com sucesso.")
    app.run_polling()
