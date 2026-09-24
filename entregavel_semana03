"""Soluções modularizadas dos desafios da Semana 03."""

from collections import Counter


def somar(primeiro_numero, segundo_numero):
    """Retorna a soma de dois números."""
    return primeiro_numero + segundo_numero


def subtrair(primeiro_numero, segundo_numero):
    """Retorna a subtração entre dois números."""
    return primeiro_numero - segundo_numero


def multiplicar(primeiro_numero, segundo_numero):
    """Retorna a multiplicação entre dois números."""
    return primeiro_numero * segundo_numero


def dividir(dividendo, divisor):
    """Retorna a divisão de dois números ou None quando o divisor é zero."""
    if divisor == 0:
        return None

    return dividendo / divisor


def celsius_para_fahrenheit(temperatura_celsius):
    """Converte uma temperatura em Celsius para Fahrenheit."""
    return (temperatura_celsius * 9 / 5) + 32


def validar_senha(senha):
    """Valida se a senha tem oito caracteres, letra e número."""
    possui_tamanho_minimo = len(senha) >= 8
    possui_letra = any(caractere.isalpha() for caractere in senha)
    possui_numero = any(caractere.isdigit() for caractere in senha)

    return possui_tamanho_minimo and possui_letra and possui_numero


def calcular_caixa(*precos):
    """Retorna o total dos preços recebidos como argumentos posicionais."""
    return sum(precos)


def criar_ficha_aluno(**dados):
    """Monta uma ficha textual do aluno a partir de dados nomeados."""
    nome = dados.get("nome", "Não informado")
    idade = dados.get("idade", "Não informada")
    curso = dados.get("curso", "Não informado")

    return f"Nome: {nome} | Idade: {idade} | Curso: {curso}"


def adicionar_item_seguro(lista_original, item):
    """Adiciona um item em uma cópia da lista sem alterar a lista original."""
    nova_lista = lista_original.copy()
    nova_lista.append(item)

    return nova_lista


def calcular_estatisticas(numeros):
    """Retorna média, mediana e moda de uma cópia da lista de números."""
    if not numeros:
        return None

    numeros_seguros = numeros.copy()
    numeros_ordenados = sorted(numeros_seguros)
    quantidade = len(numeros_ordenados)
    media = sum(numeros_ordenados) / quantidade
    indice_central = quantidade // 2

    if quantidade % 2 == 0:
        mediana = (
            numeros_ordenados[indice_central - 1]
            + numeros_ordenados[indice_central]
        ) / 2
    else:
        mediana = numeros_ordenados[indice_central]

    frequencias = Counter(numeros_ordenados)
    maior_frequencia = max(frequencias.values())
    modas = [
        numero
        for numero, frequencia in frequencias.items()
        if frequencia == maior_frequencia
    ]

    return {
        "media": media,
        "mediana": mediana,
        "moda": modas,
    }


def calcular_fatorial(numero):
    """Calcula recursivamente o fatorial de um inteiro não negativo."""
    if numero < 0:
        return None
    if numero in (0, 1):
        return 1

    return numero * calcular_fatorial(numero - 1)


def relatorio(titulo, *linhas, **config):
    """Monta um relatório textual configurável a partir de várias linhas."""
    separador = config.get("separador", "-")
    largura = int(config.get("largura", 40))
    exibir_rodape = config.get("exibir_rodape", True)
    linha_separadora = separador * largura
    conteudo = "\n".join(f"- {linha}" for linha in linhas)
    relatorio = f"{linha_separadora}\n{titulo}\n{linha_separadora}\n{conteudo}"

    if exibir_rodape:
        relatorio = f"{relatorio}\n{linha_separadora}"

    return relatorio


# Versão comentada em Portugol/Portugal:
# funcao dividir(dividendo, divisor)
#     se divisor = 0 entao
#         devolve nulo
#     fim se
#     devolve dividendo / divisor
# fim funcao
#
# funcao adicionar_item_seguro(lista_original, item)
#     nova_lista <- copiar(lista_original)
#     adicionar nova_lista, item
#     devolve nova_lista
# fim funcao
#
# enquanto tentativas < limite faca
#     ler senha
#     validar senha
# fim enquanto


def main():
    """Demonstra o funcionamento de todas as funções do arquivo."""
    primeiro_numero = 10
    segundo_numero = 5
    resultado_divisao = dividir(primeiro_numero, segundo_numero)
    divisao_por_zero = dividir(primeiro_numero, 0)

    print(f"{'=' * 50}")
    print(f"CALCULADORA")
    print(f"{'=' * 50}")
    print(f"Soma: {somar(primeiro_numero, segundo_numero)}")
    print(f"Subtração: {subtrair(primeiro_numero, segundo_numero)}")
    print(f"Multiplicação: {multiplicar(primeiro_numero, segundo_numero)}")
    print(f"Divisão: {resultado_divisao}")

    if divisao_por_zero is None:
        print(f"Divisão por zero: operação não permitida.")

    temperatura_fahrenheit = celsius_para_fahrenheit(25.0)
    senha_valida = validar_senha("Python123")
    total_caixa = calcular_caixa(19.90, 25.50, 10.00)
    ficha = criar_ficha_aluno(nome="Ana", idade=20, curso="Python")

    print(f"\n{'=' * 50}")
    print(f"UTILIDADES")
    print(f"{'=' * 50}")
    print(f"25.0 °C equivalem a {temperatura_fahrenheit:.1f} °F")
    print(f"Senha válida: {senha_valida}")
    print(f"Total do caixa: R$ {total_caixa:.2f}")
    print(f"Ficha do aluno: {ficha}")

    lista_original = ["caderno", "caneta"]
    lista_com_item = adicionar_item_seguro(lista_original, "livro")

    print(f"\n{'=' * 50}")
    print(f"LISTA SEGURA")
    print(f"{'=' * 50}")
    print(f"Lista original: {lista_original}")
    print(f"Nova lista: {lista_com_item}")

    estatisticas = calcular_estatisticas([2, 4, 4, 6, 8])
    fatorial = calcular_fatorial(5)
    relatorio_semanal = relatorio(
        "RELATÓRIO SEMANAL",
        "Calculadora testada",
        "Lista original preservada",
        separador="=",
        largura=35,
    )

    print(f"\n{'=' * 50}")
    print(f"DESAFIOS BÔNUS")
    print(f"{'=' * 50}")

    if estatisticas is not None:
        print(f"Média: {estatisticas['media']:.2f}")
        print(f"Mediana: {estatisticas['mediana']}")
        print(f"Moda: {estatisticas['moda']}")

    print(f"Fatorial de 5: {fatorial}")
    print(f"{relatorio_semanal}")


if __name__ == "__main__":
    main()
