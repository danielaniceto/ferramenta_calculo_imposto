#from app.models import *
from typing import List, Dict

class CalculoSimplesNacional():

    TRIBUTACOES: List[Dict[str, int]] = [
        {"minimo": 0, "maximo": 180000, "aliquota": 0.04, "desconto": 0},
        {"minimo": 180001, "maximo": 360000, "aliquota": 0.073, "desconto": 5940},
        {"minimo": 360001, "maximo": 720000, "aliquota": 0.095, "desconto": 13860},
        {"minimo": 720001, "maximo": 1800000, "aliquota": 0.107, "desconto": 22500},
        {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.143, "desconto": 87300},
        {"minimo": 3600001, "maximo": 4800000, "aliquota": 0.19, "desconto": 378000}
    ]
        
#Anexo 01 - Comercio - Calculo para receitas abaixo de R$180.000,00
    @classmethod
    def calcular_simples_nacional_menor_180k(cls, receita_bruta: float) -> float:
        print(F"EU SOU A RECEITA DENTRO DE SIMPLES NACIONAL {receita_bruta}")
        porcentagem_aliquota = None
        faixa_desconto = None
        
        for tributacao in cls.TRIBUTACOES:
            if receita_bruta > tributacao["minimo"] and receita_bruta <= tributacao["maximo"]:
                    porcentagem_aliquota = tributacao["aliquota"]
                    faixa_desconto = tributacao["desconto"]

                    print(f"EU SOU A TRIBUTAÇÃO {tributacao}")
                    print(f"EU SOU A RECEITA BRUTA DENTRO DA FUNÇÃO {receita_bruta}")
                    print(f"EU SOU A PORCENTAGEM ALIQUOTA{porcentagem_aliquota}")
                    print(f"EU SOU A FAIXA DE DESCONTO {faixa_desconto}")

            elif receita_bruta < 0:
                raise Exception("Impossível Calcular Simples Nacional com receita negativa")
            
            elif receita_bruta not in range(tributacao["minimo"] and receita_bruta in tributacao["maximo"]):
                raise ValueError("O valor da receita fornecida, está fora do valor máximo de calculo segundo o anexo 01")

            elif receita_bruta > 0 and receita_bruta <= 180000:

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