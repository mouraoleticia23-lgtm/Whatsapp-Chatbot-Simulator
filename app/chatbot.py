# Chatbot simples para atendimento ao cliente
# Ele responde a mensagens do cliente com base em um arquivo JSON que contém produtos e status de pedidos

# Importa as funções e constantes necessárias de outros módulos
from app.data_loader import load_data
from app.states import START, MENU, ORDER_STATUS
from typing import Dict, Any
from app.logger import logger
from datetime import datetime

# Carrega os dados do arquivo JSON 
data = load_data()

# Dicionário para armazenar o estado de cada usuário (identificado pelo nº de telefone)
user_states = {}

# Função para obter o estado do usuário, criando um novo estado se o usuário for novo
def get_state(phone: str) -> Dict[str, Any]:
    if phone not in user_states:
        user_states[phone] = {"step": START, "timestamp": datetime.now()}
    return user_states[phone]

# Função para obter o menu principal
def get_menu() -> str:
    return (
        "Bem-vindo!\n\n"
        "Escolha uma opção:\n\n"
        "1 - Ver produtos\n"
        "2 - Status do pedido\n"
        "3 - Falar com suporte\n"
        "0 - Voltar ao menu"
    )

# Função principal para processar a mensagem do usuário e retornar uma resposta
def get_response(phone: str, message: str) -> Dict[str, str]:

    message = message.lower().strip()
    state = get_state(phone)

    logger.info(f"Received from {phone}: {message}")

    # RESET DA CONVERSA
    if message == "reset":
        state["step"] = START
        response = {"message": "Conversa reiniciada. Envie qualquer mensagem para começar."}
        logger.info(f"Sent to {phone}: {response['message']}")
        return response

    # PRIMEIRA INTERAÇÃO
    if state["step"] == START:
        state["step"] = MENU
        response = {"message": get_menu()}
        logger.info(f"Sent to {phone}: {response['message']}")
        return response

    # MENU PRINCIPAL
    if state["step"] == MENU:

        if message == "1":
            products = "\n".join(f"- {p}" for p in data["products"])
            response = {"message": f"Nossos produtos:\n\n{products}\n\nDigite '0' para voltar."}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        elif message == "2":
            state["step"] = ORDER_STATUS
            response = {"message": "Digite o número do seu pedido."}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        elif message == "3":
            response = {"message": "Nosso suporte entrará em contato em breve."}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        elif message == "0":
            response = {"message": get_menu()}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        else:
            response = {"message": f"Opção inválida.\n\n{get_menu()}"}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

    # CONSULTA DE PEDIDO
    if state["step"] == ORDER_STATUS:

        if message == "0":
            state["step"] = MENU
            response = {"message": get_menu()}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        if message in data["orders"]:
            status = data["orders"][message]
            state["step"] = MENU
            response = {"message": f"Status do pedido {message}: {status}\n\nDigite '0' para voltar."}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response

        else:
            response = {"message": "Pedido não encontrado.\n\nDigite um número válido."}
            logger.info(f"Sent to {phone}: {response['message']}")
            return response
