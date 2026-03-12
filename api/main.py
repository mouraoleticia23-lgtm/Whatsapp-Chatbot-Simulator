# main.py
# É o ponto de entrada para a aplicação FastAPI - define as rotas e a lógica para processar as mensagens do chatbot.

# Importa as bibliotecas necessárias
from fastapi import FastAPI
from pydantic import BaseModel
from app.chatbot import get_response

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
def home():
    return {"message": "WhatsApp Chatbot Simulator API"}

# Rota para processar as mensagens do chatbot
@app.post("/chat")
def chat(msg: Message):
    return get_response(msg.phone, msg.message)
