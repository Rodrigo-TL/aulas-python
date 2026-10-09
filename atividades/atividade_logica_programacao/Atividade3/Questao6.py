# Questão 6: O Erro de Verificação (Análise e Correção de Código)

# Código Corrigido:

print("--- Questão 6 ---")
senha_cadastrada = 1234
# Correção: Adicionado o casting int() para converter a entrada de texto em número inteiro
senha_digitada = int(input("Digite sua senha: "))
acesso_liberado = senha_cadastrada == senha_digitada
print("Acesso liberado?", acesso_liberado, "\n")


# Explicação Técnica:
# O erro acontece porque a função input() sempre captura e retorna os dados digitados
# pelo usuário no formato de texto (String/str). No código original, a variável
# 'senha_cadastrada' armazena um número inteiro (int), enquanto 'senha_digitada'
# armazena um texto (str). Em Python, o número inteiro 1234 é diferente do texto "1234",
# por isso a comparação com '==' resultava sempre em False.