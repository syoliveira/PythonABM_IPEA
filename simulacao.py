from familia import Familia
from imovel import Imovel
import exporter
import graficos

class Simulacao: #Criação da classe de simulação com a função run() para testes de repetições

    def run(repeticoes) -> object:
        lista_familias = []
        for x in range(repeticoes):
            familia = Familia()
            imoveis = [Imovel("A"), Imovel("B"), Imovel("C")]
            print("Nova Familia: \n")
            print(familia.__str__())
            print(imoveis[0].__str__())
            print(imoveis[1].__str__())
            print(imoveis[2].__str__())
            print(familia.comprar(imoveis), "\n")  # adição de chamada da função compra
            dados_familia = []
            if familia.casado:
                dados_familia.append("Casado")
            else:
                dados_familia.append("Solteiro")
            dados_familia.append(str(familia.filhos))
            dados_familia.append(str(round(familia.renda + familia.rendaConjuge, 2)))
            dados_familia.append(str(familia.poupanca))
            dados_familia.append(str(familia.despesaFilhos()))
            dados_familia.append(str(familia.despesaMoradia()))
            for i in range(3):  # adição de loop para substituir as repetições q eram possiveis de ser feitas com loop
                dados_familia.append(str(imoveis[i].valor))
                dados_familia.append(str(imoveis[i].aluguel))
            lista_familias.append(dados_familia)
        exporter.toCSV(lista_familias)
        lista_grafico = []
        lista_num_graf = []
        for i in range(len(lista_familias)):
            lista_grafico.append(float(lista_familias[i][2]))
            lista_num_graf.append("Família " + str(int(+i + 1)))
        graficos.generate(lista_num_graf, lista_grafico)

if __name__ == '__main__':
    Simulacao.run(100) #aqui pode ser incluido a quantidade de repeticoes que a simulacao ira fazer