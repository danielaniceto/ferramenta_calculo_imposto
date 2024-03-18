from app.models import *

tributacoes = [
    {"minimo": 0, "maximo": 180000, "aliquota": 0.04, "faixa_desconto": 0},
    {"minimo": 180001, "maximo": 360000, "aliquota": 0.073, "faixa_desconto": 5940},
    {"minimo": 360001, "maximo": 720000, "aliquota": 0.095, "faixa_desconto": 13860},
    {"minimo": 720001, "maximo": 1800000, "aliquota": 0.107, "faixa_desconto": 22500},
    {"minimo": 1800001, "maximo": 3600000, "aliquota": 0.143, "faixa_desconto": 87300},
    {"minimo": 3600001, "maximo": 4800000, "aliquota": 0.19, "faixa_desconto": 378000}
]

class CalculoSimplesNacional:
#Anexo 01 - Comercio - Calculo para receitas abaixo de R$180.000,00
    def calcular_simples_nacional_menor_180k(self, imposto_simples_nacional_menor_180: SimplesNacional):
        imposto_simples_nacional_menor_180.receita_bruta
        imposto_simples_nacional_menor_180.porcentagem_aliquota
        imposto_simples_nacional_menor_180.faixa_desconto

        if imposto_simples_nacional_menor_180.receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")

        elif imposto_simples_nacional_menor_180.receita_bruta > 0 and  imposto_simples_nacional_menor_180.receita_bruta <= 180000:
            imposto_anexo01_menor_180 = (float(imposto_simples_nacional_menor_180.receita_bruta * imposto_simples_nacional_menor_180.porcentagem_aliquota)) - imposto_simples_nacional_menor_180.faixa_desconto
            
            return round(imposto_anexo01_menor_180, 2)
        
#Anexo 01 - Comercio - Calculo para receitas entre R$180.000,00 a R$360.000,00      
    def calcular_simples_nacional_entre_180_a_360(self, imposto_simples_nacional_180_a_360: SimplesNacional):
        if imposto_simples_nacional_180_a_360.receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")

        elif imposto_simples_nacional_180_a_360.receita_bruta <180000:
            return

        elif imposto_simples_nacional_180_a_360.receita_bruta >= 180000:
            imposto_anexo01_entre_180_e_360 = (float(imposto_simples_nacional_180_a_360.receita_bruta * imposto_simples_nacional_180_a_360.porcentagem_aliquota)) - imposto_simples_nacional_180_a_360.faixa_desconto
            
            return round(imposto_anexo01_entre_180_e_360, 2)
        

#Anexo 02 - Industria
        
#Anexo 03 - Prestadores de Serviço (empresas que oferecem serviços de instalação, de reparos e de manutenção. Consideram-se neste anexo ainda, agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia, consideram-se neste anexo ainda agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia.)
        
#Anexo 04 - Prestadores de Serviço (Empresas de Limpeza, vigilancia, obras, construção de imóveis, serviços advocatícios)
        
#Anexo 05 - Prestadores de Serviço (empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros)