# Questão 4: O Boletim Escolar Automático (Aritmética + Lógica AND)

print("--- Questão 4 ---")
nota1 = float(input("Digite a Nota 1: "))
nota2 = float(input("Digite a Nota 2: "))
frequencia = float(input("Digite a porcentagem de frequência (0 a 100): "))

media = (nota1 + nota2) / 2
aprovado = (media >= 6.0) and (frequencia >= 75)

print(f"Média calculada: {media:.1f}")
print(f"Aluno aprovado? {aprovado}\n")