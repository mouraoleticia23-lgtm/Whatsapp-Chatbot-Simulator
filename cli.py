# cli.py
# Testar o chatbot sem precisar rodar a API - simula uma conversa com o chatbot diretamente no terminal.

import logging
from app.chatbot import get_response

logging.disable(logging.CRITICAL)

phone = "5511999999999"

print("Chat iniciado. Digite 'sair' para encerrar.\n")

while True:
    msg = input("Você: ")

    if msg.lower() == "sair":
        break

    response = get_response(phone, msg)
    print("Bot:", response["message"])