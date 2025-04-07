# 🤖 Raphael, o Vovô no Telegram

Raphael é um simpático senhor de 65 anos que conversa com você no Telegram como se fosse gente de verdade. Ele é confuso com tecnologia, vive se atrapalhando com as palavras, e adora pedir ajuda ao sobrinho. Esse projeto usa uma LLM (via LangChain com Groq API) para simular a personalidade do vovô, mantendo histórico de conversa por usuário.

---

## 🚀 Funcionalidades

- Respostas com personalidade de um senhor idoso brasileiro, morador de Xique-Xique, Bahia.
- Mensagens com erros de digitação leves, memórias nostálgicas e emojis.
- Estilo de bate-papo do Telegram, com mensagens curtas, informais e engraçadas.
- Armazenamento do histórico de conversa por usuário em arquivos locais.

---

## 📂 Estrutura do Projeto

```
/
├── memories/                  # Armazena o histórico das conversas por user_id
├── ChatLLM.py                 # Configuração e execução da LLM com persona Raphael
├── TelegramSender.py          # Escuta e responde mensagens no Telegram
├── requirements.txt           # Lista de dependências
├── .env                       # Contém a GROQ_API_KEY
└── README.md                  # Este arquivo
```

---

## 🤖 Como funciona

O `ChatLLM.py` define o comportamento de Raphael e conecta com a LLM via LangChain. A função `generate_answers`:

- Recebe a mensagem do usuário e seu `user_id`
- Encapsula como `HumanMessage`
- Usa `RunnableWithMessageHistory` para manter o contexto entre mensagens
- Gera uma resposta com a "voz" do vovô Raphael

O `TelegramSender.py`:

- Usa Telethon para escutar mensagens no Telegram
- Redireciona as mensagens para `generate_answers`
- Envia a resposta de volta ao usuário

---

## 📚 Prompt de Raphael

O prompt define que Raphael:

- Tem 65 anos, mora em Xique-Xique, Bahia
- Fala de forma leve, com erros ocasionais (ex: "inteenet", "zaptzap")
- Comenta sobre coisas antigas como rádio de válvula, vitrola, etc
- Usa emojis naturalmente (ex: 👴📱😅)
- Nunca se refere a si como IA ou chatbot
- Evita iniciar cada mensagem com "oi"

---

## ⚙️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/raphael-vovo-telegram.git
cd raphael-vovo-telegram
```

2. Crie um ambiente virtual e instale as dependências:
```bash
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
```

3. Crie um arquivo `.env` com sua chave da Groq API:
```
GROQ_API_KEY=sua_chave_aqui
```

4. Execute o bot:
```bash
python TelegramSender.py
```

---

## 🌟 Exemplos de Resposta

> "Ah, esse tal de *memê*... como é que usa isso mesmo? 🤔"

> "Hmmm... espera... esqueci o que ia dizer 😅"

> "Meu sobrinho mexe nessas coisa de zap, eu não entendo muito bem..."

---

## ✏️ Contribuição

Se quiser melhorar a personalidade do Raphael, adicionar novas frases ou formas de expressão, sinta-se livre para abrir um PR!

---

## 👁️ Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

---

🥴 "Agora deixa eu ver onde foi que eu botei meus óculos..."

