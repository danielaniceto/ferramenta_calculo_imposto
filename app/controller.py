from typing import List, Dict
from calculos.simples_nacional import CalculoSimplesNacional

class SimplesNacionalAnexo01:    
    
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
    side_tributacao_anexo01 = self.__get_tributacao_anexo01_side(self.receita_bruta)

    if receita_bruta < 0:
       raise Exception("Impossível Calcular Simples Nacional com receita negativa")
    
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
       raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
       raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")

    if porcentagem_aliquota is None:
      self.porcentagem_aliquota = side_tributacao_anexo01.get("aliquota")
      print(F"EU SOU A PORCENTAGEM {self.porcentagem_aliquota}")

    else:
      self.porcentagem_aliquota = porcentagem_aliquota
            
    if faixa_desconto is None:
      self.faixa_desconto = side_tributacao_anexo01.get("desconto")
      print(f"EU SOU O DESCONTO {self.faixa_desconto}")
      
    else:
      self.faixa_desconto = faixa_desconto
      print(f"EU SOU O SIDE_TRIBUTACAO {side_tributacao_anexo01}")

  @staticmethod
  def __get_tributacao_anexo01_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacionalAnexo01.TRIBUTACOES_ANEXO_01:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
      return {}
  
  @staticmethod
  def calcula_simples_nacional_anexo01(receita_bruta:float)->float:
    receita_bruta = float(receita_bruta)
    side_tributacao = SimplesNacionalAnexo01.__get_tributacao_anexo01_side(receita_bruta)
    valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao)
    print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
          
    return valor_simples_nacional
  
class SimplesNacionalAnexo02:
   
  TRIBUTACOES_ANEXO_02: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.045, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.078, "desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.01, "desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.112, "desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.147, "desconto": 85500},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.30, "desconto": 720000}
  ]
   
  def __init__(self, receita_bruta:float, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.receita_bruta = float(receita_bruta)
    side_tributacao_anexo02 = self.__get_tributacao_anexo02_side(self.receita_bruta)

    if receita_bruta < 0:
       raise Exception("Impossível Calcular Simples Nacional com receita negativa")
    
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
       raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
       raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")

    if porcentagem_aliquota is None:
      self.porcentagem_aliquota = side_tributacao_anexo02.get("aliquota")
      print(F"EU SOU A PORCENTAGEM {self.porcentagem_aliquota}")

    else:
      self.porcentagem_aliquota = porcentagem_aliquota
            
    if faixa_desconto is None:
      self.faixa_desconto = side_tributacao_anexo02.get("desconto")
      print(f"EU SOU O DESCONTO {self.faixa_desconto}")
      
    else:
       self.faixa_desconto = faixa_desconto
       print(f"EU SOU O SIDE_TRIBUTACAO {side_tributacao_anexo02}")

  @staticmethod
  def __get_tributacao_anexo02_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacionalAnexo02.TRIBUTACOES_ANEXO_02:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
      return {}
  
  @staticmethod
  def calcula_simples_nacional_anexo02(receita_bruta:float)->float:
    receita_bruta = float(receita_bruta)
    side_tributacao = SimplesNacionalAnexo02.TRIBUTACOES_ANEXO_02(receita_bruta)
    valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao)
    print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
          
    return valor_simples_nacional
  