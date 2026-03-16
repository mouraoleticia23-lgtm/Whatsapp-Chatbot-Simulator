# app/config.py
# Configurações centralizadas do projeto

import logging
from pathlib import Path

# Logging
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = logging.INFO

# Paths
DATA_DIR = Path(__file__).parent.parent / "data"
DATA_FILE = DATA_DIR / "data.json"

# Outras configurações
DEFAULT_PHONE = "5511999999999"