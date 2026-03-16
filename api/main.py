# main.py
# É o ponto de entrada para a aplicação FastAPI - define as rotas e a lógica para processar as mensagens do chatbot.

from fastapi import FastAPI            # FastAPI para definir as rotas da API
from pydantic import BaseModel         # Pydantic para validar os dados de entrada e saída da API
from app.chatbot import get_response   # get_response processa as mensagens e gera respostas
from typing import Dict                # Dict para definir o tipo de retorno da função home

# Cria a aplicação FastAPI
app = FastAPI(
    title="WhatsApp Chatbot Simulator",
    version="1.0"
)

# Define o modelo de dados para a mensagem recebida
class Message(BaseModel):
    phone: str
    message: str

# Rota para a página inicial
@app.get("/")
def home() -> Dict[str, str]:
    return {"message": "WhatsApp Chatbot Simulator API"}

# Modelo de resposta do chatbot
class ChatResponse(BaseModel):
    message: str

# Rota para processar as mensagens do chatbot
@app.post("/chat", response_model=ChatResponse)
def chat(msg: Message) -> ChatResponse:
    return get_response(msg.phone, msg.message)
