<center>

# Instalação

</center>

> Manual para Configuração do Ambiente e Criação de Conexão com PostgreSQL.

---
<center>

# Primeiro passo Criação do usuário padrão

</center>

> Rodar o script de criação de usuário a baixo:

````sql
CREATE ROLE prison_trading_user WITH
	LOGIN
	NOSUPERUSER
	CREATEDB
	NOCREATEROLE
	INHERIT
	NOREPLICATION
	NOBYPASSRLS
	CONNECTION LIMIT -1
	PASSWORD '123';
COMMENT ON ROLE prison_trading_user IS 'Usuário padrão para acesso ao banco de dados do jogo prison trading';
````

---
<center>

# Segundo passo Criação do server

</center>

> Criar o servidor passando como referência o:

* Host name/address : localhost
* Port : 5432
* Username : prison_trading_user
* Password : 123

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/p2.png?raw=true"/></div>
</div>

---
<center>

# Terceiro passo Criação do database

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

# Quarto passo Criação das tabelas

</center>

> Para criação das tabelas basta utilizar o DDL do projeto encontrado [aqui](https://github.com/SBD1/2024.1-Prison-Trading/blob/main/src/DDL.sql).

---
<center>

# Quinto passo População das tabelas

</center>

> Para população das tabelas basta utilizar o DML do projeto encontrado [aqui](https://github.com/SBD1/2024.1-Prison-Trading/blob/main/src/DML.sql).

---
<center>

# Sexto passo Rodar clonar o repositório e abrir a branch main

</center>

> Repositório disponivel [aqui](https://github.com/SBD1/2024.1-Prison-Trading)

---
<center>

# Sétimo passo Baixar as bibliotecas usadas.

</center>

> Digitar esse comando no terminal:

````python
pip install psycopg2
````

---
<center>

# Oitavo passo Rodar o jogo.

</center>

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |        Descrição         | Autores                                          |
|:----------:|:------:|:------------------------:|--------------------------------------------------|
| 11/08/2024 | `1.0`  |  Criação do documento.   | [João Antonio G.](https://github.com/joaoseisei) |
| 17/08/2024 | `1.1`  | Criação do tutorial SQL. | [João Antonio G.](https://github.com/joaoseisei)                                                 |

</div>