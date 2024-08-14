<center>

# Linguagem de Consulta de Dados - DQL

</center>

---
<Center>

# O que é?

</center>

> DQL é um subconjunto de SQL (Structured Query Language) usado para consultar e recuperar dados armazenados em um banco de dados. Com o DQL, é possível buscar, filtrar e organizar informações sem alterar os dados.

---
<center>

# Pessoa

</center>

* Ver o tipo de uma pessoa.

```sql

CÓDIGO AQUI

```

> Perguntar se o id de pessoa vai buscar diretamente os detalhes de uma pessoa x em multiplas tabelas.

---
<center>

# Inventário

</center>

* Acessar o inventario de qualquer pessoa (tamanho_ocupado... todos os atributos).

```sql

CÓDIGO AQUI

```

* Ver os itens do inventario de qualquer pessoa.

```sql

CÓDIGO AQUI

```

> Perguntar se coloca um JOIN aqui.

---
<center>

# Jogador

</center>

* Ver (habilidade_briga, vida e força) de um jogador X.

```sql

CÓDIGO AQUI

```

* Ver (nome, tempo_vida, gangue e nivel) de um jogador X.

```sql

CÓDIGO AQUI

```

* Buscar missão de um jogador. (JOIN)

```sql

CÓDIGO AQUI

```

* Buscar Lugar de um jogador. (JOIN)

```sql

CÓDIGO AQUI

```

---
<center>

# Informante

</center>

* Ver o nome do informante.

```sql

CÓDIGO AQUI

```

---

<center>

# Policial

</center>

* Ver quais policiais são corruptos.

```sql

CÓDIGO AQUI

```

* Ver estatisticas de um policial X.

```sql

CÓDIGO AQUI

```

---
<center>

# Prisioneiro

</center>

* Ver quais Prisioneiro estão em uma gangue X.

```sql

CÓDIGO AQUI

```

* Ver (habilidade_briga, vida e forca) de um prisioneiro X.

```sql

CÓDIGO AQUI

```

* Ver nome de um prisioneiro X.

```sql

CÓDIGO AQUI

```

---
<center>

# Prisao

</center>

* Ver (nome, descricao, motim) de uma prisão X.

```sql

CÓDIGO AQUI

```

---
<center>

# Região

</center>

* Ver (nome, descricao) de uma região X.

```sql

CÓDIGO AQUI

```

---
<center>

# Lugar

</center>

* Ver todas as conexões de um lugar X.

```sql

CÓDIGO AQUI

```

* Ver quais pessoas estão em um lugar X.

```sql

CÓDIGO AQUI

```

* Ver quais itens estão em um lugar X.

```sql

CÓDIGO AQUI

```
---

<center>

# Fabricação

</center>

* Ver uma fabricação especifica.

```sql
SELECT (item) FROM lista_fabricacao
WHERE fabricacao = 1;
```

* Ver fabricações possiveis com um item especifico.

```sql
SELECT (item_fabricavel) FROM lista_fabricacao
WHERE item = 20;
```

* Ver todas as fabricações de um livro. (1)

```sql
SELECT * FROM fabricacao
WHERE livro_fabricacao = 2;
```

---
<center>

# Missão

</center>

* Ver o item que uma missao vai dar.

```sql

CÓDIGO AQUI

```

* Ver o lugar que uma missao está.

```sql

CÓDIGO AQUI

```

* Ver o (nome, descrição) de uma missão.

```sql

CÓDIGO AQUI

```

---
<center>

# Item

</center>

* Ver o tipo de um item especifico.

```sql
SELECT tipo FROM item
WHERE id = 1;
```

---
<center>

# Item_Fabricavel

</center>

* Ver o tipo do item fabricavel especifico.

```sql
SELECT tipo FROM item_fabricavel
WHERE id = 1;
```

---
<center>

# Item_Não_Fabricavel

</center>

* Ver o tipo do item não fabricavel especifico.

```sql

CÓDIGO AQUI

```

---
<center>

# Arma

</center>

* Ver os atributos de arma.

```sql
SELECT nome, tamanho, descricao, dano FROM arma
WHERE id = 8;
```

---
<center>

# Ferramenta

</center>

* Ver os atributos de ferramenta.

```sql
SELECT nome, tamanho, descricao, utilidade FROM ferramenta
WHERE id = 2;
```

---
<center>

# Comida

</center>

* Ver os atributos de comida.

```sql

CÓDIGO AQUI

```

---
<center>

# Medicamento

</center>

* Ver os atributos de medicamento.

```sql

CÓDIGO AQUI

```

---
<center>

# Utilizavel

</center>

* Ver os atributos de utilizavel.

```sql

CÓDIGO AQUI

```

---
<center>

# Instancia_item

</center>

?????

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição             | Autores                                          |
|:----------:|:------:|-----------------------|--------------------------------------------------|
| 28/07/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |

</div>