# 🐍 PyWorkbook

> **Um micro-framework CLI leve para organizar múltiplos exercícios Python em um único arquivo.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Read in English](https://img.shields.io/badge/Read_in-English-blue)](./README.md)

## 🎯 O Problema
Durante cursos de programação, é comum ter que realizar dezenas de pequenos desafios por aula. A abordagem tradicional cria uma bagunça de arquivos (`ex01.py`, `ex02.py`, `teste.py`...) ou obriga o uso de Notebooks, o que distancia o aluno de ambientes de desenvolvimento reais.

## 💡 A Solução
Este micro-framework permite escrever **todos os exercícios de uma aula em um único arquivo**, gerando automaticamente um **Menu Interativo (CLI)** no terminal.

Basta adicionar um **Decorador** (`@regFunction`) acima da função e ela aparecerá magicamente no menu.

## ✨ Funcionalidades
- **Organização Limpa:** Um arquivo por módulo/aula, múltiplos exercícios dentro.
- **Auto-Discovery:** Uso de Decorators para registrar funções automaticamente sem `if/else` manuais.
- **Developer Experience:** Acompanha Snippets do VS Code para criar a estrutura do exercício em 1 segundo.
- **Cross-Platform:** Funciona em Linux (Fedora/Ubuntu), Windows e macOS.

---

## 🚀 Como Usar

### 1. Estrutura Básica
No seu arquivo de aula (ex: `aula01.py`), importe o framework e use o decorador:

```python
from pyworkbook.pyworkbook import regFunction, startMenu

# O Decorador registra a função no menu automaticamente
@regFunction("Olá Mundo")
def exercicio_01():
    print("Olá! Este é meu primeiro exercício.")

@regFunction("Calculadora")
def exercicio_02():
    a = int(input("Digite A: "))
    b = int(input("Digite B: "))
    print(f"Soma: {a + b}")

if __name__ == "__main__":
    startMenu()
```

### 2. Rodando o Projeto

Abra seu terminal e execute:
```Bash

python aula01.py
```
O resultado será um menu interativo:
```Plaintext

-------- MENU DE FUNÇÕES --------
=================================

 [1] - Olá Mundo
 [2] - Calculadora

---------------------------------

 [0] - Sair

Digite o número da função desejada: 
```
⚡ Produtividade com VS Code (Snippets)

Este projeto inclui configurações de Workspace para o VS Code. Ao abrir a pasta do projeto, você ganha acesso ao snippet newExercise.

    Digite rgf

    Aperte Tab

    A estrutura completa da função e do decorador será criada instantaneamente.

🛠️ Como Funciona (Under the Hood)

Este projeto utiliza o conceito de Higher-Order Functions e Metaprogramação.

    O Decorator (@regFunction): É executado em Definition Time (quando o Python lê o arquivo).

    Side Effect: Ao ser lido, o decorador armazena a referência da função em um Dicionário de Rotas.

    Inversão de Controle: O loop principal (startMenu) itera sobre esse dicionário dinâmico, permitindo que novos exercícios sejam adicionados sem alterar o código do motor principal.

📂 Estrutura do Projeto
    
    .
    ├── .vscode/                # Configurações e Snippets automáticos
    ├── pyworkbook/             # O "motor" do CLI (Decorators e Menu)
    │   └── pyworkbook.py       # Lógica principal
    └── README.md               # Documentação

Feito com ☕ e Python por Felipe Souza De Oliveira.