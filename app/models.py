import uuid
from calculos.simples_nacional import CalculoSimplesNacional
#from typing import List, Dict

class EmpresaCliente:
  def __init__(self, id, nome_empresa, cnpj, renda_bruta):
    self.id = id(str(uuid.uuid4()))
    self.nome_empresa = nome_empresa
    self.documento = cnpj
    self.renda_bruta = renda_bruta
