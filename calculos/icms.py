from typing import Dict

class CalculoIcms():

    @classmethod
    def calcular_icms(cls, side_tributacao_icms: Dict[str, float]) -> float:
        imposto_icms = (float(side_tributacao_icms["valor_do_produto"] / side_tributacao_icms["aliquota"]) * side_tributacao_icms["aliquota"])
        print(f"EU SOU O IMPOSTO ANEXO 01 = {imposto_icms}")
                     
        return round(imposto_icms, 2)
    