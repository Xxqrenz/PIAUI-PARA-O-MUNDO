from flask import Flask, request
import sqlite3
from datetime import datetime
import time
import requests

app = Flask(__name__)

# CONEXÃO COM O BANCO
conn = sqlite3.connect(
    "colmeia.db",
    check_same_thread=False
)

cursor = conn.cursor()
ultima_atividade = {}
# CRIAR TABELA
cursor.execute("""

CREATE TABLE IF NOT EXISTS leituras (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    colmeia INTEGER,

    temperatura REAL,

    som INTEGER,

    alerta TEXT,

    data TEXT

)

""")

ultimos_alertas = {}



def pode_enviar(colmeia, tipo_alerta):

    chave = f"{colmeia}_{tipo_alerta}"

    agora = time.time()

    TEMPO_RESET = 30

    # PRIMEIRA VEZ

    if chave not in ultimos_alertas:

        ultimos_alertas[chave] = agora

        return True

    # TEMPO PASSADO

    tempo_passado = agora - ultimos_alertas[chave]

    if tempo_passado >= TEMPO_RESET:

        ultimos_alertas[chave] = agora

        return True

    return False



conn.commit()

def analisar_colmeia(
    colmeia,
    temperatura,
    som
):

    alerta = "NORMAL"

    # ==========================
    # TEMPERATURA
    # ==========================

    if temperatura > 35:

        alerta = "SUPERAQUECIMENTO"

        if pode_enviar(colmeia, "temperatura"):

            enviar_whatsapp(
                f"🔥 ALERTA COLMEIA {colmeia} TEMPERATURA {temperatura}C"
            )

    # ==========================
    # SOM
    # ==========================

    if som > 2500:

        alerta = "ESTRESSE SONORO"

        if pode_enviar(colmeia, "som"):

            enviar_whatsapp(
                f"🔊 ALERTA COLMEIA {colmeia} SOM {som}Hz"
            )

    # ==========================
    # ENXAMEAÇÃO
    # ==========================

    if temperatura > 33 and som > 2200:

        alerta = "POSSIVEL ENXAMEACAO"

        if pode_enviar(colmeia, "enxameacao"):

            enviar_whatsapp(
                f"⚠️ POSSIVEL ENXAMEACAO COLMEIA {colmeia}"
            )

    return alerta



def verificar_colmeias_offline():

    offline = []

    agora = time.time()

    for colmeia, ultimo_envio in ultima_atividade.items():

        tempo_sem_dados = agora - ultimo_envio

        if tempo_sem_dados > 60:

            offline.append(colmeia)

    return offline

def enviar_whatsapp(mensagem):

    numero = "558994358353"

    api_key = "3278509"

    url = f"https://api.callmebot.com/whatsapp.php?phone={numero}&text={mensagem}&apikey={api_key}"

    requests.get(url)


@app.route("/dados", methods=["POST"])
def dados():

    conteudo = request.json

    colmeia = conteudo["colmeia"]
    ultima_atividade[colmeia] = time.time()

    temperatura = conteudo["temperatura"]

    som = conteudo["som"]

    alerta = analisar_colmeia(
        colmeia,
        temperatura,
        som
    )

    data = datetime.now().strftime(
        "%d/%m/%Y %H:%M:%S"
    )

    cursor.execute("""

    INSERT INTO leituras
    (
        colmeia,
        temperatura,
        som,
        alerta,
        data
    )

    VALUES (?, ?, ?, ?, ?)

    """, (
        colmeia,
        temperatura,
        som,
        alerta,
        data
    ))

    conn.commit()

    print("\nDADOS SALVOS:")

    print(conteudo)

    print("\nALERTA:")

    print(alerta)

    return "OK", 200






app.run(
    host="0.0.0.0",
    port=3000
)