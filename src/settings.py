# ============ Importação ============= #
import os
from dotenv import load_dotenv, find_dotenv

# ============ Constantes ============= #
_ = load_dotenv(find_dotenv())

TELEGRAM_API_ID = os.environ['TELEGRAM_API_ID']
TELEGRAM_API_HASH = os.environ['TELEGRAM_API_HASH']
TELEGRAM_TOKEN = os.environ['TELEGRAM_TOKEN']