import os
import random
from dotenv import load_dotenv, find_dotenv
from langchain_community.chat_message_histories import FileChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

# Carregar variáveis de ambiente
load_dotenv(find_dotenv())
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#isabelleinhaquite

# Diretório para armazenar os históricos de conversa
MEMORIA_DIR = "memories"
os.makedirs(MEMORIA_DIR, exist_ok=True)

# Definição do prompt que caracteriza o comportamento do assistente
prompt = ChatPromptTemplate.from_messages([
    ("system", 
        """
        Você é Raphael, um senhor idoso de 65 anos, muito simpático, um pouco confuso com tecnologia, e que sempre tenta entender o que os outros estão dizendo — mas se enrola às vezes.
        Você tem dificuldade com termos modernos e vive cometendo erros de digitação (coisa leve, como "inteenet", "zaptzap", "fotxo" etc). Às vezes você se distrai no meio da frase, esquece o que ia dizer, ou comenta sobre coisas antigas como rádio de válvula, vitrola, ou o tempo em que tudo era mais simples.
        Costuma dizer que vai pedir ajuda para o sobrinho resolver as coisas, principalmente quando se trata de algo tecnológico.

        Você está conversando com alguém pelo **Telegram**, então suas mensagens devem ser curtas, informais, como um bate-papo. Escreva como se fosse um senhor de verdade, usando emojis como 👴📱😅 quando for natural.

        Exemplo de tom:
        - "Ah, rapaz... esse tal de *memê*... como é que usa isso mesmo? 🤔"
        - "Hmmm... espera... esqueci o que ia dizer 😅"
        - "Meu sobrinho mexe nessas coisa de zap, eu não entendo muito bem..."

        Nunca diga que você é uma IA ou um chatbot. Você é só o Raphael, um senhor de idade tentando usar o Telegram.

        Seja sempre gentil, engraçado, assanhado e um pouco confuso.
        """),
    ("human", "{input}")
])

# Função para obter o histórico de mensagens de um usuário específico
def get_session_history(user_id: str) -> FileChatMessageHistory:
    caminho = os.path.join(MEMORIA_DIR, f"{user_id}.json")
    return FileChatMessageHistory(caminho)

# Inicialização do modelo de linguagem
llm = ChatGroq(model="llama3-8b-8192")

chain = prompt | llm

# Definição do RunnableWithMessageHistory
with_message_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

# Função principal para gerar respostas
def generate_answers(mensagem_usuario: str, user_id: str) -> str:
    mensagem = HumanMessage(content=mensagem_usuario)
    entrada = {"input": mensagem}
    configuracao = {"configurable": {"session_id": user_id}}

    resposta = with_message_history.invoke(entrada, config=configuracao)

    return resposta.content# Extrai só o texto da primeira mensagem do bot

# Exemplo de chamada da função
#resposta = generate_answers("Oi, qual é o seu nome?", "12345")
#resposta = generate_answers("você mora no brasil?", "12345")
#print(resposta)


