import random
from imovel import Imovel
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

    def comprar(self, imovel): #criação de função de compra calculado a partir e 20% do valor do imovel em comparação a poupança da familia
        for item in imovel:
            if item.valor * 0.2 <= self.poupanca:
                return f'Imóvel tipo {item.tipo} comprada no valor de R${item.valor}.'

        return 'Esta família não tem saldo suficiente na poupança para comprar nenhuma das opções de imóvel.'

    def __str__(self) -> str:
        estado_civil = ""
        if self.casado:
            estado_civil += "Casado"
        else:
            estado_civil += "Solteiro"

        return f'{estado_civil}\nFilhos: {self.filhos}\nRenda do Conjuge: R${self.rendaConjuge}\nPoupança: ' \
           f'{self.poupanca}\nDespesa Filhos: {self.despesaFilhos()}\nDespesa Moradia: {self.despesaMoradia()}\n' #remoção de repetições



