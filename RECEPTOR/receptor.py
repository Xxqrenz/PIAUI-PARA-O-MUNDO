import socket

import requests

import json

HOST = "127.0.0.1"

PORTA = 5000

SERVIDOR = "http://127.0.0.1:3000/dados"

servidor = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

servidor.bind(
    (HOST, PORTA)
)

servidor.listen()

print("Gateway LoRa iniciado...")

while True:

    cliente, endereco = servidor.accept()

    mensagem = cliente.recv(
        1024
    ).decode()

    print(
        "\n[RECEPTOR]"
    )

    print(mensagem)

    dados = json.loads(
        mensagem
    )

    resposta = requests.post(
        SERVIDOR,
        json=dados
    )

    print(
        "HTTP:",
        resposta.status_code
    )

    cliente.close()