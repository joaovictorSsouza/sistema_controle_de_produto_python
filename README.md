# 🧾 Sistema de Cadastro de Produtos (CRUD + Relatórios)

Um modelo de **sistema de cadastro de produtos com relatórios de estoque e de vendas**, desenvolvido em **Python**, utilizando **Programação Orientada a Objetos** e persistência de dados com **Pandas**.
O projeto tem como objetivo praticar **lógica de programação, modularização, POO e manipulação de dados**, simulando um sistema de gestão simples de produtos.

---

## 🚀 Funcionalidades

- ✅ **Cadastro de produtos**
- 📋 **Listagem de produtos**
- ✏️ **Atualização de informações**
- ❌ **Exclusão de produtos**
- 📦 **Relatório de estoque** (quantidade disponível de cada produto)
- 💰 **Relatório de vendas** (registro e total de vendas realizadas)
- ⚙️ **Tratamento de erros** e validações de entrada
- 💾 **Persistência de dados** em planilha Excel, utilizando a biblioteca Pandas.
- 🧩 **Organização modular** com pacotes e funções separadas

---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO) com classes para modelar os produtos
- Estruturas condicionais (`if`, `elif`, `else`)
- Estruturas de repetição (`for`, `while`)
- Modularização e uso de pacotes
- Entrada e saída de dados no terminal
- Tratamento de exceções (`try`, `except`)
- Manipulação de dados com a biblioteca **Pandas** para leitura e escrita em arquivos Excel.
- Organização de código para fácil manutenção

---

## 🏗️ Estrutura do Projeto

sistema_controle_de_produto_python/
│
├── main.py # Arquivo principal (ponto de entrada do programa)
│
├── classeProduto/
│   └── __init__.py # Define a classe Produto e seus métodos
│
├── sistema/
│   ├── Cadastro/     # Pacote com a lógica de cadastro (CRUD)
│   ├── Excel/        # Pacote para manipulação de arquivos Excel
│   ├── principal/    # Pacote com a estrutura principal do menu
│   ├── relatorio/    # Pacote com as funções de relatório
│   ├── uteis/        # Pacote com funções utilitárias (validação, títulos)
│   └── venda/        # Pacote com a lógica de controle de vendas
│
├── Produtos.xlsx # Banco de dados (planilha) onde os produtos são salvos
├── Vendas.xlsx   # Banco de dados (planilha) onde as vendas são salvas
│
└── README.md # Este arquivo

## 💻 Como Executar

1. Certifique-se de ter o **Python 3** instalado no seu computador.  
2. Faça o download ou clone o repositório:

https://github.com/joaovictorSsouza/sistema_controle_de_produto_python

3. Execute o progrma principal:
Python main.py

Exemplo de uso **cadastro**
![Menu_principal](Img/menu principal sistema.py.png)
![Menu_cadastro](Img/menu cadastro.png)

🔧 Melhorias Futuras

🖥️ Criar interface gráfica.

Desenvolvido por: João Victor Azevedo de Souza
Projeto de pratica em python.
Contato: joaovictor.souzacontato@gmail.com