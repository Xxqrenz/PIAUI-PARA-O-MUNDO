from flask import Flask, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# CONEXÃO COM O BANCO
conn = sqlite3.connect(
    "colmeia.db",
    check_same_thread=False
)

cursor = conn.cursor()

# CRIAR TABELA
cursor.execute("""

CREATE TABLE IF NOT EXISTS leituras (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    temperatura REAL,

    som INTEGER,

    data TEXT

)

""")

conn.commit()

@app.route("/")
def home():

    return "SERVIDOR FUNCIONANDO"

@app.route("/dados", methods=["POST"])
def dados():

    conteudo = request.json

    temperatura = conteudo["temperatura"]

    som = conteudo["som"]

    data = datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )

    cursor.execute("""

    INSERT INTO leituras
    (temperatura, som, data)

    VALUES (?, ?, ?)

    """, (
        temperatura,
        som,
        data
    ))

    conn.commit()

    print("\nDADOS SALVOS:")

    print(conteudo)

    return "OK", 200

app.run(
    host="0.0.0.0",
    port=3000
)