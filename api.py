import json
from main import *
from calculos.simples_nacional import *
from flask import Flask, Response, request, redirect, render_template, url_for

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("receita_bruta.html")

@app.route('/resultado_simples_nacional', methods=['POST'])
def is_CalculoImpostoSimplesNacionalAnexo01_menor180k():
    pega_receita_bruta = request.form["renda_bruta"]

    imposto_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional_menor_180k(
        receita_bruta = pega_receita_bruta,
        porcentagem_alicota = 0.04, #valor fixo segundo tabela de imposto
        faixa_desconto = 0 #valor fixo segundo tabela de imposto
        )
    
    return render_template("resultado_simples_nacional.html", imposto_simples_nacional=imposto_simples_nacional)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
