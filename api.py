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
        
    receita_bruta = float(request.form.get("renda_bruta"))
    print(f"EU SOU A RECEITA BRUTA VINDA DO FORMS {receita_bruta}")

    valida_valor_simples_nacional = SimplesNacional(receita_bruta)
    print(f"EU SOU O RETONO DA VALIDACAO DO VALOR DO IMPOSTO {valida_valor_simples_nacional}")

    valor_simples_nacional = SimplesNacional.calcula_simples_nacional(receita_bruta)
    print(print(f"EU SOU O RETORNO VALOR SIMPLES NACIONAL DENTRO DA API {valor_simples_nacional}"))
    
    return render_template ("/resultados_calculos_imposto.html", imposto_simples_nacional = valor_simples_nacional)

if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
