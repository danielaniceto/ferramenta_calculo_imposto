import uuid
import json

class Cliente:
  def __init__(self, nome_empresa, cnpj):
    self.id = str(uuid.uuid4())
    self.nome_empresa = nome_empresa
    self.documento = cnpj

  def __str__(self):
    return json.dumps(self, default=lambda o: o.__dict__,
      sort_keys=True, indent=4)