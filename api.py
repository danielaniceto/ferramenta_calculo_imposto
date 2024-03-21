from main import *
from calculos.simples_nacional import *
from app.models import SimplesNacional
from flask import Flask, request, render_template

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("receita_bruta.html")

@app.route('/resultados_calculos_imposto', methods=['POST'])
def is_CalculoImpostoSimplesNacionalAnexo01():
        
    receita = SimplesNacional(receita_bruta=request.form.get("renda_bruta"))
    print(f"OLAAAAAAAAAAAAAAAAAA {receita}")

    valor_simples_nacional_menor_180k = CalculoSimplesNacional.calcular_simples_nacional_menor_180k(receita)

    return render_template ("/resultados_calculos_imposto.html", imposto_simples_nacional = valor_simples_nacional_menor_180k)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
