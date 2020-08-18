from Familia import Familia
from Imovel import Imovel
import Exporter
import Graficos

print("Famila BeTa")
familias = int(input("Quantas familias você deseja gerar ? "))
lista_familias = []
for x in range(familias):
    familia = Familia()
    imovelA = Imovel("A")
    imovelB = Imovel("B")
    imovelC = Imovel("C")
    print("Nova Familia: \n")
    print(familia.__str__())
    print(imovelA.__str__())
    print(imovelB.__str__())
    print(imovelC.__str__())
    dados_familia = []
    if familia.casado:
        dados_familia.append("Casado")
    else:
        dados_familia.append("Solteiro")
    dados_familia.append(str(familia.filhos))
    dados_familia.append(str(round(familia.renda+familia.rendaConjuge,2)))
    dados_familia.append(str(familia.poupanca))
    dados_familia.append(str(familia.despesaFilhos()))
    dados_familia.append(str(familia.despesaMoradia()))
    dados_familia.append(str(imovelA.valor))
    dados_familia.append(str(imovelA.aluguel))
    dados_familia.append(str(imovelB.valor))
    dados_familia.append(str(imovelB.aluguel))
    dados_familia.append(str(imovelC.valor))
    dados_familia.append(str(imovelC.aluguel))
    lista_familias.append(dados_familia)
Exporter.toCSV(lista_familias)
lista_grafico=[]
lista_num_graf = []
for i in range(len(lista_familias)):
    lista_grafico.append(float(lista_familias[i][2]))
    lista_num_graf.append("Família "+str(int(+i+1)))
Graficos.generate(lista_num_graf,lista_grafico)
