# CLASSE FILHA #
# arquivo.py classe

from Animal import Animal
from Categoria import Categoria


class Gato(Animal, Categoria):  # Herança múltipla
    def __init__(self, idade, nome, regiao, cadeia_alimentar):
        # Inicializa ambas as classes pai explicitamente
        Animal.__init__(self, idade=idade, tipo="Gato", regiao=regiao)
        Categoria.__init__(self, cadeiaAlimentar=cadeia_alimentar)

        self.nome = nome

    def cospe_pelo(self):
        print(f"O gato {self.nome} cospiu pelo...")

    def mostrar_idade_do_gato(self):
        print(self._tipo)
