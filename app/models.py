import uuid
import json

class Cliente:
  def __init__(self, id, nome_empresa, cnpj):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj

class SimplesNacional:
    def __init__(self, receita_bruta, porcentagem_alicota, faixa_desconto):
        self.receita_bruta = receita_bruta
        self.porcentagem_alicota = porcentagem_alicota
        self.faixa_desconto = faixa_desconto
        