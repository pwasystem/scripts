from flask import Flask, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Dados de exemplo
dados = [
    {
        "estado": "São Paulo",
        "sigla": "SP",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "temperatura": 25.4,
        "precipitacao": 185
    },
    {
        "estado": "Rio de Janeiro",
        "sigla": "RJ",
        "data": datetime.now().strftime("%Y-%m-%d"),
        "temperatura": 28.1,
        "precipitacao": 120
    }
]

@app.route('/clima', methods=['GET'])
def get_clima():
    return jsonify(dados)

@app.route('/clima/<uf>', methods=['GET'])
def get_clima_uf(uf):
    uf = uf.upper()
    resultado = next((item for item in dados if item["sigla"] == uf), None)
    return jsonify(resultado) if resultado else ("UF não encontrada", 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)