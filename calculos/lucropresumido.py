from typing import Dict

class CalculoLucroPresumido():
    
    @classmethod
    def calcular_lucro_presumido(cls, side_tributacao_lucro_presumido: Dict[str, float]) -> float:
        imposto_lucro_presumido = float(side_tributacao_lucro_presumido["renda_bruta"] * side_tributacao_lucro_presumido["aliquota"])
        print(f"EU SOU O IMPOSTO LUCRO PRESUMIDO = {imposto_lucro_presumido}")
                     
        return round(imposto_lucro_presumido, 2)
