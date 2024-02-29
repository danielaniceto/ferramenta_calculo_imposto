import json

class SimplesNacional:
    def __init__(self, cliente):
        self.cliente = cliente
        
    #Anexo 01 - Comercio
    def calcular_simples_nacional(self, receita_bruta, porcentagem_alicota, faixa_desconto):
        self.receita_bruta = receita_bruta
        self.porcentagem_alicota = porcentagem_alicota
        self.faixa_Desconto = faixa_desconto

        if receita_bruta <= 0:
            raise Exception("Impossível Calcular Simples Nacional com receita negativa")
        
        elif receita_bruta < 180000:
            imposto_anexo01 = receita_bruta * 0.04
            return imposto_anexo01

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__,
        sort_keys=True, indent=4)
