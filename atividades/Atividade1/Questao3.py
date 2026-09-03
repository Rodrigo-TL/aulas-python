#QUESTÃO 3: O Problema da Concatenação

#Explicação: Tudo que entra no 'input()' vira texto
#(String). Quando usamos o sinal de '+' com textos,
#o Python junta eles em vez de somar. Por isso que
#"10" + "10" virou "1010". Para resolver, temos que
#avisar que é um número usando float() ou int().

#Código corrigido:

n1 = float(input("Primeiro número: "))
n2 = float(input("Segundo número: "))
resultado = n1 + n2
print("O resultado da soma é:", resultado)