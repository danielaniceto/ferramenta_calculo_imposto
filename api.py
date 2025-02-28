from main import *
from calculos.simples_nacional import *
from calculos.icms import *
from calculos.lucropresumido import *
from app.models import *
from app.controller import *
from flask import Flask, request, render_template, redirect

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

    valida_receita_bruta = ValidaReceita.valida_receita_simples_nacional(receita_bruta)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {valida_receita_bruta}")

    SimplesNacional(receita_bruta, anexos)

    valor_simples_nacional = SimplesNacional.calcula_simples_nacional(receita_bruta, anexos)
        
    return render_template ("/resultado_simples_nacional.html", imposto_simples_nacional = valor_simples_nacional)

@app.route('/lucro_presumido', methods=["POST"])
def isApresentaLucroPresumido():
    return render_template("lucro_presumido.html")

@app.route('/resultado_lucro_presumido', methods=['POST'])
def is_CalculoImpostoLucroPresumido():
    renda_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS = {renda_bruta}")

    atividade = str(request.form.get("atividades"))
    print(F"EU SOU ATIVIDADE VINDO DO FORMS = {atividade}")

    valida_receita_bruta = ValidaReceita.valida_receita_bruta_lucro_presumido(renda_bruta)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {valida_receita_bruta}")

    LucroPresumido(renda_bruta, atividade)

    resultado_lucro_presumido = LucroPresumido.calcula_imposto_lucro_presumido(renda_bruta, atividade)

    return render_template ("/resultado_lucro_presumido.html", imposto_lucro_presumido = resultado_lucro_presumido)

@app.route('/lucro_real', methods=['POST'])
def isApresentaLucroReal():
    return render_template("lucro_real.html")

@app.route('/resultado_calculo_imposto_lucro_real', methods=['POST'])
def is_CalculoImpostoLucroReal():
    periodo = str(request.form.get("periodo"))
    print(f"EU SOU O PERIODO DE AVALIACAO VINDO DO FORMS = {periodo}")

    lucro_real_empresa = float(request.form.get("lucro"))
    print(F"EU SOU O VALOR LUCRO REAL VINDO DO FORMS = {lucro_real_empresa}")

    tributacao_especial_csll = str(request.form.get("SimOuNao"))
    print(f"EU SOU O RETORNO DA OPCAO NO HTML DA SEGURADORA OU FINANCEIRA = {tributacao_especial_csll}")

    valida_receita_bruta = ValidaReceita.valida_lucro_real(lucro_real_empresa, periodo)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO = {valida_receita_bruta}")

    LucroReal(periodo, lucro_real_empresa, tributacao_especial_csll)

    resultado_lucro_real = LucroReal.calcula_imposto_lucro_real(periodo, lucro_real_empresa, tributacao_especial_csll)

    return render_template ("/resultado_lucro_real.html", imposto_lucro_real = resultado_lucro_real)

@app.route('/icms', methods=['POST'])
def isApresetaICMS():
    return render_template("icms.html")

@app.route('/resultado_calculo_imposto_icms', methods=['POST'])
def is_CalculoImpostoIcms():

    valor_do_produto_servico = float(request.form.get("valor_produto_servico"))
    print(f"EU SOU O VALOR DO PRODUTO VINDO DO FORMS = {valor_do_produto_servico}")

    estado = str(request.form.get("Estados"))
    print(F"EU SOU O ESTADO VINDO DO FORMS = {estado}")

    validacao_valor_produto = ValidaReceita.valida_valor_icms(valor_do_produto_servico)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO PRODUTO = {validacao_valor_produto}")

    valor_icms = ICMS.calcula_icms(valor_do_produto_servico, estado)
    print(f"EU SOU O RETONO DO VALOR DO IMPOSTO VINDO DO CALCULO = {estado, valor_icms}")
        
    return render_template ("/resultado_icms.html", imposto_icms = valor_icms)

"""@app.route('/mei', methods=['POST'])
def isApresetaMEI():
    return render_template("mei.html")"""

"""app.route('/resultado_calculo_imposto_mei', methods=['POST'])
def is_CalculoImpostoMei():"""

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
