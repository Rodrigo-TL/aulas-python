# ATIVIDADE PRÁTICA: OPERADORES, LÓGICA E SISTEMAS BÁSICOS

# Questão 1: A Divisão da Conta (Calculadora)

print("--- Questão 1 ---")
total_conta = float(input("Digite o valor total da conta (ex: 150.00): "))
qtd_pessoas = int(input("Digite a quantidade de pessoas na mesa: "))

valor_dividido = total_conta / qtd_pessoas

print(f"O valor total foi de R$ {total_conta:.2f}, e cada pessoa deve pagar R$ {valor_dividido:.2f}\n")


# Questão 2: A Fábrica de Caixas (Operador de Módulo)

print("--- Questão 2 ---")
total_macas = int(input("Digite a quantidade total de maçãs colhidas: "))

sobra_macas = total_macas % 12

print(f"Soberão {sobra_macas} maçãs fora das caixas.\n")


# Questão 3: A Catraca do Parque (Operadores de Comparação)

print("--- Questão 3 ---")
altura = float(input("Digite a altura da criança em metros (ex: 1.35): "))

pode_entrar = altura >= 1.40

print(f"Pode entrar na montanha-russa? {pode_entrar}\n")


# Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)

print("--- Questão 4 ---")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
frequencia = float(input("Digite a porcentagem de frequência (0 a 100): "))

media = (nota1 + nota2) / 2
aprovado = (media >= 6.0) and (frequencia >= 75)

print(f"Média calculada: {media:.1f}")
print(f"Aluno aprovado? {aprovado}\n")


# Questão 5: O Sistema de Desconto (Lógica OR)

print("--- Questão 5 ---")
valor_compra = float(input("Digite o valor total da compra: "))
eh_vip = int(input("Você possui cartão VIP? (Digite 1 para Sim ou 0 para Não): "))

# Converte o input numérico para um booleano (1 vira True, 0 vira False)
tem_cartao_vip = eh_vip == 1

frete_gratis = (valor_compra > 200.00) or tem_cartao_vip

print(f"Tem direito a frete grátis? {frete_gratis}\n")


# Questão 6: O Erro de Verificação (Análise e Correção de Código)

# Explicação Técnica:
# O erro acontece porque a função input() sempre captura e retorna os dados digitados
# pelo usuário no formato de texto (String/str). No código original, a variável
# 'senha_cadastrada' armazena um número inteiro (int), enquanto 'senha_digitada'
# armazena um texto (str). Em Python, o número inteiro 1234 é diferente do texto "1234",
# por isso a comparação com '==' resultava sempre em False.

# Código Corrigido:

print("--- Questão 6 ---")
senha_cadastrada = 1234
# Correção: Adicionado o casting int() para converter a entrada de texto em número inteiro
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado, "\n")


# Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

print("--- Questão 7 ---")
idade_doador = int(input("Digite a idade do doador: "))
peso_doador = float(input("Digite o peso do doador (em kg): "))

pode_doar = (idade_doador >= 16) and (idade_doador <= 69) and (peso_doador > 50)

print(f"O doador está apto a doar sangue? {pode_doar}\n")


# Questão 8: A Calculadora de Lucro da Empresa

print("--- Questão 8 ---")
nome_produto = input("Digite o nome do produto: ")
custo_fabrica = float(input("Digite o custo de fábrica do produto: "))
preco_venda = float(input("Digite o preço de venda na loja: "))

lucro = preco_venda - custo_fabrica
lucro_bom = lucro > 20.00

print(f"Produto: {nome_produto}")
print(f"Lucro obtido: R$ {lucro:.2f}")
print(f"O lucro foi bom? {lucro_bom}")
