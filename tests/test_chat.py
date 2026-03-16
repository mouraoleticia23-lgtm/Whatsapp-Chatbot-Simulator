# Testes automatizados para o chatbot usando pytest

import pytest
from app.chatbot import get_response

def test_welcome_message():
    phone = "5511999999999"
    response = get_response(phone, "oi")
    assert "Bem-vindo" in response["message"]

def test_products_menu():
    phone = "5511999999998"
    get_response(phone, "oi")  # Inicia
    response = get_response(phone, "1")
    assert "Nossos produtos" in response["message"]

def test_order_status_prompt():
    phone = "5511999999997"
    get_response(phone, "oi")  # Inicia
    response = get_response(phone, "2")
    assert "Digite o número do seu pedido" in response["message"]

def test_order_status_valid():
    phone = "5511999999996"
    get_response(phone, "oi")  # Inicia
    get_response(phone, "2")  # Vai para order status
    response = get_response(phone, "123")  # Pedido válido
    assert "Status do pedido" in response["message"]

def test_order_status_invalid():
    phone = "5511999999995"
    get_response(phone, "oi")  # Inicia
    get_response(phone, "2")  # Vai para order status
    response = get_response(phone, "999")  # Pedido inválido
    assert "Pedido não encontrado" in response["message"]

def test_invalid_option():
    phone = "5511999999994"
    get_response(phone, "oi")  # Inicia
    response = get_response(phone, "99")
    assert "Opção inválida" in response["message"]

def test_reset():
    phone = "5511999999993"
    response = get_response(phone, "reset")
    assert "Conversa reiniciada" in response["message"]

def test_support():
    phone = "5511999999992"
    get_response(phone, "oi")  # Inicia
    response = get_response(phone, "3")
    assert "suporte entrará em contato" in response["message"]
    