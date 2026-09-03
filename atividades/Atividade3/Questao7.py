# Questão 7: O Formulário de Doação de Sangue (Múltiplas Condições)

print("--- Questão 7 ---")

idade_doador = int(input("Digite a idade do doador: "))
peso_doador = float(input("Digite o peso do doador (em kg): "))

pode_doar = (idade_doador >= 16) and (idade_doador <= 69) and (peso_doador > 50)

print(f"O doador está apto a doar sangue? {pode_doar}\n")
