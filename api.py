import json
from main import *
from cliente import Cliente
from calculos.simples_nacional import *
from flask import Flask, Response, request, jsonify

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/simples_nacional', methods=['GET'])
def is_CalculoImpostoSimplesNacionalAnexo01_menor180k():

    pega_receita_bruta["renda_bruta"] = float(request.args.get('renda_bruta'))

    simples_nacional = SimplesNacional.calcular_simples_nacional_menor_180k(
        self = None,
        receita_bruta=pega_receita_bruta,
        porcentagem_alicota = 0.04,
        faixa_desconto=0
        )
    return Response(json.dumps(simples_nacional), mimetype="application/json")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
