from typing import List, Dict
from calculos.simples_nacional import CalculoSimplesNacional
#from calculos.icms import CalculoIcms

class SimplesNacional:
    
  TRIBUTACOES_ANEXO_01: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.04, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.073, "desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.095, "desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.107, "desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.143, "desconto": 87300},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.19, "desconto": 378000}
  ]

  TRIBUTACOES_ANEXO_02: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.045, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.078, "desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.10, "desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.112, "desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.147, "desconto": 85500},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.30, "desconto": 720000}
  ]

  TRIBUTACOES_ANEXO_03: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.06, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.112, "desconto": 9360},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.135, "desconto": 17640},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.16, "desconto": 35640},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.21, "desconto": 125640},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.33, "desconto": 648000}
  ]

  TRIBUTACOES_ANEXO_04: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.045, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.09, "desconto": 9360},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.102, "desconto": 17640},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.14, "desconto": 35640},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.22, "desconto": 125640},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.33, "desconto": 648000}
  ]

  TRIBUTACOES_ANEXO_05: List[Dict[str, int]] = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.155, "desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.18, "desconto": 9360},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.195, "desconto": 17640},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.205, "desconto": 35640},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.23, "desconto": 125640},
    {"minimo": 3600001, "maximo": 5760000, "aliquota": 0.3005, "desconto": 648000}
  ]

  def __init__(self, receita_bruta:float, anexo:str, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.anexo = str(anexo)
    self.receita_bruta = float(receita_bruta)

    if receita_bruta < 0:
      raise Exception("Impossível Calcular Simples Nacional com receita negativa")
      
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
      raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
      raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")

    if anexo == "Anexo 01":
      print(F"EU SOU O ANEXO DENTRO DA CONTROLLER {self.anexo}")
      side_tributacao = self.__get_tributacao_anexo01_side(self.receita_bruta)

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

    elif anexo == "Anexo 02":
      side_tributacao = self.__get_tributacao_anexo02_side(self.receita_bruta)

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

    elif anexo == "Anexo 03":
      side_tributacao = self.__get_tributacao_anexo03_side(self.receita_bruta)
      
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

    elif anexo == "Anexo 04":
      side_tributacao = self.__get_tributacao_anexo04_side(self.receita_bruta)
      
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

    elif anexo == "Anexo 05":
      side_tributacao = self.__get_tributacao_anexo05_side(self.receita_bruta)
      
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


  @staticmethod
  def __get_tributacao_anexo01_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_01:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND = {tributacao}")
            
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND = {tributacao}")
        return tributacao
    return {}
    
  @staticmethod
  def __get_tributacao_anexo02_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_02:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
    
  @staticmethod
  def __get_tributacao_anexo03_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_03:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
  
  @staticmethod
  def __get_tributacao_anexo04_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_04:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
  
  @staticmethod
  def __get_tributacao_anexo05_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_05:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
    
  @staticmethod
  def calcula_simples_nacional(receita_bruta:float, attachment:str)->float:
    if attachment == "Anexo 01":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo01_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
  
    elif attachment == "Anexo 02":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo02_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
    
    elif attachment == "Anexo 03":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo03_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
    
    elif attachment == "Anexo 04":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo04_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
    
    elif attachment == "Anexo 05":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo05_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
    
class ICMS:
    
  TRIBUTACOES_ESTADOS_2024: List[Dict[str, int]] = [
    {"estado": "MINASGERAIS", "aliquota": 0.18},
    {"estado": "SAOPAULO", "aliquota": 0.18},
    {"estado": "RIODEJANEIRO", "aliquota": 0.22},
    {"estado": "RIOGRANDEDOSUL", "aliquota": 0.17},
    {"estado": "PARANA", "aliquota": 0.195},
    {"estado": "SANTACATARINA", "aliquota": 0.17},
    {"estado": "BAHIA", "aliquota": 0.205},
    {"estado": "DISTRITOFEDERAL", "aliquota": 0.20},
    {"estado": "GOIAS", "aliquota": 0.19},
    {"estado": "PARA", "aliquota": 0.19},
    {"estado": "MATOGROSSO", "aliquota": 0.17},
    {"estado": "PERNAMBUCO", "aliquota": 0.205},
    {"estado": "CEARA", "aliquota": 0.20},
    {"estado": "ESPIRITOSANTO", "aliquota": 0.17},
    {"estado": "MATOGROSSODOSUL", "aliquota": 0.17},
    {"estado": "AMAZONAS", "aliquota": 0.20},
    {"estado": "MARANHAO", "aliquota": 0.22},
    {"estado": "RIOGRANDEDONORTE", "aliquota": 0.205},
    {"estado": "PARAIBA", "aliquota": 0.20},
    {"estado": "ALAGOAS", "aliquota": 0.19},
    {"estado": "PIAUI", "aliquota": 0.21},
    {"estado": "RONDONIA", "aliquota": 0.195},
    {"estado": "SERGIPE", "aliquota": 0.19},
    {"estado": "TOCANTINS", "aliquota": 0.20},
    {"estado": "ACRE", "aliquota": 0.19},
    {"estado": "AMAPA", "aliquota": 0.18},
    {"estado": "RORAIMA", "aliquota": 0.205}
  ]
    
  def __init__(self, estado:str, aliquota:float=None, valor_produto:float=None):
    self.aliquota = float(aliquota)
    self.estado = str(estado)
    self.valor_produto =float(valor_produto)

    if valor_produto < 0:
      raise Exception("Impossivel calcular ICMS com valor do produto negativo")
  
    side_tributacao_icms = self.__get_tributacao_estados_side(self.estado, self.valor_produto)

  @staticmethod
  def __get_tributacao_estados_side(estado:str, valor_produto:float)->dict:
    for tributacao_icms in ICMS.TRIBUTACOES_ESTADOS_2024:
      if estado == ICMS.TRIBUTACOES_ESTADOS_2024["estado"]:
        aliquota = ICMS.TRIBUTACOES_ESTADOS_2024["aliquota"]
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao_icms}")

        tributacao_icms["valor_produto_servico"] = valor_produto
        tributacao_icms["aliquota"] = aliquota
        print(F"EU SOU A TRIBUTACAO DEPOIS DO APPEND")
        return tributacao_icms
    return {}

  @staticmethod
  def calcula_icms(valor_produto:float, aliquota:str)->float:
      valor_produto = float(valor_produto)
      aliquota = float(aliquota)
      side_tributacao_icms = SimplesNacional.__get_tributacao_estados_side(estado)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
  
  ###########################################

  def calcula_simples_nacional(receita_bruta:float, attachment:str)->float:
    if attachment == "Anexo 01":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo01_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
            
      return valor_simples_nacional
  
    elif attachment == "Anexo 02":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo02_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")