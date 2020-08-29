import random
class Imovel:
    def __init__(self,tipo) -> None:
        self.tipo = tipo
        if tipo == "A":
            self.esgoto = True
            self.escola = ["particular","estadual","municipal"]
            self.transporte = "total"
            self.valor = round(random.uniform(700000,1400000),2) #imovel de classe media alta
        if tipo == "B":
            self.esgoto = True
            self.escola = ["estadual","municipal"]
            self.transporte = "parcial"
            self.valor = round(random.uniform(200000, 600000), 2) #imovel classe media
        if tipo == "C": # o codigo considera que todo imovel tem agua
            self.esgoto = False
            self.escola = ["municipal"]
            self.transporte = "nenhum"
            self.valor = round(random.uniform(30000, 100000), 2)
        self.aluguel = round(self.valor * random.uniform(0.03, 0.08), 2) #imovel classe C

    def __str__(self) -> str:
        string = ""
        if self.esgoto:
            string += "Esgoto: Sim\n"
        else:
            string += "Esgoto: Não\n"
        string+="Opções de Escola: "
        for item in self.escola:
            string+=f"{item}, "
        string+=f"\nTransporte: {self.transporte}\nValor de Compra: {self.valor}\nValor de Aluguel: {self.aluguel}\n" #pequena remoção de repetições
        return string
# A localizacao do imovel considera, que todas as localidades tem agua.
