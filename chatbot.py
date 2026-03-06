# Chatbot simples para atendimento ao cliente
# Ele responde a mensagens do cliente com base em um arquivo JSON que contém produtos e status de pedidos

# Importa a biblioteca json para ler o arquivo de dados
import json

# Carrega os dados do arquivo JSON
with open("data.json") as f:
    data = json.load(f)

# Dicionário para armazenar o estado de cada usuário (identificado pelo nº de telefone)
user_states = {}

# Função para obter o estado do usuário, criando um novo estado se o usuário for novo
def get_state(phone):
    if phone not in user_states:
        user_states[phone] = {
            "step": "start"
        }
    return user_states[phone]

# Função para obter o menu principal
def get_menu():
    return (
        "Bem-vindo!\n\n"
        "Escolha uma opção:\n\n"
        "1 - Ver produtos\n"
        "2 - Status do pedido\n"
        "3 - Falar com suporte"
    )

# Função principal para processar a mensagem do usuário e retornar uma resposta
def get_response(phone, message):

    message = message.lower().strip()
    state = get_state(phone)

    # RESET DA CONVERSA
    if message == "reset":
        state["step"] = "start"
        return {
            "message": "Conversa reiniciada. Envie qualquer mensagem para começar."
        }

    # PRIMEIRA INTERAÇÃO
    if state["step"] == "start":
        state["step"] = "menu"
        return {
            "message": get_menu()
        }

    # MENU PRINCIPAL
    if state["step"] == "menu":

        if message == "1":
            products = "\n".join(f"- {p}" for p in data["products"])

            return {
                "message": f"Nossos produtos:\n\n{products}\n\nDigite 'menu' para voltar."
            }

        elif message == "2":
            state["step"] = "order_status"
            
            return {
                "message": "Digite o número do seu pedido."
            }

        elif message == "3":
            return {
                "message": "Nosso suporte entrará em contato em breve."
            }

        elif message == "menu":
            return {
                "message": get_menu()
            }

        else:
            return {
                "message": f"Opção inválida.\n\n{get_menu()}"
            }

    # CONSULTA DE PEDIDO
    if state["step"] == "order_status":

        if message == "menu":
            state["step"] = "menu"
            return {
                "message": get_menu()
            }

        if message in data["orders"]:

            status = data["orders"][message]

            state["step"] = "menu"

            return {
                "message": f"Status do pedido {message}: {status}\n\nDigite 'menu' para voltar."
            }

        else:
            return {
                "message": "Pedido não encontrado.\n\nDigite um número válido."
            }
