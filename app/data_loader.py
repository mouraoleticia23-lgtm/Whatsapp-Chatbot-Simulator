# data_loader.py
# Carrega os dados do arquivo JSON e os retorna como um dicionário.
# A função pode ser importada e usada em outros módulos, depois posso trocar JSON sem mexer no chatbot.py

import json

def load_data():
    with open("data/data.json", "r", encoding="utf-8") as f:
        return json.load(f)
