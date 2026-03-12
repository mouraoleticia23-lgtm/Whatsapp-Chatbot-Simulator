# Teste simples para verificar a resposta do chatbot

from app.chatbot import get_response

phone = "5511999999999"

print("Chat iniciado. Digite 'sair' para encerrar.\n")

while True:

    user_message = input("You: ")

    if user_message.lower() == "sair":
        print("Encerrando chat...")
        break

    response = get_response(phone, user_message)

    print("Bot:", response["message"])
    print()
    