<center>

# Linguagem de Definição de Dados - DDL

</center>

---

> O que é?

```s

CREATE TABLE PEDIDOS(
	cod_ped SERIAL PRIMARY KEY,
	cod_cliente INT NOT NULL REFERENCES clientes(cod_cliente),
	cod_prod INT NOT NULL,
	qtd SMALLINT NOT NULL,
	FOREIGN KEY (cod_prod) REFERENCES produtos(cod_prod)
);

```

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição             | Autores                                          |
|:----------:|:------:|-----------------------|--------------------------------------------------|
| 28/07/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |

</div>