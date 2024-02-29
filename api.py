import json
from simples_nacional import *
from flask import Flask, Response, request

simples_nacional = SimplesNacional.calcular_simples_nacional()

app = Flask(__name__)

@app.get('/simples_nacional')
def obterCalculoImpostoSimplesNacionalAnexo01():
  return Response(json.dumps(simples_nacional), mimetype="application/json")

app.run(host="0.0.0.0", port=5000)

