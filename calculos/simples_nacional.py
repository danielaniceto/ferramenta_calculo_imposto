from typing import Dict

class CalculoSimplesNacional():        
#Anexo 01 - Comercio
    @classmethod
    def calcular_simples_nacional(cls, side_tributacao: Dict[str, float]) -> float:

            imposto_anexo01 = (float(side_tributacao["receita_bruta"] * side_tributacao["aliquota"]) - side_tributacao["desconto"])
            print(f"EU SOU O IMPOSTO ANEXO 01 {imposto_anexo01}")
                
            return round(imposto_anexo01, 3)

#Anexo 02 - Industria
        
#Anexo 03 - Prestadores de Serviço (empresas que oferecem serviços de instalação, de reparos e de manutenção. Consideram-se neste anexo ainda, agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia, consideram-se neste anexo ainda agências de viagens, escritórios de contabilidade, academias, laboratórios, empresas de medicina e odontologia.)
        
#Anexo 04 - Prestadores de Serviço (Empresas de Limpeza, vigilancia, obras, construção de imóveis, serviços advocatícios)
        
#Anexo 05 - Prestadores de Serviço (empresas que fornecem serviço de auditoria, jornalismo, tecnologia, publicidade, engenharia, entre outros)