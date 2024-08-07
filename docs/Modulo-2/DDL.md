<center>

# Linguagem de Definição de Dados - DDL

</center>

---

<CENTER>

# O Que é?

</CENTER>

> DDL é um subconjunto de SQL (Structured Query Language) usado para definir e gerenciar a estrutura de bancos de dados e suas tabelas. Com o DDL é possivel criar, modificar e excluir objetos no banco de dados.

---

```sql
BEGIN TRANSACTION;

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
	lugar INTEGER NULL,
	regiao INTEGER NULL,
	inventario INTEGER NULL,
	pessoa INTEGER NULL,
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

COMMIT;
```

>PARTE DO FERNANDO, MEXER!!!

CREATE TYPE TipoItemNaoFabricavel AS ENUM('comida', 'medicamento', 'utilizavel');


CREATE TABLE item_nao_fabricavel(
	id INTEGER NOT NULL,
	tipo TipoItemNaoFabricavel NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item(id)
);

CREATE TABLE medicamento(
	id INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	tamanho SMALLINT NOT NULL DEFAULT 1 
	descricao TEXT NOT NULL,
	raridade SMALLINT NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2)
	cura SMALLINT NOT NULL,
	quantidade SMALLINT NOT NULL DEFAULT 5
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
);

CREATE TABLE comida(
	id INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	tamanho SMALLINT NOT NULL DEFAULT 1 
	descricao TEXT NOT NULL,
	raridade SMALLINT NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2)
	quantidade SMALLINT NOT NULL DEFAULT 3
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
);

CREATE TABLE utilizavel(
	id INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	tamanho SMALLINT NOT NULL DEFAULT 1 
	descricao TEXT NOT NULL,
	raridade SMALLINT NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2)
	quantidade SMALLINT NOT NULL DEFAULT 1,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
);

CREATE TABLE missao(
	id SERIAL NOT NULL,
	item INTEGER NOT NULL,
	lugar INTEGER NOT NULL,
	nome CHAR(25) NOT NULL UNIQUE,
	descricao TEXT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (item) REFERENCES item_nao_fabricavel(id)
	FOREIGN KEY (lugar) REFERENCES lugar(id, regiao),

);

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                          | Autores                                          |
| :--------: | :----: | ---------------------------------- | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.              | [João Antonio G.](https://github.com/joaoseisei) |
| 06/08/2024 | `1.1`  | Adiciona DDL Prevido de fabricacao | [João Antonio G.](https://github.com/joaoseisei) |
| 07/08/2024 | `1.2`  | Adiciona parte do fernando         | [Fernando Gabriel](https://github.com/show-dawn) |


</div>