"""Sistema de Produtos - Entregável de Desenvolvimento em Python."""

"""
PORTUGOL - CADASTRO DE PRODUTOS COM VETORES FIXOS

algoritmo "Cadastro_de_Produtos"
var
    nomes: vetor[1..100] de caractere
    precos: vetor[1..100] de real
    categorias: vetor[1..100] de caractere
    quantidade_produtos, indice: inteiro
    continuar: caractere

inicio
    quantidade_produtos <- 0
    continuar <- "S"

    enquanto continuar = "S" faca
        quantidade_produtos <- quantidade_produtos + 1

        escreva("Nome do produto: ")
        leia(nomes[quantidade_produtos])

        escreva("Preco do produto: ")
        leia(precos[quantidade_produtos])

        escreva("Categoria do produto: ")
        leia(categorias[quantidade_produtos])

        escreva("Deseja cadastrar outro produto? (S/N): ")
        leia(continuar)
    fimenquanto

    para indice de 1 ate quantidade_produtos faca
        escreval(nomes[indice], " - ", precos[indice])
    fimpara
fimalgoritmo

Em Portugol, os vetores possuem um tamanho fixo de 100 posições.
Em Python, uma lista é dinâmica e o método append() adiciona novos
dicionários conforme os produtos são cadastrados.
"""


def ler_preco(mensagem):
    """Lê um valor de preço válido."""
    while True:
        try:
            preco = float(input(f"{mensagem}").replace(",", "."))

            if preco < 0:
                print(f"O preço não pode ser negativo.")
                continue

            return preco
        except ValueError:
            print(f"Valor inválido. Digite um número válido, como 10.50.")


def cadastrar_produtos():
    """Cadastra produtos em uma lista de dicionários."""
    produtos = []

    print(f"\n=== CADASTRO DE PRODUTOS ===")

    while True:
        nome = input(f"Nome do produto: ").strip()

        while not nome:
            print(f"O nome não pode ficar vazio.")
            nome = input(f"Nome do produto: ").strip()

        preco = ler_preco(f"Preço do produto: ")

        categoria = input(f"Categoria do produto: ").strip()

        while not categoria:
            print(f"A categoria não pode ficar vazia.")
            categoria = input(f"Categoria do produto: ").strip()

        produto = {
            "nome": nome,
            "preco": preco,
            "categoria": categoria,
        }

        produtos.append(produto)

        continuar = input(
            f"Deseja cadastrar outro produto? (S/N): "
        ).strip().upper()

        while continuar not in ("S", "N"):
            print(f"Opção inválida. Digite S ou N.")
            continuar = input(
                f"Deseja cadastrar outro produto? (S/N): "
            ).strip().upper()

        if continuar == "N":
            break

    return produtos


"""
PORTUGOL - FILTRAGEM DE PRODUTOS POR PREÇO

algoritmo "Filtrar_Produtos"
var
    nomes: vetor[1..100] de caractere
    precos: vetor[1..100] de real
    quantidade_produtos, indice: inteiro
    valor_referencia: real

inicio
    escreva("Informe um valor de referência: ")
    leia(valor_referencia)

    escreval("Produtos abaixo do valor informado:")

    para indice de 1 ate quantidade_produtos faca
        se precos[indice] < valor_referencia entao
            escreval(nomes[indice], " - R$ ", precos[indice])
        fimse
    fimpara

    escreval("Produtos acima do valor informado:")

    para indice de 1 ate quantidade_produtos faca
        se precos[indice] > valor_referencia entao
            escreval(nomes[indice], " - R$ ", precos[indice])
        fimse
    fimpara
fimalgoritmo

O laço para percorre as posições preenchidas dos vetores de tamanho fixo.
Em Python, o for percorre cada dicionário da lista de produtos.
"""


def filtrar_produtos_por_preco(produtos, valor_referencia):
    """Separa os produtos abaixo e acima do valor de referência."""
    produtos_abaixo = []
    produtos_acima = []

    for produto in produtos:
        if produto["preco"] < valor_referencia:
            produtos_abaixo.append(produto)
        elif produto["preco"] > valor_referencia:
            produtos_acima.append(produto)

    return produtos_abaixo, produtos_acima


"""
PORTUGOL - ORDENAÇÃO MANUAL COM BUBBLE SORT

algoritmo "Ordenar_Produtos"
var
    nomes: vetor[1..100] de caractere
    precos: vetor[1..100] de real
    categorias: vetor[1..100] de caractere
    quantidade_produtos, indice, proximo_indice: inteiro
    auxiliar_nome, auxiliar_categoria: caractere
    auxiliar_preco: real

inicio
    para indice de 1 ate quantidade_produtos - 1 faca
        para proximo_indice de 1 ate quantidade_produtos - indice faca
            se precos[proximo_indice] > precos[proximo_indice + 1] entao
                auxiliar_preco <- precos[proximo_indice]
                precos[proximo_indice] <- precos[proximo_indice + 1]
                precos[proximo_indice + 1] <- auxiliar_preco

                auxiliar_nome <- nomes[proximo_indice]
                nomes[proximo_indice] <- nomes[proximo_indice + 1]
                nomes[proximo_indice + 1] <- auxiliar_nome

                auxiliar_categoria <- categorias[proximo_indice]
                categorias[proximo_indice] <- categorias[proximo_indice + 1]
                categorias[proximo_indice + 1] <- auxiliar_categoria
            fimse
        fimpara
    fimpara
fimalgoritmo

O Bubble Sort compara elementos vizinhos e troca suas posições quando
necessário. Para ordenar de forma decrescente, a comparação deve usar
o operador menor que (<) em vez de maior que (>).

Em Python, sort() ordena a própria lista, enquanto sorted() cria uma
nova lista ordenada.
"""


def ordenar_produtos(produtos):
    """Organiza os produtos em ordem crescente e decrescente de preço."""
    produtos_crescentes = produtos.copy()
    produtos_crescentes.sort(key=lambda produto: produto["preco"])

    produtos_decrescentes = sorted(
        produtos,
        key=lambda produto: produto["preco"],
        reverse=True,
    )

    return produtos_crescentes, produtos_decrescentes


"""
PORTUGOL - SIMULAÇÃO MANUAL DE CATEGORIAS ÚNICAS

algoritmo "Categorias_Unicas"
var
    categorias: vetor[1..100] de caractere
    categorias_unicas: vetor[1..100] de caractere
    quantidade_produtos, quantidade_categorias: inteiro
    indice, comparador: inteiro
    categoria_repetida: logico

inicio
    quantidade_categorias <- 0

    para indice de 1 ate quantidade_produtos faca
        categoria_repetida <- falso

        para comparador de 1 ate quantidade_categorias faca
            se categorias[indice] = categorias_unicas[comparador] entao
                categoria_repetida <- verdadeiro
            fimse
        fimpara

        se categoria_repetida = falso entao
            quantidade_categorias <- quantidade_categorias + 1
            categorias_unicas[quantidade_categorias] <- categorias[indice]
        fimse
    fimpara

    escreval("Categorias únicas:")

    para indice de 1 ate quantidade_categorias faca
        escreval(categorias_unicas[indice])
    fimpara
fimalgoritmo

Como Portugol básico não possui sets, é necessário usar dois laços para:
1. Percorrer todas as categorias cadastradas.
2. Comparar a categoria atual com as categorias já armazenadas.
Assim, valores repetidos são ignorados manualmente.

Em Python, set() elimina automaticamente os valores repetidos.
"""


def obter_categorias_unicas(produtos):
    """Cria um conjunto com as categorias únicas cadastradas."""
    categorias_unicas = set()

    for produto in produtos:
        categorias_unicas.add(produto["categoria"])

    return categorias_unicas


"""
PORTUGOL - ESTATÍSTICAS DE PREÇOS

algoritmo "Estatisticas_de_Precos"
var
    precos: vetor[1..100] de real
    quantidade_produtos, indice: inteiro
    menor_preco, maior_preco, soma_precos, media_precos: real

inicio
    menor_preco <- precos[1]
    maior_preco <- precos[1]
    soma_precos <- 0

    para indice de 1 ate quantidade_produtos faca
        soma_precos <- soma_precos + precos[indice]

        se precos[indice] < menor_preco entao
            menor_preco <- precos[indice]
        fimse

        se precos[indice] > maior_preco entao
            maior_preco <- precos[indice]
        fimse
    fimpara

    media_precos <- soma_precos / quantidade_produtos

    escreval("Menor preço: ", menor_preco)
    escreval("Maior preço: ", maior_preco)
    escreval("Média dos preços: ", media_precos)
fimalgoritmo

No Portugol, um laço para percorre o vetor fixo e calcula manualmente
o menor valor, o maior valor e a soma dos preços.

Em Python, min(), max(), sum() e len() realizam esses cálculos.
A tupla criada possui exatamente três informações e é imutável.
"""


def calcular_estatisticas(produtos):
    """Cria uma tupla com menor preço, maior preço e média dos preços."""
    precos = []

    for produto in produtos:
        precos.append(produto["preco"])

    menor_preco = min(precos)
    maior_preco = max(precos)
    media_precos = sum(precos) / len(precos)

    estatisticas = (menor_preco, maior_preco, media_precos)

    return estatisticas


"""
PORTUGOL - RELATÓRIO FINAL FORMATADO

algoritmo "Relatorio_Final"
var
    indice: inteiro

inicio
    escreval("RELATÓRIO FINAL")

    escreval("Todos os produtos:")

    para indice de 1 ate quantidade_produtos faca
        escreval(
            nomes[indice],
            " | R$ ",
            precos[indice],
            " | ",
            categorias[indice]
        )
    fimpara

    escreval("Menor preço: ", menor_preco)
    escreval("Maior preço: ", maior_preco)
    escreval("Média de preços: ", media_precos)
fimalgoritmo

O relatório final utiliza laços para percorrer os vetores de tamanho
fixo e apresentar os dados. Em Python, o relatório utiliza listas,
conjuntos, tuplas e laços for para consolidar todas as informações.
"""


def exibir_produtos(titulo, produtos):
    """Exibe os produtos de uma lista com formatação."""
    print(f"\n{titulo}")

    if not produtos:
        print(f"Nenhum produto encontrado.")
        return

    for produto in produtos:
        print(
            f"Nome: {produto['nome']} | "
            f"Preço: R$ {produto['preco']:.2f} | "
            f"Categoria: {produto['categoria']}"
        )


def exibir_relatorio(produtos, valor_referencia):
    """Exibe todos os resultados do sistema em um relatório consolidado."""
    produtos_abaixo, produtos_acima = filtrar_produtos_por_preco(
        produtos,
        valor_referencia,
    )

    produtos_crescentes, produtos_decrescentes = ordenar_produtos(produtos)
    categorias_unicas = obter_categorias_unicas(produtos)
    estatisticas = calcular_estatisticas(produtos)

    menor_preco, maior_preco, media_precos = estatisticas

    print(f"\n{'=' * 65}")
    print(f"RELATÓRIO FINAL DO SISTEMA DE PRODUTOS")
    print(f"{'=' * 65}")
    print(f"Quantidade de produtos cadastrados: {len(produtos)}")
    print(f"Valor de referência: R$ {valor_referencia:.2f}")

    exibir_produtos(f"TODOS OS PRODUTOS", produtos)

    exibir_produtos(
        f"PRODUTOS ABAIXO DE R$ {valor_referencia:.2f}",
        produtos_abaixo,
    )

    exibir_produtos(
        f"PRODUTOS ACIMA DE R$ {valor_referencia:.2f}",
        produtos_acima,
    )

    exibir_produtos(
        f"PRODUTOS EM ORDEM CRESCENTE DE PREÇO",
        produtos_crescentes,
    )

    exibir_produtos(
        f"PRODUTOS EM ORDEM DECRESCENTE DE PREÇO",
        produtos_decrescentes,
    )

    print(f"\nCATEGORIAS ÚNICAS")
    for categoria in sorted(categorias_unicas):
        print(f"- {categoria}")

    print(f"\nTUPLA DE ESTATÍSTICAS")
    print(f"Menor preço: R$ {menor_preco:.2f}")
    print(f"Maior preço: R$ {maior_preco:.2f}")
    print(f"Média dos preços: R$ {media_precos:.2f}")
    print(f"Tupla completa: {estatisticas}")
    print(f"{'=' * 65}")


def main():
    """Executa o programa principal."""
    print(f"Bem-vindo ao Sistema de Produtos!")

    produtos = cadastrar_produtos()

    valor_referencia = ler_preco(
        f"\nInforme o valor de referência para a filtragem: "
    )

    exibir_relatorio(produtos, valor_referencia)

    print(f"\nSistema encerrado com sucesso.")


if __name__ == "__main__":
    main()
