import uuid
import json

class Cliente:
  def __init__(self, id, nome_empresa, cnpj):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj

class SimplesNacional:
    def __init__(self, receita_bruta):
        self.receita_bruta = float(receita_bruta)
        