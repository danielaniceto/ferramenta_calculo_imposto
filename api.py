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
        
        pega_receita_bruta = request.form.get("Renda Bruta")

        CalculoSimplesNacional.calcular_simples_nacional_menor_180k(
             
        )
        return redirect ("/resultado_simples_nacional")

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
