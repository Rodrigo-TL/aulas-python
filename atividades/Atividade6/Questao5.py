# Questão 5: Tabuada Simples

numero = int(input("Digite um número inteiro: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} x {contador} = {resultado}")
    contador += 1
