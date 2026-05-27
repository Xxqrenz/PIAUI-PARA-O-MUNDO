import paho.mqtt.publish as publish
import random
import time
import json

BROKER = "broker.hivemq.com"
TOPICO = "colmeia/dados"

COLMEIA_ID = 3

while True:

    temperatura = round(random.uniform(25, 35), 1)

    som = random.randint(1000, 3000)

    dados = {
        "colmeia": COLMEIA_ID,
        "temperatura": temperatura,
        "som": som
    }

    mensagem = json.dumps(dados)

    publish.single(
        TOPICO,
        mensagem,
        hostname=BROKER
    )

    print("\n[TRANSMISSOR]")

    print(mensagem)

    time.sleep(5)