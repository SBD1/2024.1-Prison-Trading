<center>

# Instalação

</center>

> Manual para Configuração do Ambiente e Criação de Conexão com PostgreSQL.

---
<center>

# Primeiro passo Criação do Database

</center>

> Rodar o script a baixo ou seguir as configurações da imagem (dentro do server criado):

Código:

````sql
CREATE DATABASE "Prison-Trading"
    WITH
    OWNER = prison_trading_user
    ENCODING = 'UTF8'
    LOCALE_PROVIDER = 'libc'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

COMMENT ON DATABASE "Prison-Trading"
    IS 'Banco de dados referente ao jogo Prison Trading';
````
Imagem:

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/p3.png?raw=true"/></div>
</div>

---
<center>

# Segundo passo Criação das tabelas

</center>

> Para criação das tabelas basta utilizar o DDL do projeto encontrado [aqui](https://sbd1.github.io/2024.1-Prison-Trading/#/Modulo-2/DDL).

---
<center>

# Terceiro passo População das tabelas

</center>

> Para população das tabelas basta utilizar o DML do projeto encontrado [aqui](https://sbd1.github.io/2024.1-Prison-Trading/#/Modulo-2/DML?id=inserts).

---
<center>

# Quarto passo Criação dos Triggers

</center>

> Para criação dos triggers basta utilizar os triggers do projeto encontrado [aqui](https://sbd1.github.io/2024.1-Prison-Trading/#/Modulo-3/Triggers).

---
<center>

# Quinto passo Criação dos Views

</center>

> Para criação dos triggers basta utilizar a view do projeto encontrado [aqui](https://sbd1.github.io/2024.1-Prison-Trading/#/Modulo-3/views).

---
<center>

# Sexto passo Configuração do pgAgent

</center>

> Para criação configuração do pgAgent basta seguir as intruções do pgAgent encontradas [aqui](https://sbd1.github.io/2024.1-Prison-Trading/#/Modulo-3/pgagent).

---
<center>

# Sétimo passo Clonar o repositório e abrir a branch main

</center>

> Repositório disponivel [aqui](https://github.com/SBD1/2024.1-Prison-Trading)

---
<center>

# Oitavo passo Baixar as bibliotecas usadas.

</center>

> Digitar esse comando no terminal:

````python
pip install psycopg2-binary os-sys time keyboard textwrap psycopg2
````

---
<center>

# Nono passo Rodar o jogo.

</center>

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |        Descrição         | Autores                                          |
|:----------:|:------:|:------------------------:|--------------------------------------------------|
| 11/08/2024 | `1.0`  |  Criação do documento.   | [João Antonio G.](https://github.com/joaoseisei) |
| 17/08/2024 | `1.1`  | Criação do tutorial SQL. | [João Antonio G.](https://github.com/joaoseisei) |
| 05/09/2024 | `1.2`  |    Atualiza tutorial.    | [João Antonio G.](https://github.com/joaoseisei) |

</div>
