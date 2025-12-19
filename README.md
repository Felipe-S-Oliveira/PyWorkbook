# 🐍 PyWorkbook

> **A lightweight CLI framework for organizing multiple Python exercises in a single file.**

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](./LICENSE)
[![Read in Portuguese](https://img.shields.io/badge/Leia_em-Português-yellow)](./README_pt-br.md)

## 🎯 The Problem
During programming courses, students often have to solve dozens of small coding challenges per class. The traditional approach creates a clutter of files (`ex01.py`, `ex02.py`, `test.py`...) or forces the use of Notebooks, which distances the student from real-world software development environments.

## 💡 The Solution
This micro-framework allows you to write **all exercises for a specific class in a single file**, automatically generating an **Interactive CLI Menu** in the terminal.

Simply add a **Decorator** (`@regFunction`) above your function, and it will magically appear in the menu.

## ✨ Features
- **Clean Organization:** One file per module/class, multiple exercises inside.
- **Auto-Discovery:** Uses Decorators to automatically register functions without manual `if/else` chains.
- **Developer Experience:** Includes VS Code Snippets to scaffold new exercises in 1 second.
- **Cross-Platform:** Works on Linux (Fedora/Ubuntu), Windows, and macOS.

---

## 🚀 Getting Started

### 1. Basic Structure
In your lesson file (e.g., `class01.py`), import the framework and use the decorator:

```python
from pyworkbook.pyworkbook import regFunction, startMenu

# The Decorator automatically registers the function to the menu
@regFunction("Hello World")
def exercise_01():
    print("Hello! This is my first exercise.")

@regFunction("Calculator")
def exercise_02():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    print(f"Sum: {a + b}")

if __name__ == "__main__":
    startMenu()
```
### 2. Running the Project

Open your terminal and run:
```Bash

python class01.py
```

The result will be an interactive menu:
```Plaintext

-------- MENU DE FUNÇÕES --------
=================================

 [1] - Hello World
 [2] - Calculator

---------------------------------

 [0] - Exit

Digite o número da função desejada: 
```

⚡ VS Code Productivity (Snippets)

This project includes Workspace Settings for VS Code. When you open the project folder, you gain access to the newExercise snippet.

    Type rgf

    Press Tab

    The complete structure for the function and decorator is created instantly.

🛠️ How It Works (Under the Hood)

For Computer Science students and recruiters interested in the implementation details:

This project applies Higher-Order Functions and Metaprogramming concepts.

    The Decorator (@regFunction): Executed at Definition Time (when Python reads the file).

    Side Effect: Upon reading, the decorator stores the function reference in a Route Dictionary.

    Inversion of Control: The main loop (startMenu) iterates over this dynamic dictionary, allowing new exercises to be added without modifying the engine code.

📂 Project Structure

    .
    ├── .vscode/                # Auto-configuration and Snippets
    ├── pyworkbook/             # The CLI Engine (Decorators and Menu)
    │   └── pyworkbook.py       # Core logic
    └── README.md               # Documentation

Made with ☕ and Python by Felipe Souza De Oliveira.
