import socket

import json

import random

import time

HOST = "127.0.0.1"

PORTA = 5000

while True:

    cliente = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    cliente.connect(
        (HOST, PORTA)
    )

    dados = {

        "colmeia": "3",

        "temperatura": round(
            random.uniform(28, 40),
            1
        ),

        "som": random.randint(
            1000,
            4000
        )
    }

    mensagem = json.dumps(dados)

    cliente.send(
        mensagem.encode()
    )

    print(
        "[TRANSMISSOR]",
        mensagem
    )

    cliente.close()

    time.sleep(30)