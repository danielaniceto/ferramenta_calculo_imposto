from typing import Dict

class CalculoLucroReal():
    
    @classmethod
    def calcular_lucro_real(cls, side_tributacao_lucro_real: Dict[str, float]) -> float:
        
        if side_tributacao_lucro_real["periodo"] == "Trimestral":
            if side_tributacao_lucro_real["lucro_real"] / 3 > 60000:
               valor_exedente = side_tributacao_lucro_real["lucro_real"] - 60000
               imposto_lucro_real_irpj = (side_tributacao_lucro_real["lucro_real"] * 0.15) + valor_exedente * 0.1

               imposto_lucro_real_csll = side_tributacao_lucro_real["lucro_real"] * side_tributacao_lucro_real["aliquota"]

               imposto_lucro_real_total = imposto_lucro_real_irpj + imposto_lucro_real_csll

               return round(imposto_lucro_real_total, 2)

            else:
                imposto_lucro_real_irpj = side_tributacao_lucro_real["lucro_real"] * 0.15

                imposto_lucro_real_csll = side_tributacao_lucro_real["lucro_real"] * side_tributacao_lucro_real["aliquota"]

                imposto_lucro_real_total = imposto_lucro_real_irpj + imposto_lucro_real_csll

                return imposto_lucro_real_total
            
        elif side_tributacao_lucro_real["periodo"] == "Anual":
            if side_tributacao_lucro_real["lucro_real"] / 12 > 240000:
               valor_exedente = side_tributacao_lucro_real["lucro_real"] - 240000
               imposto_lucro_real_irpj = (side_tributacao_lucro_real["lucro_real"] * 0.15) + valor_exedente * 0.1

               imposto_lucro_real_csll = side_tributacao_lucro_real["lucro_real"] * side_tributacao_lucro_real["aliquota"]

               imposto_lucro_real_total = imposto_lucro_real_irpj + imposto_lucro_real_csll

               return round(imposto_lucro_real_total, 2)
            
            else:
                imposto_lucro_real_irpj = side_tributacao_lucro_real["lucro_real"] * 0.15

                imposto_lucro_real_csll = side_tributacao_lucro_real["lucro_real"] * side_tributacao_lucro_real["aliquota"]

                imposto_lucro_real_total = imposto_lucro_real_irpj + imposto_lucro_real_csll

                return round(imposto_lucro_real_total, 2)
               
        print(f"EU SOU O IMPOSTO LUCRO PRESUMIDO = {imposto_lucro_real_total}")
