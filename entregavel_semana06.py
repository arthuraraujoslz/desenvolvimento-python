from abc import ABC, abstractmethod


class Produto(ABC):
    """Classe abstrata que representa um produto genérico."""

    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    @property
    def nome(self):
        """Retorna o nome do produto."""
        return self._nome

    @nome.setter
    def nome(self, nome):
        """Valida e define o nome do produto."""
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError(f"O nome do produto deve ser uma string não vazia.")

        self._nome = nome.strip()

    @property
    def preco(self):
        """Retorna o preço do produto."""
        return self._preco

    @preco.setter
    def preco(self, preco):
        """Valida e define o preço do produto."""
        if not isinstance(preco, (int, float)) or isinstance(preco, bool):
            raise ValueError(f"O preço deve ser um valor numérico.")

        if preco < 0:
            raise ValueError(f"O preço não pode ser negativo.")

        self._preco = float(preco)

    @property
    def estoque(self):
        """Retorna a quantidade em estoque."""
        return self._estoque

    @estoque.setter
    def estoque(self, estoque):
        """Valida e define a quantidade em estoque."""
        if not isinstance(estoque, int) or isinstance(estoque, bool):
            raise ValueError(f"O estoque deve ser um número inteiro.")

        if estoque < 0:
            raise ValueError(f"O estoque não pode ser negativo.")

        self._estoque = estoque

    @abstractmethod
    def calcular_preco_final(self):
        """Calcula o preço final do produto conforme sua categoria."""

    @abstractmethod
    def descricao_categoria(self):
        """Retorna uma descrição específica da categoria do produto."""

    def adicionar_estoque(self, quantidade):
        """Adiciona unidades ao estoque do produto."""
        if not isinstance(quantidade, int) or isinstance(quantidade, bool):
            raise ValueError(f"A quantidade adicionada deve ser um inteiro.")

        if quantidade <= 0:
            raise ValueError(f"A quantidade adicionada deve ser maior que zero.")

        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        """Remove unidades do estoque quando houver saldo disponível."""
        if not isinstance(quantidade, int) or isinstance(quantidade, bool):
            raise ValueError(f"A quantidade removida deve ser um inteiro.")

        if quantidade <= 0:
            raise ValueError(f"A quantidade removida deve ser maior que zero.")

        if quantidade > self.estoque:
            raise ValueError(f"Não há estoque suficiente para essa remoção.")

        self.estoque -= quantidade

    def __str__(self):
        """Retorna uma representação amigável do produto."""
        return (
            f"Produto: {self.nome} | "
            f"Preço base: R$ {self.preco:.2f} | "
            f"Estoque: {self.estoque}"
        )

    def __repr__(self):
        """Retorna uma representação técnica do produto."""
        return (
            f"{self.__class__.__name__}("
            f"nome='{self.nome}', preco={self.preco}, estoque={self.estoque})"
        )

    def __lt__(self, outro_produto):
        """Compara produtos pelo preço base."""
        if not isinstance(outro_produto, Produto):
            return NotImplemented

        return self.preco < outro_produto.preco


class ProdutoFisico(Produto):
    """Representa um produto físico que possui peso e frete."""

    def __init__(self, nome, preco, estoque, peso, frete):
        super().__init__(nome, preco, estoque)
        self.peso = peso
        self.frete = frete

    @property
    def peso(self):
        """Retorna o peso do produto em quilogramas."""
        return self._peso

    @peso.setter
    def peso(self, peso):
        """Valida e define o peso do produto."""
        if not isinstance(peso, (int, float)) or isinstance(peso, bool):
            raise ValueError(f"O peso deve ser um valor numérico.")

        if peso <= 0:
            raise ValueError(f"O peso deve ser maior que zero.")

        self._peso = float(peso)

    @property
    def frete(self):
        """Retorna o valor do frete."""
        return self._frete

    @frete.setter
    def frete(self, frete):
        """Valida e define o valor do frete."""
        if not isinstance(frete, (int, float)) or isinstance(frete, bool):
            raise ValueError(f"O frete deve ser um valor numérico.")

        if frete < 0:
            raise ValueError(f"O frete não pode ser negativo.")

        self._frete = float(frete)

    def calcular_preco_final(self):
        """Calcula o preço final com o valor do frete."""
        return self.preco + self.frete

    def descricao_categoria(self):
        """Retorna a descrição da categoria física."""
        return f"Produto físico com peso de {self.peso:.2f} kg."

    def __str__(self):
        """Retorna uma representação amigável do produto físico."""
        return (
            f"{super().__str__()} | Tipo: Físico | "
            f"Peso: {self.peso:.2f} kg | Frete: R$ {self.frete:.2f}"
        )

    def __repr__(self):
        """Retorna uma representação técnica do produto físico."""
        return (
            f"ProdutoFisico(nome='{self.nome}', preco={self.preco}, "
            f"estoque={self.estoque}, peso={self.peso}, frete={self.frete})"
        )


class ProdutoDigital(Produto):
    """Representa um produto digital que possui tamanho de arquivo."""

    def __init__(self, nome, preco, estoque, tamanho_mb, formato_arquivo):
        super().__init__(nome, preco, estoque)
        self.tamanho_mb = tamanho_mb
        self.formato_arquivo = formato_arquivo

    @property
    def tamanho_mb(self):
        """Retorna o tamanho do arquivo digital em megabytes."""
        return self._tamanho_mb

    @tamanho_mb.setter
    def tamanho_mb(self, tamanho_mb):
        """Valida e define o tamanho do arquivo."""
        if not isinstance(tamanho_mb, (int, float)) or isinstance(
            tamanho_mb,
            bool,
        ):
            raise ValueError(f"O tamanho do arquivo deve ser numérico.")

        if tamanho_mb <= 0:
            raise ValueError(f"O tamanho do arquivo deve ser maior que zero.")

        self._tamanho_mb = float(tamanho_mb)

    @property
    def formato_arquivo(self):
        """Retorna o formato do arquivo digital."""
        return self._formato_arquivo

    @formato_arquivo.setter
    def formato_arquivo(self, formato_arquivo):
        """Valida e define o formato do arquivo."""
        if not isinstance(formato_arquivo, str) or not formato_arquivo.strip():
            raise ValueError(f"O formato do arquivo não pode ficar vazio.")

        self._formato_arquivo = formato_arquivo.strip().upper()

    def calcular_preco_final(self):
        """Calcula o preço final com desconto para produto digital."""
        desconto_digital = self.preco * 0.10
        return self.preco - desconto_digital

    def descricao_categoria(self):
        """Retorna a descrição da categoria digital."""
        return (
            f"Produto digital no formato {self.formato_arquivo} "
            f"com {self.tamanho_mb:.2f} MB."
        )

    def __str__(self):
        """Retorna uma representação amigável do produto digital."""
        return (
            f"{super().__str__()} | Tipo: Digital | "
            f"Formato: {self.formato_arquivo} | "
            f"Tamanho: {self.tamanho_mb:.2f} MB"
        )

    def __repr__(self):
        """Retorna uma representação técnica do produto digital."""
        return (
            f"ProdutoDigital(nome='{self.nome}', preco={self.preco}, "
            f"estoque={self.estoque}, tamanho_mb={self.tamanho_mb}, "
            f"formato_arquivo='{self.formato_arquivo}')"
        )


class ProdutoPerecivel(ProdutoFisico):
    """Representa um produto físico com data de validade."""

    def __init__(self, nome, preco, estoque, peso, frete, dias_validade):
        super().__init__(nome, preco, estoque, peso, frete)
        self.dias_validade = dias_validade

    @property
    def dias_validade(self):
        """Retorna a quantidade de dias de validade."""
        return self._dias_validade

    @dias_validade.setter
    def dias_validade(self, dias_validade):
        """Valida e define os dias de validade."""
        if not isinstance(dias_validade, int) or isinstance(dias_validade, bool):
            raise ValueError(f"Os dias de validade devem ser um número inteiro.")

        if dias_validade <= 0:
            raise ValueError(f"Os dias de validade devem ser maiores que zero.")

        self._dias_validade = dias_validade

    def calcular_preco_final(self):
        """Calcula preço com frete e desconto para produtos perecíveis."""
        preco_com_frete = self.preco + self.frete
        desconto_perecivel = preco_com_frete * 0.05
        return preco_com_frete - desconto_perecivel

    def descricao_categoria(self):
        """Retorna a descrição da categoria perecível."""
        return (
            f"Produto perecível com validade de "
            f"{self.dias_validade} dias."
        )

    def __str__(self):
        """Retorna uma representação amigável do produto perecível."""
        return (
            f"{super().__str__()} | Tipo: Perecível | "
            f"Validade: {self.dias_validade} dias"
        )

    def __repr__(self):
        """Retorna uma representação técnica do produto perecível."""
        return (
            f"ProdutoPerecivel(nome='{self.nome}', preco={self.preco}, "
            f"estoque={self.estoque}, peso={self.peso}, frete={self.frete}, "
            f"dias_validade={self.dias_validade})"
        )


def exibir_relatorio(produtos):
    """Exibe um relatório formatado dos produtos cadastrados."""
    print(f"\n{'=' * 75}")
    print(f"RELATÓRIO DO SISTEMA DE E-COMMERCE")
    print(f"{'=' * 75}")

    for produto in produtos:
        print(f"\n{produto}")
        print(f"Categoria: {produto.descricao_categoria()}")
        print(f"Preço final: R$ {produto.calcular_preco_final():.2f}")

    print(f"\n{'=' * 75}")
    print(f"PRODUTOS ORDENADOS POR PREÇO BASE")
    print(f"{'=' * 75}")

    for produto in sorted(produtos):
        print(f"{produto.nome}: R$ {produto.preco:.2f}")

    print(f"{'=' * 75}")


def demonstrar_excecoes():
    """Demonstra validações disparadas pelos setters das propriedades."""
    print(f"\nDEMONSTRAÇÃO DE TRATAMENTO DE EXCEÇÕES")

    try:
        ProdutoFisico(
            nome="Produto Inválido",
            preco=-50,
            estoque=10,
            peso=1.0,
            frete=10.0,
        )
    except ValueError as erro:
        print(f"Erro capturado ao criar produto: {erro}")

    try:
        produto_teste = ProdutoDigital(
            nome="Curso de Python",
            preco=100,
            estoque=20,
            tamanho_mb=250,
            formato_arquivo="pdf",
        )
        produto_teste.estoque = -5
    except ValueError as erro:
        print(f"Erro capturado ao alterar estoque: {erro}")

    try:
        produto_teste = ProdutoFisico(
            nome="Mouse Gamer",
            preco=150,
            estoque=5,
            peso=0.2,
            frete=20,
        )
        produto_teste.remover_estoque(10)
    except ValueError as erro:
        print(f"Erro capturado ao remover estoque: {erro}")


def main():
    """Cria instâncias e executa as demonstrações do sistema."""
    produtos = [
        ProdutoFisico("Notebook", 3500.00, 8, 2.3, 45.00),
        ProdutoFisico("Teclado Mecânico", 450.00, 15, 0.9, 20.00),
        ProdutoFisico("Monitor", 1200.00, 10, 4.5, 35.00),
        ProdutoDigital("E-book Python", 49.90, 100, 5.2, "pdf"),
        ProdutoDigital("Curso de Django", 199.90, 50, 1200.0, "mp4"),
        ProdutoDigital("Planilha Financeira", 29.90, 80, 1.5, "xlsx"),
        ProdutoPerecivel("Leite Integral", 6.50, 30, 1.0, 2.00, 10),
        ProdutoPerecivel("Queijo Minas", 35.90, 12, 0.5, 5.00, 20),
        ProdutoPerecivel("Iogurte Natural", 8.90, 25, 0.2, 3.00, 15),
        ProdutoFisico("Cadeira de Escritório", 899.90, 6, 12.0, 80.00),
    ]

    print(f"Bem-vindo ao Sistema POO de E-commerce!")

    exibir_relatorio(produtos)

    print(f"\nDEMONSTRAÇÃO DE POLIMORFISMO")
    print(f"{'=' * 75}")

    for produto in produtos:
        print(
            f"{produto.nome} | "
            f"Classe: {produto.__class__.__name__} | "
            f"Preço final: R$ {produto.calcular_preco_final():.2f}"
        )

    demonstrar_excecoes()

    print(f"\nSistema finalizado com sucesso.")


if __name__ == "__main__":
    main()
