# 🤖 Raphael, o Vovô do Telegram

Raphael é um simpático senhor idoso de Xique-Xique (Bahia), que conversa com você pelo Telegram como se fosse um vovô de verdade! Ele se enrola com tecnologia, fala do rádio de válvula, pede ajuda ao sobrinho, e comete erros de digitação engraçados.

O projeto é uma LLM personalizada que conversa com os usuários em tom leve, carismático e sempre com muita confusão tecnológica 😅

---

## 📁 Estrutura do Projeto

```
ChatTelegram/
├── bot.py                # Integração com o bot oficial do Telegram (python-telegram-bot)
├── TelegramSender.py     # Integração com Telethon
├── ChatLLM.py            # Configuração da LLM e função generate_answers
├── requirements.txt      # Dependências do projeto
├── memories/             # Pasta onde ficam os históricos de conversa por usuário
└── .env                  # Arquivo de variáveis de ambiente (GROQ_API_KEY)
```

---

## ⚙️ Requisitos

- Python 3.10+
- Conta na [Groq](https://console.groq.com/) com uma API Key
- Crie um bot com o [BotFather](https://t.me/botfather) no Telegram para usar o `bot.py`

Instale as dependências com:

```bash
pip install -r requirements.txt
```

No arquivo `.env`, adicione sua chave da API da Groq:
```env
GROQ_API_KEY=your_key_here
```

---

## 🚀 Como usar

### 1. Usando com Telethon (`TelegramSender.py`)

Este modo usa a biblioteca Telethon para escutar mensagens privadas enviadas ao bot e responder com a LLM.

```bash
python TelegramSender.py
```

Você precisará inserir seu `api_id` e `api_hash` do Telegram na primeira execução. O script salva a sessão.

### 2. Usando com Bot oficial (`bot.py`)

Este modo usa a biblioteca oficial `python-telegram-bot`. Basta inserir o token do bot no `.env`:

```env
BOT_TOKEN=your_telegram_bot_token
```

Depois, execute:

```bash
python bot.py
```

O Raphael responderá automaticamente a mensagens privadas enviadas ao bot.

---

## 🤖 Sobre o Raphael

- Mora em Xique-Xique, Bahia 🇧🇷
- Fala como um vovô real usando emojis 👴😅📱
- Escreve mensagens curtas e engraçadas como se estivesse no zap
- Nunca admite ser uma IA
- Tem um sobrinho que sempre resolve as coisas

---

## ✨ Exemplo de conversa

> Você: vovô como eu baixo o zaptzap?  
> Raphael: Ahhh esse *zaptzap*... eu tentei baixar aqui mas apertei no lugar errado 😅 Vou pedir pro meu sobrinho ver isso... espera...

---

## 🧠 Powered by

- [LangChain](https://www.langchain.com/)
- [Groq API](https://console.groq.com/)
- [python-telegram-bot](https://docs.python-telegram-bot.org/)
- [Telethon](https://docs.telethon.dev/)

---

## 📜 Licença

Este projeto é livre para uso e modificação. Se fizer algo legal com o Raphael, compartilha com a gente!
