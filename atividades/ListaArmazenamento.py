# crie uma lista que ela armazene um numero x de funcionarios. Usando o while, adicione quantos funcionarios quiser em execução.

# Com o for, voce irá imprimir duas listas:

# uma lista com todos os funcionarios que receber]ao um aumento.

# Outra lista, com todos os funcionarios que serão demitidos.

# Voce irá decidir qual funcionario será dmitido ou receberá aumento pelo index do funcionario lista[]

# Questão 1: Lista de Funcionários

funcionarios = []
funcionario = input("Digite o nome do funcionário (Enter para encerrar): ").strip()

while funcionario != "":
    funcionarios.append(funcionario)
    funcionario = input("Digite o nome do funcionário (Enter para encerrar): ").strip()

# Os funcionários nos índices 0 e 2 receberão aumento.
indices_aumento = [0, 2]
funcionarios_aumento = []
funcionarios_demissao = []

for indice in range(len(funcionarios)):
    if indice in indices_aumento:
        funcionarios_aumento.append(funcionarios[indice])
    else:
        funcionarios_demissao.append(funcionarios[indice])

print("\nFuncionários que receberão aumento:")
for funcionario in funcionarios_aumento:
    print(funcionario)

print("\nFuncionários que serão demitidos:")
for funcionario in funcionarios_demissao:
    print(funcionario)
