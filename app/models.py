#import uuid
from calculos.simples_nacional import CalculoSimplesNacional
from typing import List, Dict

"""class Cliente:
  def __init__(self, id, nome_empresa, cnpj):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj"""

class SimplesNacional:
    
  TRIBUTACOES_ANEXO_01: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.04, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.073, "desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.095, "desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.107, "desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.143, "desconto": 87300},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.19, "desconto": 378000}
  ]
   
  def __init__(self, receita_bruta:float, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.receita_bruta = float(receita_bruta)
    side_tributacao = self.__get_tributacao_anexo01_side(self.receita_bruta)

    if receita_bruta < 0:
       raise Exception("Impossível Calcular Simples Nacional com receita negativa")
    
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
       raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
       raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")

    if porcentagem_aliquota is None:
      self.porcentagem_aliquota = side_tributacao.get("aliquota")
      print(F"EU SOU A PORCENTAGEM {self.porcentagem_aliquota}")

    else:
      self.porcentagem_aliquota = porcentagem_aliquota
            
    if faixa_desconto is None:
      self.faixa_desconto = side_tributacao.get("desconto")
      print(f"EU SOU O DESCONTO {self.faixa_desconto}")
      
    else:
       self.faixa_desconto = faixa_desconto

    print(f"EU SOU O SIDE_TRIBUTACAO {side_tributacao}")

    valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao)
    print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL MODELS/SIMPLES {valor_simples_nacional}")
    return(valor_simples_nacional)

  @staticmethod
  def __get_tributacao_anexo01_side(receita_bruta:float)->dict:
        for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_01:
            if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
                print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
                
                tributacao["receita_bruta"] = receita_bruta
                print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
                return tributacao
        return {}
  
  @staticmethod
  def calcula_simples_nacional():
    valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao=SimplesNacional.__get_tributacao_anexo01_side)
    return valor_simples_nacional
    