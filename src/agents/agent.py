from settings import GOOGLE_API_KEY, SYSTEM_PROMPT, DATABASE_URL

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory


memory = InMemoryChatMessageHistory()


def get_by_session_id(session_id):
    return SQLChatMessageHistory(
        session_id=session_id,
        connection_string=DATABASE_URL
    )


class NutritionistAgent:
    def __init__(self, session_id):
        self.session_id = session_id

        self.prompt = ChatPromptTemplate.from_messages([
            ('system', SYSTEM_PROMPT),
            ('placeholder', '{history}'),
            ('human', '{input}')
        ])
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=GOOGLE_API_KEY,
            model="gemini-1.5-flash",
            temperature=0.1,
        )
        self.tools = []

        self.chain = self.prompt | self.llm | StrOutputParser()

        self.chain_w_memory = RunnableWithMessageHistory(
            self.chain,
            get_by_session_id,
            input_messages_key="input",
            history_messages_key="history",
        )

    def run(self, input):
        try:
            # utilizar self.chain_w_memory para conversar com memoria
            response = self.chain.invoke(
                {'input': input},
                config={'configurable': {'session_id': self.session_id}}
            )
        except Exception as e:
            print(e)
            response = "Desculpe, houve um erro ao processar sua mensagem. Por favor, tente novamente mais tarde."

        return response
