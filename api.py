from main import *
from calculos.simples_nacional import *
from calculos.icms import *
from calculos.lucropresumido import *
from app.models import *
from app.controller import *
from flask import Flask, request, render_template, redirect

#empresa = Cliente("Maiore", 0000000000000)

app = Flask(__name__)

@app.route('/')
def recebe_receita_html():
    return render_template("escolha_imposto.html")

@app.route('/simples_nacional', methods=['POST'])
def isApresetaSimplesNacional():
    return render_template("simples_nacional.html")

@app.route('/resultado_calculo_imposto_simples_nacional', methods=['POST'])
def is_CalculoImpostoSimplesNacional():

    receita_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS = {receita_bruta}")

    anexos = str(request.form.get("Anexos_Simples_Nacional"))
    print(f"EU SOU O ANEXO VINDO DO FORMS = {anexos}")

    valida_receita_bruta = Valida_Receita(receita_bruta)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {valida_receita_bruta}")

    SimplesNacional(receita_bruta, anexos)

    valor_simples_nacional = SimplesNacional.calcula_simples_nacional(receita_bruta, anexos)
        
    return render_template ("/resultado_simples_nacional.html", imposto_simples_nacional = valor_simples_nacional)

@app.route('/lucro_presumido', methods=["POST"])
def isApresentaLucroPresumido():
    return render_template("lucro_presumido.html")

app.route('/resultado_lucro_presumido', methods=['POST'])
def is_CalculoImpostoLucroPresumido():
    receita_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS = {receita_bruta}")

    atividade = str(request.form.get("Estados"))
    print(F"EU SOU O ESTADO VINDO DO FORMS = {atividade}")

    resultado_lucro_presumido = 

    return render_template ("/resultado_lucro_presumido.html", resultado_lucro_presumido = resultado_lucro_presumido)

@app.route('/lucro_real', methods=['POST'])
def isApresentaLucroReal():
    return render_template("lucro_real.html")

"""app.route('/resultado_lucro_real', methods=['POST'])
def is_CalculoImpostoLucroReal():"""

@app.route('/icms', methods=['POST'])
def isApresetaICMS():
    return render_template("icms.html")

@app.route('/resultado_calculo_imposto_icms', methods=['POST'])
def is_CalculoImpostoIcms():

    valor_do_produto = float(request.form.get("valor_produto_servico"))
    print(f"EU SOU O VALOR DO PRODUTO VINDO DO FORMS = {valor_do_produto}")

    estado = str(request.form.get("Estados"))
    print(F"EU SOU O ESTADO VINDO DO FORMS = {estado}")

    validacao_valor_produto = ICMS(valor_do_produto, estado)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO PRODUTO = {validacao_valor_produto}")

    valor_icms = ICMS.calcula_icms(valor_do_produto, estado)
    print(f"EU SOU O RETONO DO VALOR DO IMPOSTO VINDO DO CALCULO = {estado, valor_icms}")
        
    return render_template ("/resultado_icms.html", imposto_icms = valor_icms)

@app.route('/mei', methods=['POST'])
def isApresetaMEI():
    return render_template("mei.html")

"""app.route('/resultado_calculo_imposto_mei', methods=['POST'])
def is_CalculoImpostoMei():"""

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
