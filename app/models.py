import uuid
from typing import List, Dict

class Cliente:
  def __init__(self, id, nome_empresa, cnpj):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj

class SimplesNacional:
    
  TRIBUTACOES: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.04, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.073, "desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.095, "desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.107, "desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.143, "desconto": 87300},
    {"minimo": 3600001, "maximo": 4800000, "aliquota": 0.19, "desconto": 378000}
  ]
   
  def __init__(self, receita_bruta:float, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.receita_bruta = float(receita_bruta)
    side_tributacao = self.__get_tributacao_side(self.receita_bruta)

    if porcentagem_aliquota is None:
      self.porcentagem_aliquota = side_tributacao.get("aliquota")

    else:
      self.porcentagem_aliquota = porcentagem_aliquota
            
    if faixa_desconto is None:
      self.faixa_desconto = side_tributacao.get("faixa_desconto")

    else:
       self.faixa_desconto = faixa_desconto
    
    @staticmethod
    def __get_tributacao_side(receita_bruta:float)->dict:
        for tributacao in SimplesNacional.TRIBUTACOES:
            if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
                return tributacao
        return {}
    