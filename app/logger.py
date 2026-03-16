# Configuração de logging
# Servem para registrar mensagens recebidas, respostas enviadas e erros.

import logging
from .config import LOG_FORMAT, LOG_LEVEL

def setup_logging():
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

# Logger global
logger = logging.getLogger(__name__)
setup_logging()