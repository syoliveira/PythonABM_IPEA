import csv
def toCSV(data_list):
    with open('Familias.csv', 'w',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Estado Civil', 'Filhos', 'Renda Total', 'Poupança', 'Despesa Filhos', 'Despesa Moradia', 'Valor Moradia 1','Aluguel Moradia 1','Valor Moradia 2','Aluguel Moradia 2','Valor Moradia 3','Aluguel Moradia 3'])
        lista = []
        for item in data_list:
            lista.append(item)
        writer.writerows(lista)