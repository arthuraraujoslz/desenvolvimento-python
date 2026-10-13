import csv
import re
from datetime import datetime


class FormatoInvalidoError(Exception):
    """Representa um dado que não atende ao formato esperado."""


def criar_arquivo_exemplo(caminho_arquivo):
    """Cria um arquivo CSV de exemplo quando ele não existe."""
    registros_exemplo = [
        [
            "nome",
            "email",
            "cpf",
            "telefone",
            "data_cadastro",
        ],
        [
            "Ana Souza",
            "ana.souza@email.com",
            "123.456.789-00",
            "(11) 99999-1111",
            "10/05/2026",
        ],
        [
            "Bruno Lima",
            "bruno.lima@email.com",
            "987.654.321-00",
            "(21) 98888-2222",
            "15/06/2026",
        ],
        [
            "Carla Silva",
            "carla.email.com",
            "111.222.333-44",
            "(31) 97777-3333",
            "20/07/2026",
        ],
        [
            "Diego Alves",
            "diego@exemplo.com",
            "11122233344",
            "(41) 96666-4444",
            "31/02/2026",
        ],
        [
            "Elisa Ramos",
            "elisa@exemplo.com",
            "555.666.777-88",
            "99999-5555",
            "01/08/2026",
        ],
        [
            "Felipe Costa",
            "felipe@exemplo.com",
            "999.888.777-66",
            "(51) 95555-6666",
            "2026-09-10",
        ],
    ]

    with open(caminho_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo, delimiter=";")
        escritor.writerows(registros_exemplo)


def validar_email(email):
    """Valida o formato de um e-mail usando expressão regular."""
    padrao_email = r"^\s*\w[\w.\-]*@\w[\w.\-]*\.\w{2,}\s*$"

    if not re.match(padrao_email, email):
        raise FormatoInvalidoError(f"E-mail inválido: {email}")


def validar_cpf(cpf):
    """Valida o formato 000.000.000-00 de um CPF."""
    padrao_cpf = r"^\s*\d{3}\.\d{3}\.\d{3}-\d{2}\s*$"

    if not re.match(padrao_cpf, cpf):
        raise FormatoInvalidoError(f"CPF inválido: {cpf}")


def validar_telefone(telefone):
    """Valida telefones no formato (00) 00000-0000 ou (00) 0000-0000."""
    padrao_telefone = r"^\s*\(\d{2}\)\s\d{4,5}-\d{4}\s*$"

    if not re.match(padrao_telefone, telefone):
        raise FormatoInvalidoError(f"Telefone inválido: {telefone}")


def validar_data(data):
    """Valida o formato DD/MM/AAAA e verifica se a data existe."""
    padrao_data = r"^\s*(0[1-9]|[12]\d|3[01])/(0[1-9]|1[0-2])/\d{4}\s*$"

    if not re.match(padrao_data, data):
        raise FormatoInvalidoError(f"Data com formato inválido: {data}")

    datetime.strptime(data.strip(), "%d/%m/%Y")


def validar_registro(registro):
    """Valida os campos obrigatórios e os formatos de um registro."""
    campos_obrigatorios = [
        "nome",
        "email",
        "cpf",
        "telefone",
        "data_cadastro",
    ]

    for campo in campos_obrigatorios:
        if campo not in registro:
            raise KeyError(f"Coluna obrigatória ausente: {campo}")

        if not registro[campo] or not registro[campo].strip():
            raise FormatoInvalidoError(
                f"Campo obrigatório vazio: {campo}"
            )

    validar_email(registro["email"])
    validar_cpf(registro["cpf"])
    validar_telefone(registro["telefone"])
    validar_data(registro["data_cadastro"])


def carregar_registros(caminho_arquivo):
    """Lê o arquivo CSV e cria um exemplo caso ele não seja encontrado."""
    linhas = []

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        print(
            f"Arquivo არ encontrado. Um arquivo de exemplo será criado."
        )
        criar_arquivo_exemplo(caminho_arquivo)

        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
    else:
        print(f"Arquivo encontrado e lido com sucesso.")
    finally:
        print(f"Processamento do arquivo '{caminho_arquivo}' concluído.")

    leitor = csv.DictReader(linhas, delimiter=";")
    return list(leitor)


def analisar_registros(registros):
    """Separa os registros válidos dos inválidos e registra os erros."""
    registros_validos = []
    registros_invalidos = []

    for numero_linha, registro in enumerate(registros, start=2):
        try:
            validar_registro(registro)
        except KeyError as erro:
            registros_invalidos.append(
                {
                    "linha": numero_linha,
                    "registro": registro,
                    "erro": f"Erro de coluna: {erro}",
                }
            )
        except ValueError as erro:
            registros_invalidos.append(
                {
                    "linha": numero_linha,
                    "registro": registro,
                    "erro": f"Erro de valor na data: {erro}",
                }
            )
        except FormatoInvalidoError as erro:
            registros_invalidos.append(
                {
                    "linha": numero_linha,
                    "registro": registro,
                    "erro": f"Erro de formato: {erro}",
                }
            )
        except Exception as erro:
            registros_invalidos.append(
                {
                    "linha": numero_linha,
                    "registro": registro,
                    "erro": f"Erro inesperado: {erro}",
                }
            )
        else:
            registros_validos.append(registro)
        finally:
            print(f"Registro da linha {numero_linha} analisado.")

    return registros_validos, registros_invalidos


def exibir_relatorio(registros, registros_validos, registros_invalidos):
    """Exibe o relatório final da análise dos dados."""
    total_registros = len(registros)
    quantidade_validos = len(registros_validos)
    quantidade_invalidos = len(registros_invalidos)

    if total_registros > 0:
        percentual_aprovacao = (quantidade_validos / total_registros) * 100
    else:
        percentual_aprovacao = 0.0

    print(f"\n{'=' * 65}")
    print(f"RELATÓRIO FINAL DE ANÁLISE DE DADOS")
    print(f"{'=' * 65}")
    print(f"Total de registros analisados: {total_registros}")
    print(f"Quantidade de registros válidos: {quantidade_validos}")
    print(f"Quantidade de registros inválidos: {quantidade_invalidos}")
    print(f"Percentual de aprovação: {percentual_aprovacao:.2f}%")
    print(f"{'=' * 65}")

    print(f"\nREGISTROS VÁLIDOS")
    if registros_validos:
        for registro in registros_validos:
            print(
                f"Nome: {registro['nome']} | "
                f"E-mail: {registro['email']} | "
                f"CPF: {registro['cpf']} | "
                f"Telefone: {registro['telefone']} | "
                f"Data: {registro['data_cadastro']}"
            )
    else:
        print(f"Nenhum registro válido foi encontrado.")

    print(f"\nREGISTROS INVÁLIDOS")
    if registros_invalidos:
        for registro_invalido in registros_invalidos:
            print(
                f"Linha: {registro_invalido['linha']} | "
                f"Motivo: {registro_invalido['erro']}"
            )
    else:
        print(f"Nenhum registro inválido foi encontrado.")

    print(f"{'=' * 65}")


def main():
    """Executa o sistema de análise de dados."""
    caminho_arquivo = "dados_clientes.csv"

    print(f"=== SISTEMA DE ANÁLISE DE DADOS ===")

    registros = carregar_registros(caminho_arquivo)
    registros_validos, registros_invalidos = analisar_registros(registros)

    exibir_relatorio(
        registros,
        registros_validos,
        registros_invalidos,
    )

    print(f"\nSistema finalizado com sucesso.")


if __name__ == "__main__":
    main()
