# Desenvolvimento em Python — Atividades Acadêmicas

Este repositório contém as soluções dos desafios e projetos desenvolvidos para a disciplina de Desenvolvimento em Python, cobrindo desde os fundamentos da linguagem até estruturas de dados, controle de fluxo, modularização e boas práticas aplicadas.

## Sobre o Projeto

O objetivo deste repositório é consolidar o aprendizado prático em Python, aplicando boas práticas de programação, organização de código conforme a PEP 8 e resolução de problemas do mundo real.

## Etapas do Projeto

### Semana 01 — Fundamentos de Python e Prática Independente
Resolução dos 6 mini-desafios focados na sintaxe básica, manipulação de variáveis, operadores e entrada/saída de dados:
- **Calculadora de Troco:** Cálculo automático da diferença entre o valor pago e o valor da compra.
- **Média de Notas:** Entrada de 3 notas via `input()` e exibição da média aritmética com 2 casas decimais.
- **Conversor de Tempo:** Conversão de valores em segundos para o formato `HH:MM:SS`.
- **Calculadora de Desconto:** Aplicação de percentual de desconto sobre o preço original do produto.
- **Par ou Ímpar:** Verificação de paridade de números inteiros utilizando o operador de módulo `%`.
- **Inversor de Nome:** Inversão de strings utilizando a técnica de slicing `[::-1]`.

### Semana 02 — Estruturas de Controle e Repetição
Resolução dos 4 desafios focados em tomada de decisão e laços de repetição:
- **Classificador de Cliente:** Classificação de clientes nas categorias Bronze, Prata, Ouro ou Diamante com base em idade e renda usando `if/elif/else`.
- **Menu de Operações Matemáticas:** Calculadora com 4 operações básicas utilizando a estrutura `match/case`.
- **Análise de Números:** Leitura de 5 números via `input()` para cálculo de soma, média, maior e menor valor utilizando laço `for`.
- **Sistema de Autenticação:** Validação de acesso com limite de 3 tentativas utilizando laço `while`.

### Semana 03 — Modularização, Funções e Estruturas Avançadas
Organização de código modularizado aplicando conceitos de parâmetros, retornos, tratamento defensivo, `*args`, `**kwargs` e recursão:
- **Módulo Calculadora:** Operações matemáticas básicas com tratamento defensivo de divisão por zero.
- **Módulo Utilidades:** Funções para conversão de temperatura, validação de senha, cálculo de caixa (`*args`) e ficha de aluno (`**kwargs`).
- **Lista Segura:** Manipulação defensiva de coleções mutáveis sem alterar a lista original.
- **Funções Bônus e Avançadas:** Módulo estatístico (média, mediana, moda), função recursiva de fatorial e gerador de relatórios configuráveis.
- **Equivalência em Portugal:** Demonstração da lógica em pseudocódigo comparada ao Python.

### Semana 04 — Estruturas de Dados e Equivalência em Portugol
Finalização do sistema de produtos aplicando conceitos de Listas, Tuplas e Conjuntos em Python, incluindo a demonstração de equivalência lógica estrutural em Portugol.
- **Cadastro e Filtragem:** Implementação de listas dinâmicas (`append()`) e laços de repetição para busca de valores.
- **Ordenação:** Uso de `sort()` e `sorted()` contrastado com a lógica manual do Bubble Sort.
- **Categorias Únicas:** Utilização de `set()` para a eliminação automática de elementos duplicados.
- **Estatísticas:** Extração de métricas de preços (menor, maior, média) consolidadas de forma segura em uma tupla imutável.

### Semana 05 — Manipulação de Arquivos, Regex e Tratamento de Exceções
Finalização do Sistema de Análise de Dados aplicando leitura segura de arquivos, validações avançadas de formatos e gestão robusta de erros.
- **Leitura Segura:** Utilização de blocos `with open(..., encoding="utf-8")` para manipulação de arquivos de texto e CSV.
- **Validação com Expressões Regulares (`re`):** Emprego de *raw strings* e metacaracteres para validação rigorosa de e-mails, CPFs, telefones e datas.
- **Tratamento de Exceções Avançado:** Estruturas completas contendo `try/except/else/finally` para captura de `FileNotFoundError`, `ValueError` e `KeyError`.
- **Exceção Personalizada:** Criação de classe de erro própria herdando de `Exception` para gerenciar regras específicas de validação de dados.
- **Relatório Automatizado:** Processamento e consolidação de estatísticas de registros válidos e inválidos formatados por meio de *f-strings*.

## Arquivos do Repositório

- `entregavel_semana01.py`: Código-fonte principal com as funções dos 6 mini-desafios da Semana 01.
- `entregavel_semana02.py`: Código-fonte com as funções dos 4 desafios de estruturas de controle da Semana 02.
- `entregavel_semana03.py`: Código-fonte com os módulos, funções e desafios avançados da Semana 03.
- `entregavel_semana04.py`: Código-fonte com o sistema de produtos e a aplicação de estruturas de dados (Listas, Tuplas, Conjuntos) da Semana 04.
- `entregavel_semana05/sistema_analise_dados.py`: Código-fonte do sistema de análise de dados com validação via regex e exceções personalizadas.
- `README.md`: Documentação e estrutura explicativa completa do repositório.

## Boas Práticas Aplicadas

- Nomenclatura de variáveis e funções em `snake_case` (convenção PEP 8).
- Documentação de funções através de *docstrings*.
- Conversão explícita de tipos de dados (`int`, `float`).
- Formatação de saídas limpas e claras utilizando *f-strings*.
- Uso de estruturas modernas (`match/case`, laços `for`/`while`).
- Programação defensiva (cópia de listas e tratamento de exceções).
- Modularização e reaproveitamento de código com `if __name__ == "__main__":`.
