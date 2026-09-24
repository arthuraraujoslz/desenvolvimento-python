"""Soluções dos mini-desafios da Semana 01."""


def calcular_troco():
    """Calcula a diferença entre o valor pago e o valor da compra."""
    # Desafio 1: calcula e exibe o troco da compra.
    valor_compra = float(input("Valor da compra: R$ "))
    valor_pago = float(input("Valor pago: R$ "))
    troco = valor_pago - valor_compra

    print(f"Troco: R$ {troco:.2f}")


def calcular_media_notas():
    """Calcula a média aritmética de três notas."""
    # Desafio 2: recebe três notas e mostra a média com duas casas.
    primeira_nota = float(input("Primeira nota: "))
    segunda_nota = float(input("Segunda nota: "))
    terceira_nota = float(input("Terceira nota: "))
    media = (primeira_nota + segunda_nota + terceira_nota) / 3

    print(f"Média das notas: {media:.2f}")


def converter_tempo():
    """Converte uma quantidade inteira de segundos para HH:MM:SS."""
    # Desafio 3: transforma segundos em horas, minutos e segundos.
    total_segundos = int(input("Quantidade de segundos: "))
    horas = total_segundos // 3600
    minutos = (total_segundos % 3600) // 60
    segundos = total_segundos % 60

    print(f"Tempo convertido: {horas:02d}:{minutos:02d}:{segundos:02d}")


def calcular_desconto():
    """Aplica um percentual de desconto ao preço de um produto."""
    # Desafio 4: calcula o preço final após o desconto informado.
    preco_produto = float(input("Preço do produto: R$ "))
    percentual_desconto = float(input("Percentual de desconto: "))
    valor_desconto = preco_produto * (percentual_desconto / 100)
    preco_final = preco_produto - valor_desconto

    print(f"Preço final: R$ {preco_final:.2f}")


def verificar_par_ou_impar():
    """Informa se um número inteiro é par ou ímpar."""
    # Desafio 5: usa o operador módulo para verificar a paridade.
    numero = int(input("Digite um número inteiro: "))

    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")


def inverter_nome():
    """Exibe o nome digitado na ordem inversa."""
    # Desafio 6: utiliza slicing para inverter o texto informado.
    nome = input("Digite um nome: ")
    nome_invertido = nome[::-1]

    print(f"Nome invertido: {nome_invertido}")


def main():
    """Executa todos os desafios em sequência."""
    print("=" * 50)
    print("DESAFIO 1 - CALCULADORA DE TROCO")
    print("=" * 50)
    calcular_troco()

    print("\n" + "=" * 50)
    print("DESAFIO 2 - MÉDIA DE NOTAS")
    print("=" * 50)
    calcular_media_notas()

    print("\n" + "=" * 50)
    print("DESAFIO 3 - CONVERSOR DE TEMPO")
    print("=" * 50)
    converter_tempo()

    print("\n" + "=" * 50)
    print("DESAFIO 4 - CALCULADORA DE DESCONTO")
    print("=" * 50)
    calcular_desconto()

    print("\n" + "=" * 50)
    print("DESAFIO 5 - PAR OU ÍMPAR")
    print("=" * 50)
    verificar_par_ou_impar()

    print("\n" + "=" * 50)
    print("DESAFIO 6 - INVERSOR DE NOME")
    print("=" * 50)
    inverter_nome()


if __name__ == "__main__":
    main()
