#from app.models import *
from typing import List, Dict
from app.models import SimplesNacional

class CalculoSimplesNacional():        
#Anexo 01 - Comercio - Calculo para receitas abaixo de R$180.000,00
    @classmethod
    def calcular_simples_nacional_menor_180k(cls, receita_bruta: float, porcentagem_aliquota:float=None, faixa_desconto:float=None) -> float:
        print(F"EU SOU A RECEITA DENTRO DE SIMPLES NACIONAL {receita_bruta}")

        print(f"EU SOU A RECEITA BRUTA DENTRO DA FUNÇÃO {receita_bruta}")

        if receita_bruta < 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")
            
        elif receita_bruta < tributacao["minimo"] or receita_bruta > tributacao["maximo"]:
            raise ValueError("O valor da receita fornecida, está fora do valor máximo de calculo segundo o anexo 01")

        else:
            imposto_anexo01_menor_180 = (float(receita_bruta * porcentagem_aliquota)) - faixa_desconto
            print(f" EU SOU O IMPOSTO ANEXO 01 {imposto_anexo01_menor_180}")
                
            return round(imposto_anexo01_menor_180, 2)
        
#Anexo 01 - Comercio - Calculo para receitas entre R$180.000,00 a R$360.000,00

#Anexo 01 - Comercio - Calculo para receitas entre R$360.000,00 a R$ 720.000,00

#Anexo 01 - Comercio - Calculo para receitas entre R$ 720.000,00 a R$ 1.800.000,00

#Anexo 01 - Comercio - Calculo para receitas entre R$1.800.000,00 a R$ 3.600.000,00

#Anexo 01 - Comercio - Calculo para receitas entre R$3.600.000,00 a R$ 4.800.000,00



#Anexo 02 - Industria
        
#Anexo 03 - Prestadores de Serviço (empresas que oferecem serviços de instalação, de reparos e de manutenção. Consideram-se neste anexo ainda, agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia, consideram-se neste anexo ainda agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia.)
        
#Anexo 04 - Prestadores de Serviço (Empresas de Limpeza, vigilancia, obras, construção de imóveis, serviços advocatícios)
        
#Anexo 05 - Prestadores de Serviço (empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros)