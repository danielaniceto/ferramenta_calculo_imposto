from typing import Dict

class CalculoSimplesNacional():        
#Anexo 01 - Comercio
    @classmethod
    def calcular_simples_nacional(cls, side_tributacao: Dict[str, float]) -> float:
        imposto_simples_nacional = (float(side_tributacao["receita_bruta"] * side_tributacao["aliquota"]) - side_tributacao["desconto"])
        print(f"EU SOU O IMPOSTO ANEXO 01 = {imposto_simples_nacional}")
                     
        return round(imposto_simples_nacional, 2)
    