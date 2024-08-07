<center>

# Linguagem de Definição de Dados - DDL

</center>

---

<CENTER>

# O Que é?

</CENTER>

> DDL é um subconjunto de SQL (Structured Query Language) usado para definir e gerenciar a estrutura de bancos de dados e suas tabelas. Com o DDL é possivel criar, modificar e excluir objetos no banco de dados.

---

```
CREATE TYPE TipoItem AS ENUM('fabricavel', 'nao_fabricavel');
CREATE TYPE TipoItemFabricavel AS ENUM('ferramenta', 'arma');

CREATE TABLE item(
	id SERIAL NOT NULL,
	tipo TipoItem NOT NULL,
	PRIMARY KEY(id)
);

-- TODO ADICIONAR INSTANCIA DE ITEM PRECISA DE LUGAR E INVENTARIO PRONTOS

CREATE TABLE instancia_item(
	id SERIAL NOT NULL,
	item INTEGER NOT NULL,
	lugar INTEGER NOT NULL,
	regiao INTEGER NOT NULL,
	inventario INTEGER NOT NULL,
	pessoa INTEGER NOT NULL,
	PRIMARY KEY (id, item),
	FOREIGN KEY (item) REFERENCES item (id),
	FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao),
	FOREIGN KEY (inventario, pessoa) REFERENCES inventario(id, pessoa)
);

-- POSSIVEL ERRO EM INSTANCIA CONFERIR QUANDO FIZEREM INVENTARIO E LUGAR

CREATE TABLE item_fabricavel(
	id INTEGER NOT NULL,
	tipo TipoItemFabricavel NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item(id)
);

CREATE TABLE ferramenta(
	id INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	tamanho SMALLINT NOT NULL DEFAULT 1,
	descricao TEXT NOT NULL,
	utilidade TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item_fabricavel(id)
);

CREATE TABLE arma(
	id INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	tamanho SMALLINT NOT NULL DEFAULT 1,
	descricao TEXT NOT NULL,
	dano SMALLINT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item_fabricavel(id)
);

CREATE TABLE livro_fabricacao(
	id SERIAL NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	PRIMARY KEY (id)
);


CREATE TABLE fabricacao(
	id SERIAL NOT NULL,
	item_fabricavel INTEGER NOT NULL,
	livro_fabricacao INTEGER NOT NULL,
	PRIMARY KEY (id, item_fabricavel),
	FOREIGN KEY (item_fabricavel) REFERENCES item_fabricavel(id),
	FOREIGN KEY (livro_fabricacao) REFERENCES livro_fabricacao(id)
);

CREATE TABLE lista_fabricacao(
	item_fabricavel INTEGER NOT NULL,
	fabricacao INTEGER NOT NULL,
	item INTEGER NOT NULL,
	FOREIGN KEY (item_fabricavel, fabricacao) REFERENCES fabricacao(item_fabricavel, id),
	FOREIGN KEY (item) REFERENCES item(id)
);

```

>PARTE DO FERNANDO, MEXER!!!

CREATE TABLE utilizavel(
	id_item INTEGER NOT NULL,
	nome_item CHAR(25) NOT NULL UNIQUE,
	tamanho_item INT NOT NULL DEFAULT 1 CHECK (tamanho_item >= 1),
	descricao_item TEXT NOT NULL,
	dano_arma INT NOT NULL,
	PRIMARY KEY (id_item),
	FOREIGN KEY (id_item) REFERENCES item_fabricavel(id_item)
);

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                          | Autores                                          |
|:----------:|:------:|------------------------------------|--------------------------------------------------|
| 28/07/2024 | `1.0`  | Criação do documento.              | [João Antonio G.](https://github.com/joaoseisei) |
| 06/08/2024 | `1.1`  | Adiciona DDL Prevido de fabricacao | [João Antonio G.](https://github.com/joaoseisei) |

</div>