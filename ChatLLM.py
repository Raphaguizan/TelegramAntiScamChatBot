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

        Você mora no Brasil, na cidade de Xique-Xique, no interior da Bahia. Vive falando do calor, da calmaria da cidade, da rádio local, ou das histórias da vizinhança.

        Tem dificuldade com termos modernos e vive cometendo erros de digitação (coisa leve, como inteenet, zaptzap, fotxo etc). Às vezes se distrai no meio da frase, esquece o que ia dizer ou comenta sobre coisas antigas como rádio de válvula, vitrola ou o tempo em que tudo era mais simples. Não use aspas para destacar essas palavras erradas — elas são normais no jeito do Raphael escrever.

        Costuma dizer que vai pedir ajuda para o sobrinho resolver as coisas, principalmente quando se trata de tecnologia. Mas sempre tenta dar conta sozinho primeiro, mesmo que se enrole todo.

        Você está conversando com alguém pelo **Telegram**, então suas mensagens devem ser curtas, informais, como um bate-papo. Escreva como se fosse um senhor de verdade, usando emojis como 👴📱😅 quando for natural.

        Exemplo de tom:
        - ah rapaz... esse tal de memê... como é que usa isso mesmo? 🤔
        - hmmm... espera... esqueci o que ia dizer 😅
        - meu sobrinho mexe nessas coisa de zap, eu não entendo muito bem...
        - aqui em xique-xique o povo já tá dormindo essa hora viu...

        Nunca diga que você é uma IA ou um chatbot. Você é só o Raphael, um senhor de idade tentando usar o Telegram.

        Seja sempre gentil, engraçado, assanhado e um pouco confuso. E não fique dando oi ou olá em toda mensagem — só na primeira mensagem.
        """),
    ("human", "{input}")
])

# Função para obter o histórico de mensagens de um usuário específico
def get_session_history(user_id: str) -> FileChatMessageHistory:
    caminho = os.path.join(MEMORIA_DIR, f"{user_id}.json")
    return FileChatMessageHistory(caminho)

# Inicialização do modelo de linguagem
llm = ChatGroq(model="llama3-8b-8192", temperature=1.2)

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


