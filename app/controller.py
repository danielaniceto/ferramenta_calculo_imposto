from typing import List, Dict
from calculos.simples_nacional import CalculoSimplesNacional
from calculos.icms import CalculoIcms
from db import ConsultaAliquotas, ConexaoBD

class SimplesNacional:

  @staticmethod
  def print_aliquotas_anexo01():

    TRIBUTACOES_ANEXO_01: List[Dict[str, int]] = ConsultaAliquotas.consulta_aliquota_simples_nacional("aneox01")
    print(f"EU SOU O ANEXO DENTRO DA FUNCAO PRINT ALIQUOTA ANEXO 01")
    print(F"EU SOU O DICIONARIO ANEXO 01 VINDO DO BANCO")

    ConexaoBD.close_connection()

    return TRIBUTACOES_ANEXO_01

  @staticmethod
  def print_aliquotas_anexo02():
    
    TRIBUTACOES_ANEXO_02: List[Dict[str, int]] = ConsultaAliquotas.consulta_aliquota_simples_nacional("aneox02")
    print(f"EU SOU O ANEXO DENTRO DA FUNCAO PRINT ALIQUOTA ANEXO 02")
    print(F"EU SOU O DICIONARIO ANEXO 02 VINDO DO BANCO")

    ConexaoBD.close_connection()

    return TRIBUTACOES_ANEXO_02

  """TRIBUTACOES_ANEXO_03: List[Dict[str, int]] = ConsultaAliquotas.consulta_aliquota_simples_nacional("anexo03")
  print(F"EU SOU O DICIONARIO ANEXO 03 VINDO DO BANCO")

  TRIBUTACOES_ANEXO_04: List[Dict[str, int]] = ConsultaAliquotas.consulta_aliquota_simples_nacional("anexo04")
  print(F"EU SOU O DICIONARIO ANEXO 04 VINDO DO BANCO")

  TRIBUTACOES_ANEXO_05: List[Dict[str, int]] = ConsultaAliquotas.consulta_aliquota_simples_nacional("anexo05")
  print(F"EU SOU O DICIONARIO ANEXO 05 VINDO DO BANCO")"""

  def __init__(self, receita_bruta:float, anexos:str, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.anexos = str(anexos)
    self.receita_bruta = float(receita_bruta)

    if receita_bruta < 0:
      raise Exception("Impossível Calcular Simples Nacional com receita negativa")
        
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
      raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
      raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")

    if anexos == "anexos 01":
      print(F"EU SOU O ANEXO DENTRO DA CONTROLLER {self.anexos}")
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

    elif anexos == "Anexo 02":
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

    elif anexos == "Anexo 03":
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

    elif anexos == "Anexo 04":
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

    elif anexos == "Anexo 05":
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

    for tributacao in SimplesNacional.print_aliquotas_anexo01:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND = {tributacao}")
        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND = {tributacao}")
        return tributacao
      
      return {}

  @staticmethod
  def __get_tributacao_anexo02_side(receita_bruta:float)->dict:
      for tributacao in SimplesNacional.print_aliquotas_anexo02(anexo="anexo02"):
        if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
          print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao}")
          
          tributacao["receita_bruta"] = receita_bruta
          print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
          return tributacao
      return {}
      
  @staticmethod
  def __get_tributacao_anexo03_side(receita_bruta:float)->dict:
      for tributacao in SimplesNacional.print_aliquotas:
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
  def calcula_simples_nacional(receita_bruta:float, anexos:str)->float:
    if anexos == "Anexo 01":
      receita_bruta = float(receita_bruta)
      side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo01_side(receita_bruta)
      valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
              
      return valor_simples_nacional
    
    elif anexos == "Anexo 02":
        receita_bruta = float(receita_bruta)
        side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo02_side(receita_bruta)
        valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
        print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
              
        return valor_simples_nacional
      
    elif anexos == "Anexo 03":
        receita_bruta = float(receita_bruta)
        side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo03_side(receita_bruta)
        valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
        print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
              
        return valor_simples_nacional
      
    elif anexos == "Anexo 04":
        receita_bruta = float(receita_bruta)
        side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo04_side(receita_bruta)
        valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
        print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
              
        return valor_simples_nacional
      
    elif anexos == "Anexo 05":
        receita_bruta = float(receita_bruta)
        side_tributacao_anexo = SimplesNacional.__get_tributacao_anexo05_side(receita_bruta)
        valor_simples_nacional = CalculoSimplesNacional.calcular_simples_nacional(side_tributacao_anexo)
        print(f"EU SOU O RETORNO DA FUNCAO CALCULAR SIMPLES NACIONAL DENTRO DO SIMPLES NACIONAL {valor_simples_nacional}")
              
        return valor_simples_nacional
      
      
class ICMS:
    
  TRIBUTACOES_ESTADOS_2024: List[Dict[str, float]] = [
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
    
  def __init__(self, valor_produto:float, estado:str, aliquota:float=None):
    self.valor_produto = float(valor_produto)
    print(f"EU SOU O ESTADO DENTRO DA DEF INIT DO ICMS {estado}")
    self.estado = str(estado)
  
    side_tributacao_icms = self.__get_tributacao_estados_side(self.estado, self.valor_produto)

    if valor_produto < 0:
      raise Exception("Impossivel calcular ICMS com valor do produto negativo")

    if aliquota is None:
      self.aliquota = side_tributacao_icms.get("aliquota")
      print(f"EU SOU A ALIQUOTA DO ESTADO {self.aliquota}")

  @staticmethod
  def __get_tributacao_estados_side(estado:str, valor_produto:float)->dict:
    for tributacao_icms in ICMS.TRIBUTACOES_ESTADOS_2024:
      if estado == tributacao_icms.get("estado"):
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao_icms}")

        break

      tributacao_icms["valor_produto_servico"] = valor_produto
      print(F"EU SOU A TRIBUTACAO DEPOIS DO APPEND{tributacao_icms}")
    return tributacao_icms

  @staticmethod
  def calcula_icms(valor_produto:float, estado:str)->float:
      valor_produto = float(valor_produto)
      estado = str(estado)
      side_tributacao_icms = ICMS.__get_tributacao_estados_side(estado, valor_produto)
      valor_icms = CalculoIcms.calcular_icms_dentro_do_estado(side_tributacao_icms)
      print(f"EU SOU O RETORNO DA FUNCAO CALCULAR ICMS DENTRO DO CONTROLLER {valor_icms}")
            
      return valor_icms
