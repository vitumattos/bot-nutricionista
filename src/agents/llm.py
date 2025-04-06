from src.settings import GOOGLE_API_KEY, SYSTEM_PROMPT

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import initialize_agent, AgentType


class NutritionistAgent:
    def __init__(self, session_id):
        self.session_id = session_id

        self.prompt = ChatPromptTemplate.from_messages([
            ('system', SYSTEM_PROMPT),
            ('user', '{input}')
        ])
        self.llm = ChatGoogleGenerativeAI(
            google_api_key=GOOGLE_API_KEY,
            model="gemini-1.5-flash",
            temperature=0.1,
        )
        self.tools = []

        self.chain = self.prompt | self.llm | StrOutputParser()


    def run(self, input):
        try:
            response = self.chain.invoke({'input': input})
        except Exception as e:
            print(e)
            response = "Desculpe, houve um erro ao processar sua mensagem. Por favor, tente novamente mais tarde."

        return response 
