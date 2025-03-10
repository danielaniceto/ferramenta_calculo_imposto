from typing import List, Dict
from calculos.simples_nacional import CalculoSimplesNacional
from calculos.icms import CalculoIcms
from calculos.lucropresumido import CalculoLucroPresumido
from calculos.lucroreal import CalculoLucroReal

class ValidaReceita:
  @staticmethod
  def valida_receita_simples_nacional(receita_bruta:float):
    if receita_bruta < 0:
      raise Exception("Impossível Calcular Simples Nacional com receita negativa")
          
    elif receita_bruta > 4800000 and receita_bruta <= 5760000:
      raise ValueError("Com base no valor da receita fornecida, seu imposto será calculado com o valor teto de contribuição, e com valor teto de descontos, porém, para o próximo ano, sua empresa será desenquadrada dessa modalidade")

    elif receita_bruta > 5760000:
      raise ValueError("Sua receita anual, estrapola o teto de valor para calculo nessa modalidade")
      
    return("TUDO OK, VALIDAÇÃO FEITA COM SUCESSO!!!")
  
  @staticmethod
  def valida_valor_icms(valor_do_produto_servico:float):
    if valor_do_produto_servico < 0:
      raise Exception("Impossível Calcular ICMS com valor do produto ou serviço negativo")
    
    return("TUDO OK, VALIDAÇÃO DE VALOR DE PRODUTO OU SERVIÇO FEITA COM SUCESSO!!!")
  
  @staticmethod
  def valida_receita_bruta_lucro_presumido(renda_bruta:float):
    if renda_bruta < 0:
      raise Exception("Impossível Calcular o imposto Lucro Presumido com valor do produto ou serviço negativo")
    
    elif renda_bruta > 78000000:
      raise Exception("Sua empresa não pode ser enquadrada nessa modalidade imposto, por ter receita bruta anual maior que o teto de R$78 milhões")
    
    return("TUDO OK, VALIDAÇÃO FEITA COM SUCESSO!!!")
  
  @staticmethod
  def valida_lucro_real(lucro_real_empresa: float, periodo: str):
    if lucro_real_empresa < 0:
      raise Exception("Impossível Calcular o imposto Lucro Real com lucro negativo")
    
    if periodo == "Trimestral":
      if lucro_real_empresa > 60000:
        valor_adional_lucro_real = lucro_real_empresa - 60000
        raise Exception("Seu lucro liquido estrapola o valor maximo para aliquota padrão, o calculo será feito adicionando 10% a mais sobre o valor que exceder os R$ 60.000,00 dentro do trimestre, no caso da sua empresa o valor e de R$ {valor_adional_lucro_real}")
      
      return("TUDO OK, VALIDAÇÃO FEITA COM SUCESSO!!!")
    
    elif periodo == "Anual":
      if lucro_real_empresa > 240000:
        valor_adional_lucro_real = lucro_real_empresa - 240000
        raise Exception("Seu lucro liquido estrapola o valor maximo para aliquota padrão, o calculo será feito adicionando 10% a mais sobre o valor que exceder os R$ 240.000,00 dentro do ano, no caso da sua empresa o valor e de R$ {valor_adional_lucro_real}")
      
      return("TUDO OK, VALIDAÇÃO FEITA COM SUCESSO!!!")

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

  def __init__(self, receita_bruta:float, anexos:str, porcentagem_aliquota:float=None, faixa_desconto:float=None):
    self.anexos = str(anexos)
    self.receita_bruta = float(receita_bruta)

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
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_01:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:        
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND = {tributacao}")
        return tributacao
    return {}

  @staticmethod
  def __get_tributacao_anexo02_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_02:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:          
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
      
  @staticmethod
  def __get_tributacao_anexo03_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_03:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
        tributacao["receita_bruta"] = receita_bruta
        print(F"EU SOU A TRIBUTAÇÃO DEPOIS DO APPEND {tributacao}")
        return tributacao
    return {}
    
  @staticmethod
  def __get_tributacao_anexo04_side(receita_bruta:float)->dict:
    for tributacao in SimplesNacional.TRIBUTACOES_ANEXO_04:
      if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:        
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
    self.estado = str(estado)
    print(f"EU SOU O ESTADO DENTRO DA DEF INIT DO ICMS {estado}")
  
    side_tributacao_icms = self.__get_tributacao_estados_side(self.estado, self.valor_produto)

    if aliquota is None:
      self.aliquota = side_tributacao_icms.get("aliquota")
      print(f"EU SOU A ALIQUOTA DO ESTADO {self.aliquota}")

  @staticmethod
  def __get_tributacao_estados_side(estado:str, valor_produto:float)->dict:
    for tributacao_icms in ICMS.TRIBUTACOES_ESTADOS_2024:
      if estado == tributacao_icms.get("estado"):
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao_icms}")

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

class LucroPresumido:

  TRIBUTACOES_ATIVIDADES_LUCRO_PRESUMIDO: List[Dict[str, float]] = [
    {"atividade": "Atividade 01", "aliquota": 0.016},
    {"atividade": "Atividade 02", "aliquota": 0.08},
    {"atividade": "Atividade 03", "aliquota": 0.08},
    {"atividade": "Atividade 04", "aliquota": 0.08},
    {"atividade": "Atividade 05", "aliquota": 0.08},
    {"atividade": "Atividade 06", "aliquota": 0.16},
    {"atividade": "Atividade 07", "aliquota": 0.32},
    {"atividade": "Atividade 08", "aliquota": 0.32},
    {"atividade": "Atividade 09", "aliquota": 0.32},
    {"atividade": "Atividade 10", "aliquota": 0.32},
  ]

  def __init__(self, renda_bruta:float, atividade:str, aliquota:float=None):
    self.atividade = str(atividade)
    self.renda_bruta = float(renda_bruta)
    print(f"EU SOU A ATIVIDADE DENTRO DA INIT LUCRO PRESUMIDO {atividade}")
    print(f"EU SOU A RENDA BRUTA DENTRO DA INIT LUCRO PRESUMIDO {renda_bruta}")

    side_tributacao_lucro_presumido = self.__get_tributacao_atividades_side(self.atividade, self.renda_bruta)

    if renda_bruta < 0:
      raise Exception ("Impossível calcular seu imposto com a renda bruta negativa")
    
    if aliquota is None:
      self.aliquota = side_tributacao_lucro_presumido.get("aliquota")

  @staticmethod
  def __get_tributacao_atividades_side(atividade: str, renda_bruta:float)->dict:
    for tributacao_lucro_presumido in LucroPresumido.TRIBUTACOES_ATIVIDADES_LUCRO_PRESUMIDO:
      if atividade == tributacao_lucro_presumido.get("atividade"):
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao_lucro_presumido}")
        
        tributacao_lucro_presumido["renda_bruta"] = renda_bruta
        print(f"EU SOU A TRIBUTACAO DEPOIS DO APPEND{tributacao_lucro_presumido}")
        return tributacao_lucro_presumido
    return {}
    
  @staticmethod
  def calcula_imposto_lucro_presumido(receita_bruta:float, atividade:str)->float:
    renda_bruta = float(receita_bruta)
    atividade = str(atividade)
    side_tributacao_lucro_presumido = LucroPresumido.__get_tributacao_atividades_side(atividade, renda_bruta)
    print(f"EU SOU O SIDE TRIBUTACAO DENTRO DA FUNCAO CALCULA LUCRO PRESUMIDO {side_tributacao_lucro_presumido}")
    valor_imposto_lucro_presumido = CalculoLucroPresumido.calcular_lucro_presumido(side_tributacao_lucro_presumido)
    
    print(f"EU SOU O RETORNO DA FUNCAO CALCULAR LUCRO PRESUMIDO DENTRO DA CONTROLLER {valor_imposto_lucro_presumido}")

    return valor_imposto_lucro_presumido

class LucroReal:

  TRIBUTACOES_ATIVIDADES_LUCRO_REAL: List[Dict[str, float]] = [
    {"seguradoraoufinanceira": "Sim", "aliquota": 0.15},
    {"seguradoraoufinanceira": "Não", "aliquota": 0.09},
  ]

  def __init__(self, periodo: str, lucro_real_empresa:float, tributacao_especial_csll:str):
    self.lucro_real_empresa = float(lucro_real_empresa)
    self.tributacao_especial_csll = str(tributacao_especial_csll)
    self.periodo = str(periodo)
    print(f"EU SOU A ATIVIDADE DENTRO DA INIT LUCRO PRESUMIDO {lucro_real_empresa}")
    print(f"EU SOU A RENDA BRUTA DENTRO DA INIT LUCRO PRESUMIDO {tributacao_especial_csll}")
    print(f"EU SOU O PERIODO DE AVALIACAO DENTRO DA INIT {periodo}")

    if lucro_real_empresa < 0:
      raise Exception ("Lucro real negativo, não cabe a aplicação de pagamento de impostos!!!")
    
    side_tributacao_lucro_real = self.__get_tributacao_lucro_real_side(self.tributacao_especial_csll, self.lucro_real_empresa, periodo)

  @staticmethod
  def __get_tributacao_lucro_real_side(tributacao_especial_csll:str, lucro_real_empresa:float, periodo:int)->dict:
    for tributacao_lucro_real in LucroReal.TRIBUTACOES_ATIVIDADES_LUCRO_REAL:
      if tributacao_especial_csll == tributacao_lucro_real.get("seguradoraoufinanceira"):
        print(F"EU SOU A TRIBUTAÇÃO ANTES DO APPEND {tributacao_lucro_real}")
          
        tributacao_lucro_real["lucro_real_empresa"] ["periodo"] = lucro_real_empresa, periodo
        print(f"EU SOU A TRIBUTACAO LUCRO REAL DEPOIS DO APPEND{tributacao_lucro_real}")
        return tributacao_lucro_real
    return {}
    
  @staticmethod
  def calcula_imposto_lucro_real(periodo:str, lucro_real_empresa:float, tributacao_especial_csll:str)->float:
    lucro_real_empresa = float(lucro_real_empresa)
    periodo = str(periodo)
    tributacao_especial_csll = str(tributacao_especial_csll)

    side_tributacao_lucro_real = LucroReal.__get_tributacao_lucro_real_side(lucro_real_empresa, periodo, tributacao_especial_csll)
    print(f"EU SOU O SIDE TRIBUTACAO DENTRO DA FUNCAO CALCULA LUCRO PRESUMIDO {side_tributacao_lucro_real}")
    valor_imposto_lucro_presumido = CalculoLucroReal.calcular_lucro_real(side_tributacao_lucro_real)
    
    print(f"EU SOU O RETORNO DA FUNCAO CALCULAR LUCRO PRESUMIDO DENTRO DA CONTROLLER {valor_imposto_lucro_presumido}")

    return valor_imposto_lucro_presumido
