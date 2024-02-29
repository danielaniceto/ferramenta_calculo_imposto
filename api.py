import json
from cliente import Cliente
from simples_nacional import *
from flask import Flask, Response, request, jsonify

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/simples_nacional', methods=['POST'])
def is_CalculoImpostoSimplesNacionalAnexo01_menor180k():

    get_receita_bruta = float(request.args.get('receita_bruta'))

    simples_nacional = SimplesNacional.calcular_simples_nacional_menor_180k(
        receita_bruta=get_receita_bruta,
        porcentagem_alicota = 0.04,
        faixa_desconto=0
        )
    return Response(json.dumps(simples_nacional), mimetype="application/json")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
