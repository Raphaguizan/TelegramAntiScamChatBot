import os
import asyncio
import random
from dotenv import find_dotenv, load_dotenv
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import SetTypingRequest
from telethon.tl.types import SendMessageTypingAction

#pegar credenciais
load_dotenv(find_dotenv())
TELEGRAM_API_KEY = os.getenv("TELEGRAM_API_KEY")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

# 🧠 Insira seus dados aqui
api_id = TELEGRAM_API_KEY      # <- Coloque aqui seu API ID
api_hash = TELEGRAM_API_HASH  # <- Sua API Hash
phone_number = MY_PHONE_NUMBER # <- Seu número com DDD e +55

# 🗣 Entrada interativa no terminal
alvo = input("Digite o ID numérico ou username do alvo (sem @): ").strip()

# Cria a sessão
client = TelegramClient('sessao_golpista', api_id, api_hash)

# Conecta e faz login
async def main():
    await client.start(phone_number)
    print("✅ Bot iniciado e conectado como você.")

# Evento: ao receber mensagem
@client.on(events.NewMessage)
async def handle_message(event):
    sender = await event.get_sender()
    sender_id = str(sender.id)
    sender_username = sender.username or ""
    msg = event.raw_text

    # Verifica se o remetente é o "alvo"
    if (sender_id == alvo) or (sender_username.lower() == alvo.lower()):
        print(f"📩 Mensagem de {sender.first_name}: {msg}")

        # Frase de resposta
        resposta = "Hmm... interessante. Pode me explicar melhor isso?"

        # Tempo de "pensando"
        pensando = random.uniform(1.0, 2.0) # MUDAR PARA UM TEMPO MAIOR DEPOIS
        await asyncio.sleep(pensando)

        # Simular "digitando..."
        await client(SetTypingRequest(
            peer=event.chat_id,
            action=SendMessageTypingAction()
        ))

        # Calcular tempo baseado no tamanho da resposta
        chars = len(resposta)
        tempo_por_char = random.uniform(0.1, 0.4)
        tempo_digitando = chars * tempo_por_char
        await asyncio.sleep(tempo_digitando)

        # Responde
        await event.respond(resposta)
        print(f"💬 Respondi (após pensar {pensando:.1f}s + digitar {tempo_digitando:.1f}s): {resposta}")

# Inicia o cliente
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
