import random
class Familia:
    def __init__(self):
        self.renda = round(random.uniform(1045,39200),2)
        self.poupanca = round(random.uniform(0,250000),2)
        self.casado = bool(random.getrandbits(1))
        self.rendaConjuge = 0
        if self.casado:
            self.rendaConjuge = round(random.uniform(0, 39200), 2)
        self.filhos = random.randint(0,3)

    def despesaMoradia(self):
        return round(((self.rendaConjuge+self.renda)/100)*30, 2)

    def despesaFilhos(self):
        return round(((self.rendaConjuge+self.renda)/100)*self.filhos*10, 2)

    def __str__(self) -> str:
        string = ""
        if self.casado:
            string += "Casado\n"
        else:
            string += "Solteiro\n"
        string += f"Filhos: {self.filhos}\n"
        string += f"Renda: R${self.renda}\n"
        string += f"Renda do Conjuge: R${self.rendaConjuge}\n"
        string += f"Poupança: {self.poupanca}\n"
        string += f"Despesa Filhos: {self.despesaFilhos()}\n"
        string += f"Despesa Moradia: {self.despesaMoradia()}\n"

        return string



