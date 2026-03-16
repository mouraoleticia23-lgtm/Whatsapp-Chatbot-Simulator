# WhatsApp Chatbot Simulator

Um simulador simples de chatbot inspirado em fluxos de atendimento via WhatsApp, desenvolvido em Python.

Este projeto demonstra a criação de um fluxo básico de atendimento automatizado utilizando menus, controle de usuários e consulta de dados em JSON.

O chatbot também pode ser acessado através de uma API construída com FastAPI, permitindo integração com outras aplicações.

---

# Tecnologias Utilizadas

- Python
- FastAPI
- API REST
- JSON
- Pydantic
- Lógica de fluxo de chatbot

---

# Objetivo do Projeto

Este projeto foi desenvolvido para demonstrar conceitos de:

- lógica de programação
- criação de chatbots baseados em menu
- gerenciamento de estado de conversas
- construção de APIs com FastAPI
- manipulação de dados em JSON
- simulação de automação de atendimento

---

# Funcionalidades

- Mensagem de boas-vindas automática
- Menu principal com opções numeradas
- Listagem de produtos
- Consulta de status de pedidos
- Simulação de atendimento de suporte
- Controle de estado da conversa por usuário
- Reinício de conversa com comando `reset`
- API REST para integração com outros sistemas
- Testes automatizados para validar o fluxo do chatbot

---

# Estrutura do Projeto

```
Whatsapp-Chatbot-Simulator

api/
└── main.py            # Ponto de entrada da API FastAPI

app/
├── chatbot.py         # Lógica principal do chatbot
├── config.py          # Configurações do projeto
├── data_loader.py     # Carregamento dos dados do JSON
├── logger.py          # Configuração de logs
└── states.py          # Definição dos estados da conversa

data/
└── data.json          # Dados de produtos e pedidos

tests/
├── test_chat.py       # Teste de funcionamento do chatbot

cli.py                 # Teste pelo terminal
pytest.ini             # Configurações do Pytest
README.md              # Documentação
requirements.txt       # Dependências do projeto
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

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

---

# Executar o Simulador no Terminal

Para testar o chatbot diretamente no terminal:

```bash
python tests/test_chat.py
```

Isso abrirá um chat onde você pode interagir com o bot.

---

# Executar a API

Para iniciar o servidor FastAPI:

```bash
python -m uvicorn api.main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática da API:

```
http://127.0.0.1:8000/docs
```

---

# Exemplo de Requisição

Endpoint:

```
POST /chat
```

Body da requisição:

```json
{
  "phone": "5511999999999",
  "message": "1"
}
```

Resposta:

```json
{
  "message": "Nossos produtos:\n\n- Laptop\n- Headphones\n- Keyboard"
}
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

# Estrutura dos Dados

Arquivo `data/data.json`:

```json
{
  "products": [
    "Laptop",
    "Headphones",
    "Keyboard"
  ],
  "orders": {
    "123": "Enviado",
    "456": "Processando",
    "789": "Entregue"
  }
}
```

## Possíveis Melhorias

- Integração com uma API de WhatsApp para permitir interações reais com usuários.
- Substituição do arquivo JSON por um banco de dados.
- Implementação de logs de conversas para monitoramento e análise das interações.
- Criação de uma interface web para simulação do chat no navegador.
- Adição de testes automatizados para garantir o funcionamento do fluxo do chatbot.
