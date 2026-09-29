# importam MÓDULOS
from Gato import Gato
from Cachorro import Cachorro
from CachorroDomestico import CachorroDomestico


class Main:  # PRINCIPAL -> Somente executa códigos
    print("INICIANDO CLASSE PRINCIPAL")

    # Instanciando o Gato
    gato1 = Gato(idade=2, nome="Tom", regiao="Brasil", cadeia_alimentar="Carnívoro")
    gato1.comer()
    gato1.dormir()
    gato1.mostrar_idade_do_gato()
    gato1.cospe_pelo()
    gato1.alimentando()

    # Instanciando o Cachorro (Corrigido de 'name' para 'nome')
    cachorro1 = Cachorro(idade=3, nome="Zeus", regiao="Brasil", cadeiaAlimentar="Carnívoro")
    cachorro1.comer()
    cachorro1.dormir()
    cachorro1.mostrarIdade()
    cachorro1.latir()
    cachorro1.aniversario()

    # Instanciando Cachorro Doméstico (Passando os dados que ele puxa da classe pai)
    cachorro_domestico = CachorroDomestico(idade=1, nome="Bob", regiao="Apartamento")
