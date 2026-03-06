# WhatsApp Chatbot Simulator

Um simulador simples de chatbot inspirado em fluxos de atendimento via WhatsApp, desenvolvido em Python.

Este projeto demonstra a criação de um fluxo básico de atendimento automatizado utilizando menus, controle de usuários e consulta de dados em JSON.

---

# Tecnologias Utilizadas

- Python
- JSON
- Lógica de fluxo de chatbot
- Simulação de atendimento automatizado

---

# Objetivo do Projeto

Este projeto foi desenvolvido para demonstrar conceitos de:

- lógica de programação
- criação de chatbots baseados em menu
- gerenciamento de estado de conversas
- manipulação de dados em JSON
- integração e automação de atendimento via WhatsApp

---

# Funcionalidades

- Mensagem de boas-vindas automática
- Menu principal com opções numeradas
- Listagem de produtos
- Consulta de status de pedidos
- Simulação de atendimento de suporte
- Controle de estado da conversa por usuário
- Reinício de conversa com comando `reset`

---

# Estrutura do Projeto

```
Whatsapp-Chatbot-Simulator

chatbot.py       # Lógica principal do chatbot
test_chat.py     # Simulador de conversa no terminal
data.json        # Dados de produtos e pedidos
README.md        # Documentação do projeto
```

---

# Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/Whatsapp-Chatbot-Simulator.git
```

### 2. Entrar na pasta do projeto

```bash
cd Whatsapp-Chatbot-Simulator
```

### 3. Executar o simulador

```bash
python test_chat.py
```

---

# Exemplo de Conversa

```
Bot: Bem-vindo!

Escolha uma opção:

1 - Ver produtos
2 - Status do pedido
3 - Falar com suporte

You: 1

Bot: Nossos produtos:

- Laptop
- Headphones

Digite 'menu' para voltar.
```

---

# Fluxo do Chatbot

O chatbot utiliza um sistema simples de controle de estado por usuário.

Estados principais da conversa:

- start
- menu
- order_status

Fluxo simplificado:

Usuário envia mensagem  
↓  
Bot envia mensagem de boas-vindas  
↓  
Bot mostra menu de opções  
↓  
Usuário escolhe uma opção  
↓  
Bot responde de acordo com a escolha  

---

# Estrutura do JSON

Arquivo `data.json`:

```json
{
  "products": [
    "Laptop",
    "Headphones"
  ],
  "orders": {
    "123": "Em preparação",
    "456": "Enviado",
    "789": "Entregue"
  }
}
```

---

# Possíveis Melhorias

- Integração com API do WhatsApp
- Armazenamento de informações em banco de dados
- Interface web para simulação do chat
- Logs de conversas
- Integração com IA

---
