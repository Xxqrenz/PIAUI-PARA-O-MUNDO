from flask import Flask, request
import sqlite3
from datetime import datetime
import time
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
conn.commit()
def analisar_colmeia(
    temperatura,
    som
):

    alerta = "NORMAL"

    if temperatura > 35:

        alerta = "SUPERAQUECIMENTO"

    elif som > 2500:

        alerta = "ESTRESSE SONORO"

    elif (
        temperatura > 33
        and
        som > 2200
    ):

        alerta = "POSSIVEL ENXAMEACAO"

    return alerta

def verificar_colmeias_offline():

    offline = []

    agora = time.time()

    for colmeia, ultimo_envio in ultima_atividade.items():

        tempo_sem_dados = agora - ultimo_envio

        if tempo_sem_dados > 60:

            offline.append(colmeia)

    return offline
@app.route("/dados", methods=["POST"])
def dados():

    conteudo = request.json

    colmeia = conteudo["colmeia"]
    ultima_atividade[colmeia] = time.time()

    temperatura = conteudo["temperatura"]

    som = conteudo["som"]

    alerta = analisar_colmeia(
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