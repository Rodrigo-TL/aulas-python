# CLASSE FILHA #
# Cachorro.py

from Animal import Animal


class Cachorro(Animal):
    def __init__(self, idade, nome, regiao, cadeiaAlimentar=None):
        # Inicializa a classe pai Animal
        super().__init__(idade=idade, tipo="Cachorro", regiao=regiao)
        self.nome = nome

    def latir(self):
        print(f"O {self.nome} está latindo...")

    def aniversario(self):
        self.idade += 1
        print(f"O cachorro completou {self.idade} anos de idade!")
