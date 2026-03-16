# data_loader.py
# Carrega os dados do arquivo JSON e os retorna como um dicionário.
# A função pode ser importada e usada em outros módulos, depois posso trocar JSON sem mexer no chatbot.py

from pathlib import Path
import json
from typing import Dict, Any
from .config import DATA_FILE

def load_data() -> Dict[str, Any]:
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception("Arquivo data.json não encontrado")
    except json.JSONDecodeError:
        raise Exception("Formato JSON inválido")
