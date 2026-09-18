class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade_estoque = quantidade_estoque

    def adicionar_estoque(self, quantidade):
        if quantidade <= 0:
            print("Erro: Quantidade inválida")
            return

        self.__quantidade_estoque += quantidade

    def realizar_venda(self, quantidade):
        if quantidade <= 0:
            print("Venda negada: Quantidade inválida")
            return

        if quantidade > self.__quantidade_estoque:
            print("Venda negada: Estoque insuficiente")
            return

        self.__quantidade_estoque -= quantidade

    def aplicar_desconto(self, percentual):
        if percentual <= 0 or percentual > 80:
            print("Erro: Desconto inválido")
            return

        self.__preco *= 1 - percentual / 100

    def exibir_resumo(self):
        print(f"Produto: {self.__nome}")
        print(f"Preço: R$ {self.__preco:.2f}")
        print(f"Quantidade em estoque: {self.__quantidade_estoque}")


if __name__ == "__main__":
    meu_produto = Produto("Notebook", 3500.00, 10)

    # Atribuições externas criam atributos diferentes dos privados originais.
    meu_produto.__quantidade_estoque = -50
    meu_produto.__preco = -100

    meu_produto.realizar_venda(9999)
    meu_produto.exibir_resumo()
