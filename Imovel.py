import random
class Imovel:
    def __init__(self,tipo) -> None:
        if tipo == "A":
            self.esgoto = True
            self.escola = ["particular","estadual","municipal"]
            self.transporte = "total"
            self.valor = round(random.uniform(700000,1400000),2)
        if tipo == "B":
            self.esgoto = True
            self.escola = ["estadual","municipal"]
            self.transporte = "parcial"
            self.valor = round(random.uniform(200000, 600000), 2)
        if tipo == "C":
            self.esgoto = False
            self.escola = ["municipal"]
            self.transporte = "nenhum"
            self.valor = round(random.uniform(30000, 100000), 2)
        self.aluguel = round(self.valor * random.uniform(0.03, 0.08), 2)

    def __str__(self) -> str:
        string = ""
        if self.esgoto:
            string += "Esgoto: Sim\n"
        else:
            string += "Esgoto: Não\n"
        string+="Opções de Escola: "
        for item in self.escola:
            string+=f"{item}, "
        string+=f"\nTransporte: {self.transporte}\n"
        string += f"Valor de Compra: {self.valor}\n"
        string += f"Valor de Aluguel: {self.aluguel}\n"
        return string


