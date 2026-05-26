import paho.mqtt.client as mqtt
import requests
import json

BROKER = "localhost"

TOPICO = "colmeia/dados"

SERVIDOR = "http://127.0.0.1:3000/dados"

def on_message(client, userdata, msg):

    mensagem = msg.payload.decode()

    print("\n[RECEPTOR]")

    print(mensagem)

    dados = json.loads(mensagem)

    resposta = requests.post(
            SERVIDOR,
            json=dados
        )

    print(
        "HTTP:",
        resposta.status_code
    )

client = mqtt.Client()

client.on_message = on_message

client.connect(BROKER)

client.subscribe(TOPICO)

print("Gateway iniciado...")

client.loop_forever()