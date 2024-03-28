from app.models import SimplesNacional
from typing import List, Dict
from api import is_CalculoImpostoSimplesNacionalAnexo01

class CalculoSimplesNacional():        
#Anexo 01 - Comercio
    @classmethod
    def calcular_simples_nacional(cls, calulo_valor_simples_nacional: Dict[str, float]) -> float:

            imposto_anexo01 = (float(calulo_valor_simples_nacional["receita_bruta"] * calulo_valor_simples_nacional["aliquota"]) - calulo_valor_simples_nacional["desconto"])
            print(f"EU SOU O IMPOSTO ANEXO 01 {imposto_anexo01}")
                
            return round(imposto_anexo01, 2)

#Anexo 02 - Industria
        
#Anexo 03 - Prestadores de Serviço (empresas que oferecem serviços de instalação, de reparos e de manutenção. Consideram-se neste anexo ainda, agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia, consideram-se neste anexo ainda agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia.)
        
#Anexo 04 - Prestadores de Serviço (Empresas de Limpeza, vigilancia, obras, construção de imóveis, serviços advocatícios)
        
#Anexo 05 - Prestadores de Serviço (empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros)