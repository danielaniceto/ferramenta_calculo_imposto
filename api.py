from main import *
from calculos.simples_nacional import *
from app.models import *
from app.controller import *
from flask import Flask, request, render_template

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("receita_bruta.html")

@app.route('/resultados_calculos_imposto', methods=['POST'])
def is_CalculoImpostoSimplesNacional():

    attachment = str(request.form.get("Anexos_Simples_Nacional"))
    print(f"EU SOU O ANEXO VINDO DO FORMS = {attachment}")

    estado = str(request.form.get("Estados"))

    receita_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS = {receita_bruta}")

    validacao_simples_nacional = SimplesNacional(receita_bruta, attachment)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {validacao_simples_nacional}")

    valor_simples_nacional = SimplesNacional.calcula_simples_nacional(receita_bruta, attachment)

    icms = "DANIEL PASSOU POR AQUI"
    mei = "DANIEL PASSOU POR AQUI TAMBÉM"
        
    return render_template ("/resultados_calculos_imposto.html", imposto_simples_nacional = valor_simples_nacional, imposto_icms = icms, imposto_mei = mei)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
