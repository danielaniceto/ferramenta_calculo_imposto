from main import *
from calculos.simples_nacional import *
from app.models import SimplesNacional
from flask import Flask, Response, request, redirect, render_template, url_for

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("receita_bruta.html")

@app.route('/resultado_simples_nacional_anexo01', methods=['POST'])
def is_CalculoImpostoSimplesNacionalAnexo01_menor180k():
        
        simples = SimplesNacional(int(receita_bruta = request.form.get("renda_bruta")), porcentagem_alicota = 0.04, faixa_desconto = 0)

        valor_simples_nacional_menor_180k = CalculoSimplesNacional().calcular_simples_nacional_menor_180k(simples)

        return render_template ("/resultado_simples_nacional_anexo01.html", imposto_simples_nacional = valor_simples_nacional_menor_180k)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
