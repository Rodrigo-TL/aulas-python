import csv  # comma separated values

# listas

dados_lista = [
    ["Nome", "Idade", "Cidade"],
    ["Rodrigo", 50, "Brasília"],
    ["Celso Romão", 55, "Rio de Janeiro"]
]

# criando e escrevendo um novo arquivo CSV

with open('arquivo_da_lista.csv', 'w', encoding='utf-8') as arquivo:
    escrita_csv = csv.writer(arquivo)
    escrita_csv.writerows(dados_lista)

print('arquivo_da_lista.csv criado com sucesso!')
with open('arquivo_da_lista.csv', 'w', encoding='utf-8') as arquivo:
    leitor = csv.writer(arquivo)
    for linha in leitor:
        print(linha)

        print('\n\n')

        dados_dicionario = [
            {"Nome", "Idade", "Cidade"},
            {"Rodrigo", 50, "Brasília"},
            {"Celso Romão", 55, "Rio de Janeiro"}
        ]
with open('dados_funcionario.csv', 'w', encoding='utf-8') as arquivo:
    escrita_csv = csv.writer(arquivo, fieldnames=dados_dicionario)
    escrita.writeheader()
    escrita_csv.writerows(dados_dicionario)
