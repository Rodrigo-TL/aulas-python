import json
from pathlib import Path

import requests


ARQUIVO_HISTORICO = Path(__file__).with_name("historico_pesquisa.json")
URL_VIACEP = "https://viacep.com.br/ws/{cep}/json/"


def consultar_cep(cep):
    cep = cep.strip().replace("-", "")

    if not cep.isdigit() or len(cep) != 8:
        raise ValueError("O CEP deve conter exatamente 8 números.")

    resposta = requests.get(URL_VIACEP.format(cep=cep), timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()

    if dados.get("erro"):
        raise ValueError("CEP não encontrado.")

    return dados


def carregar_historico():
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as arquivo:
            historico = json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as erro:
        raise ValueError("O arquivo de histórico contém um JSON inválido.") from erro

    if not isinstance(historico, list):
        raise ValueError("O histórico deve ser uma lista de pesquisas.")

    return historico


def salvar_pesquisa(dados):
    historico = carregar_historico()
    historico.append(dados)

    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as arquivo:
        json.dump(historico, arquivo, indent=4, ensure_ascii=False)


def exibir_endereco(dados):
    print(f"Logradouro: {dados.get('logradouro', 'Não informado')}")
    print(f"Bairro: {dados.get('bairro', 'Não informado')}")
    print(f"Cidade: {dados.get('localidade', 'Não informado')}")
    print(f"Estado: {dados.get('uf', 'Não informado')}")


def main():
    cep = input("Digite o CEP para consulta: ")

    try:
        dados = consultar_cep(cep)
        exibir_endereco(dados)
        salvar_pesquisa(dados)
        print(f"Pesquisa salva em: {ARQUIVO_HISTORICO.name}")
    except requests.RequestException as erro:
        print(f"Falha na conexão com a API ViaCEP: {erro}")
    except (ValueError, OSError) as erro:
        print(f"Não foi possível concluir a pesquisa: {erro}")


if __name__ == "__main__":
    main()
