from typing import Dict

class CalculoLucroReal():
    
    @classmethod
    def calcular_lucro_real(cls, side_tributacao_lucro_real: Dict[str, float]) -> float:
        imposto_lucro_real = float(side_tributacao_lucro_real["renda_bruta"] * side_tributacao_lucro_real["aliquota"])
        print(f"EU SOU O IMPOSTO LUCRO PRESUMIDO = {imposto_lucro_real}")
                     
        return round(imposto_lucro_real, 2)
