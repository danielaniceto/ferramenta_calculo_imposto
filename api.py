from main import *
from calculos.simples_nacional import *
from app.models import *
from app.controller import *
from flask import Flask, request, render_template

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("escolha_imposto.html")

@app.route('/simples_nacional', methods=['POST'])
def is_CalculoImpostoSimplesNacional():

    anexos = str(request.form.get("Anexos_Simples_Nacional"))
    print(f"EU SOU O ANEXO VINDO DO FORMS = {anexos}")

    receita_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS = {receita_bruta}")

    validacao_simples_nacional = SimplesNacional(receita_bruta, anexos)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {validacao_simples_nacional}")

    valor_simples_nacional = SimplesNacional.calcula_simples_nacional(receita_bruta, anexos)
        
    return render_template ("/resultados_calculos_imposto.html", imposto_simples_nacional = valor_simples_nacional)

@app.route('/icms', methods=['POST'])
def is_CalculoICMS():

    estado = str(request.form.get("Estados"))

    return render_template("/icms")



if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
