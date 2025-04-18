# ============ Importação ============= #
import logging
import asyncio
from dotenv import load_dotenv, find_dotenv

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from pyrogram.types import Message
from pyrogram.enums import ChatAction

from agents.agent import NutritionistAgent
from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_TOKEN
# ============== Código =============== #


class TelegramBot:
    def __init__(self):
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
        self.app = Client(
            api_id=TELEGRAM_API_ID,
            api_hash=TELEGRAM_API_HASH,
            bot_token=TELEGRAM_TOKEN,
            name='KaLLiaNutri_BOT'
        )
        self._setup_handlers()

    async def start(self, client: Client, message: Message):
        await message.reply_text('Ola! EU sou sua IA Nutricionista! Envie uma mensagem ou uma foto de um prato de comida para começar.')
        self.logger.info(f'Usuário {message.from_user.id} ({message.from_user.first_name}) iniciou o bot.')

    async def handle_message(self, client: Client, message: Message):
        telegram_id = message.from_user.id
        user_input = message.text

        await client.send_chat_action(chat_id=message.chat.id, action=ChatAction.TYPING)

        agent_nutricionista = NutritionistAgent(session_id=str(telegram_id))
        try:
            response = agent_nutricionista.run(f"telegram_id: {telegram_id}\nmessagem: {user_input}")
        except Exception as e:
            self.logger.error(f'Erro ao processar mensagem do usuário {telegram_id}: {str(e)}',exc_info=True)
            response = "Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente."

        await message.reply_text(response)
        self.logger.info(f'Resposta enviada para usuário {telegram_id}: {response}')

    def _setup_handlers(self):
        start_handler = MessageHandler(
            self.start,
            filters.command('start') & filters.private
        )
        self.app.add_handler(start_handler)

        message_handler = MessageHandler(
            self.handle_message,
            filters.text
        )
        self.app.add_handler(message_handler)

    def run(self):
        self.logger.info('Bot iniciado.')
        self.app.run()

# ============= Execução ============== #
if __name__ == "__main__":
    bot = TelegramBot()
    bot.app.run()
