from flask import Flask, request

app = Flask(__name__)

@app.route("/dados", methods=["POST"])
def dados():

    conteudo = request.json

    print("\nDADOS RECEBIDOS:")

    print(conteudo)

    return "OK", 200

app.run(
    host="0.0.0.0",
    port=3000
)