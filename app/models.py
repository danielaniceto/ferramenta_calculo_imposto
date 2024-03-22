import uuid

class Cliente:
  def __init__(self, id, nome_empresa, cnpj):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj

class SimplesNacional:
    def __init__(self, receita_bruta, faixa_desconto, porcentagem_aliquota):
        self.receita_bruta = float(receita_bruta)
        self.faixa_desconto = float(faixa_desconto)
        self.aliquota = float(porcentagem_aliquota)

        