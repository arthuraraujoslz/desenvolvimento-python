"""Soluções dos mini-desafios da Semana 02."""


def classificar_cliente():
    """Classifica o cliente de acordo com idade e renda mensal."""
    # Desafio 1: classifica o cliente em uma categoria de fidelidade.
    idade = int(input("Digite a idade do cliente: "))
    renda = float(input("Digite a renda mensal do cliente: R$ "))

    if idade < 18 or renda < 3000:
        categoria = "Bronze"
    elif renda < 6000:
        categoria = "Prata"
    elif renda < 10000:
        categoria = "Ouro"
    else:
        categoria = "Diamante"

    print(f"Cliente classificado na categoria: {categoria}")


def executar_operacao_matematica():
    """Executa uma operação matemática escolhida no menu."""
    # Desafio 2: usa match/case para selecionar uma operação matemática.
    print(f"1 - Soma")
    print(f"2 - Subtração")
    print(f"3 - Multiplicação")
    print(f"4 - Divisão")
    opcao = int(input("Escolha uma operação: "))
    primeiro_numero = float(input("Digite o primeiro número: "))
    segundo_numero = float(input("Digite o segundo número: "))

    match opcao:
        case 1:
            resultado = primeiro_numero + segundo_numero
            print(f"Resultado da soma: {resultado}")
        case 2:
            resultado = primeiro_numero - segundo_numero
            print(f"Resultado da subtração: {resultado}")
        case 3:
            resultado = primeiro_numero * segundo_numero
            print(f"Resultado da multiplicação: {resultado}")
        case 4:
            if segundo_numero == 0:
                print(f"Não é possível dividir por zero.")
            else:
                resultado = primeiro_numero / segundo_numero
                print(f"Resultado da divisão: {resultado}")
        case _:
            print(f"Opção inválida.")


def analisar_numeros():
    """Calcula soma, média, maior e menor valor de cinco números."""
    # Desafio 3: lê cinco números com um laço for e analisa os valores.
    numeros = []

    for indice in range(1, 6):
        numero = float(input(f"Digite o {indice}º número: "))
        numeros.append(numero)

    soma = sum(numeros)
    media = soma / len(numeros)
    maior_numero = max(numeros)
    menor_numero = min(numeros)

    print(f"Soma: {soma}")
    print(f"Média: {media:.2f}")
    print(f"Maior valor: {maior_numero}")
    print(f"Menor valor: {menor_numero}")


def autenticar_usuario():
    """Solicita a senha e bloqueia o acesso após três erros."""
    # Desafio 4: controla as tentativas de acesso com um laço while.
    senha_correta = "python123"
    tentativas = 0
    limite_tentativas = 3

    while tentativas < limite_tentativas:
        senha = input("Digite a senha: ")

        if senha == senha_correta:
            print(f"Acesso autorizado após {tentativas + 1} tentativa(s).")
            return

        tentativas += 1
        tentativas_restantes = limite_tentativas - tentativas

        if tentativas_restantes > 0:
            print(f"Senha incorreta. Restam {tentativas_restantes} tentativa(s).")

    print(f"Acesso bloqueado após {limite_tentativas} tentativas incorretas.")


def main():
    """Executa todos os desafios da Semana 02 em sequência."""
    print(f"{'=' * 50}")
    print(f"DESAFIO 1 - CLASSIFICADOR DE CLIENTE")
    print(f"{'=' * 50}")
    classificar_cliente()

    print(f"\n{'=' * 50}")
    print(f"DESAFIO 2 - MENU DE OPERAÇÕES MATEMÁTICAS")
    print(f"{'=' * 50}")
    executar_operacao_matematica()

    print(f"\n{'=' * 50}")
    print(f"DESAFIO 3 - ANÁLISE DE NÚMEROS")
    print(f"{'=' * 50}")
    analisar_numeros()

    print(f"\n{'=' * 50}")
    print(f"DESAFIO 4 - SISTEMA DE AUTENTICAÇÃO")
    print(f"{'=' * 50}")
    autenticar_usuario()


if __name__ == "__main__":
    main()
