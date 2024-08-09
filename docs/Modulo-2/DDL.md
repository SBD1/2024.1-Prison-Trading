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

CREATE TYPE TipoItem AS ENUM('fabricavel', 'nao fabricavel');
CREATE TYPE TipoItemFabricavel AS ENUM('ferramenta', 'arma');
CREATE TYPE TipoItemNaoFabricavel AS ENUM('comida', 'medicamento', 'utilizavel');
CREATE TYPE TipoPessoa AS ENUM('policial', 'informante', 'prisioneiro', 'jogador');
CREATE TYPE TipoGangue AS ENUM('polvo', 'palhaco');

CREATE TABLE prisao(
    id SERIAL NOT NULL,
    nome CHAR(25) NOT NULL,
    objetivo TEXT NOT NULL,
    PRIMARY KEY (id)
); 

CREATE TABLE regiao(
    id SERIAL NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    prisao INTEGER NOT NULL,
    descricao TEXT NOT NULL,
    PRIMARY KEY (id), 
    FOREIGN KEY (prisao) REFERENCES prisao(id)
);

CREATE TABLE lugar(
    id SERIAL NOT NULL, 
    regiao INTEGER NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    PRIMARY KEY (id, regiao),
    FOREIGN KEY (regiao) REFERENCES regiao(id)
);

CREATE TABLE lugar_origem_destino(
    lugar_origem INTEGER NOT NULL,
    regiao_origem INTEGER NOT NULL,
    lugar_destino INTEGER NOT NULL,
    regiao_destino INTEGER NOT NULL,
    FOREIGN KEY (lugar_origem, regiao_origem) REFERENCES lugar(id, regiao),
    FOREIGN KEY (lugar_destino, regiao_destino) REFERENCES lugar(id, regiao)
);

CREATE TABLE pessoa(
    id SERIAL NOT NULL,
    tipo TipoPessoa NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE inventario(
    id SERIAL NOT NULL,
    pessoa INTEGER NOT NULL,
    tamanho SMALLINT NOT NULL DEFAULT 5,
    inventario_ocupado SMALLINT NOT NULL CHECK(inventario_ocupado BETWEEN 0 AND tamanho),
    PRIMARY KEY (id, pessoa),
    FOREIGN KEY (pessoa) REFERENCES pessoa(id)
);

CREATE TABLE item(
    id SERIAL NOT NULL,
    tipo TipoItem NOT NULL,
    PRIMARY KEY(id)
);

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

CREATE TABLE item_fabricavel(
    id INTEGER NOT NULL,
    tipo TipoItemFabricavel NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES item(id)
);

CREATE TABLE item_nao_fabricavel(
    id INTEGER NOT NULL,
    tipo TipoItemNaoFabricavel NOT NULL,
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

CREATE TABLE comida(
    id INTEGER NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    tamanho SMALLINT NOT NULL DEFAULT 1,
    descricao TEXT NOT NULL,
    raridade SMALLINT NOT NULL DEFAULT 0 CHECK (raridade BETWEEN 0 AND 2),
    quantidade SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
);

CREATE TABLE medicamento(
    id INTEGER NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    tamanho SMALLINT NOT NULL DEFAULT 1, 
    descricao TEXT NOT NULL,
    raridade SMALLINT NOT NULL DEFAULT 0 CHECK (raridade BETWEEN 0 AND 2),
    cura SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
);

CREATE TABLE utilizavel(
    id INTEGER NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    tamanho SMALLINT NOT NULL DEFAULT 1, 
    descricao TEXT NOT NULL,
    raridade SMALLINT NOT NULL DEFAULT 0 CHECK (raridade BETWEEN 0 AND 2),
    quantidade SMALLINT NOT NULL DEFAULT 1,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES item_nao_fabricavel(id)
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

CREATE TABLE missao(
    id SERIAL NOT NULL,
    item_nao_fabricavel INTEGER NOT NULL,
    lugar INTEGER NOT NULL,
    regiao INTEGER NOT NULL,
    nome CHAR(25) NOT NULL UNIQUE,
    descricao TEXT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (item_nao_fabricavel) REFERENCES item_nao_fabricavel(id),
    FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao)
);

CREATE TABLE prisioneiro(
    id INTEGER NOT NULL,
    lugar INTEGER NOT NULL,
    regiao INTEGER NOT NULL,
    nome CHAR(60) NOT NULL,
    habilidade_briga SMALLINT NOT NULL CHECK (habilidade_briga BETWEEN 1 AND 10),
    vida SMALLINT NOT NULL CHECK (vida BETWEEN 1 AND 10),
    forca SMALLINT NOT NULL CHECK (forca BETWEEN 1 AND 10),
    gangue TipoGangue NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES pessoa(id),
    FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao)
);

CREATE TABLE jogador(
    id INTEGER NOT NULL,
    lugar INTEGER NOT NULL,
    regiao INTEGER NOT NULL,
    missao INTEGER NOT NULL,
    nome CHAR(60) NOT NULL,
    habilidade_briga SMALLINT NOT NULL CHECK (habilidade_briga BETWEEN 1 AND 10),
    vida SMALLINT NOT NULL CHECK (vida BETWEEN 1 AND 10),
    forca SMALLINT NOT NULL CHECK (forca BETWEEN 1 AND 10),
    tempo_vida SMALLINT NOT NULL CHECK (tempo_vida BETWEEN 1 AND 10),
    gangue TipoGangue NOT NULL,
    nivel SMALLINT NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES pessoa(id),
    FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao),
    FOREIGN KEY (missao) REFERENCES missao(id)
);

CREATE TABLE informante(
    id INTEGER NOT NULL,
    lugar INTEGER NOT NULL,
    regiao INTEGER NOT NULL,
    nome CHAR(60) NOT NULL,
    dano SMALLINT NOT NULL DEFAULT 200,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES pessoa(id),
    FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao)
);

CREATE TABLE policial(
    id INTEGER NOT NULL,
    lugar INTEGER NOT NULL,
    regiao INTEGER NOT NULL,
    nome CHAR(60) NOT NULL,
    corrupto BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (id) REFERENCES pessoa(id),
    FOREIGN KEY (lugar, regiao) REFERENCES lugar(id, regiao)
);

COMMIT;
```

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