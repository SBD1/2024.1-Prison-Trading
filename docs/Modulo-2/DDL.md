<center>

# Linguagem de Definição de Dados - DDL

</center>

---

> O que é?


> PARTE DO JOAO NAO MEXER!!!
```

CREATE TYPE TipoItem AS ENUM('fabricavel', 'nao_fabricavel');
CREATE TYPE TipoItemFabricavel AS ENUM('ferramenta', 'arma');

CREATE TABLE item(
	id_item SERIAL NOT NULL,
	tipo_item TipoItem NOT NULL,
	PRIMARY KEY(id_item)
);

CREATE TABLE item_fabricavel(
	id_item INTEGER NOT NULL,
	tipo_fabricavel TipoItemFabricavel NOT NULL,
	PRIMARY KEY (id_item),
	FOREIGN KEY (id_item) REFERENCES item(id_item)
);

CREATE TABLE ferramenta(
	id_item INTEGER NOT NULL,
	nome_item CHAR(25) NOT NULL UNIQUE,
	tamanho_item INT NOT NULL DEFAULT 1 CHECK (tamanho_item >= 1),
	descricao_item TEXT NOT NULL,
	utilidade_ferramenta TEXT NOT NULL,
	PRIMARY KEY (id_item),
	FOREIGN KEY (id_item) REFERENCES item_fabricavel(id_item)
);

CREATE TABLE arma(
	id_item INTEGER NOT NULL,
	nome_item CHAR(25) NOT NULL UNIQUE,
	tamanho_item INT NOT NULL DEFAULT 1 CHECK (tamanho_item >= 1),
	descricao_efeito_item TEXT NOT NULL,
	dano_arma INT NOT NULL,
	PRIMARY KEY (id_item),
	FOREIGN KEY (id_item) REFERENCES item_fabricavel(id_item)
);

CREATE TABLE Livro_Fabricacao(
	id_livro_fabricacao SERIAL NOT NULL,
	nome_livro_fabricacao CHAR(25) NOT NULL UNIQUE,
	PRIMARY KEY (id_livro_fabricacao)
);


CREATE TABLE fabricacao(
	id_fabricacao SERIAL NOT NULL,
	item_fabricavel INTEGER NOT NULL,
	livro_fabricacao INTEGER NOT NULL,
	PRIMARY KEY (id_fabricacao, item_fabricavel),
	FOREIGN KEY (item_fabricavel) REFERENCES item_fabricavel(id_item),
	FOREIGN KEY (livro_fabricacao) REFERENCES livro_fabricacao(id_livro_fabricacao)
);

```
> PARTE DO JOAO NAO MEXER!!!

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

|    Data    | Versão | Descrição             | Autores                                          |
|:----------:|:------:|-----------------------|--------------------------------------------------|
| 28/07/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |

</div>