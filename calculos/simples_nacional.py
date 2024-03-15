import json
from app.models import *

class CalculoSimplesNacional:
#Anexo 01 - Comercio - Calculo para receitas abaixo de R$180.000,00
    def calcular_simples_nacional_menor_180k(self, imposto_simples_nacional_menor_180k: SimplesNacional):
        imposto_simples_nacional_menor_180k.receita_bruta
        imposto_simples_nacional_menor_180k.porcentagem_alicota
        imposto_simples_nacional_menor_180k.faixa_desconto

        if imposto_simples_nacional_menor_180k.receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")
            
        elif imposto_simples_nacional_menor_180k.receita_bruta > 0 and  imposto_simples_nacional_menor_180k.receita_bruta <= 180000:
            imposto_anexo01_menor_180k = (float(imposto_simples_nacional_menor_180k.receita_bruta * imposto_simples_nacional_menor_180k.porcentagem_alicota)) - imposto_simples_nacional_menor_180k.faixa_desconto
            
            return round(imposto_anexo01_menor_180k, 2)

#Anexo 02 - Industria
        
#Anexo 03 - Prestadores de Serviço (empresas que oferecem serviços de instalação, de reparos e de manutenção. Consideram-se neste anexo ainda, agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia, consideram-se neste anexo ainda agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia.)
        
#Anexo 04 - Prestadores de Serviço (Empresas de Limpeza, vigilancia, obras, construção de imóveis, serviços advocatícios)
        
#Anexo 05 - Prestadores de Serviço (empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros)