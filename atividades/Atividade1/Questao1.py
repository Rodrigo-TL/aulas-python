#QUESTÃO 1: A Ordem da Execução

#Explicação: O Python lê o código de cima para baixo.

#Na linha 1, o 'print' tenta mostrar o 'nome', mas
#o computador ainda não sabe o que é isso, porque
#a variável só é criada na linha de baixo pelo 'input'.
#Isso dá o erro NameError.

#Código corrigido:

nome = input("Digite seu nome: ")
print("Bem-vindo(a),", nome)