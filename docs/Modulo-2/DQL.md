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
SELECT tipo
FROM Pessoa
WHERE id = 3;
```

> Perguntar se o id de pessoa vai buscar diretamente os detalhes de uma pessoa x em multiplas tabelas.

---
<center>

# Inventário

</center>

* Acessar o inventario de qualquer pessoa (tamanho_ocupado... todos os atributos).

```sql
SELECT pessoa, tamanho, inventario_ocupado
FROM Inventario
WHERE pessoa = 2;
```

* Ver os itens do inventario de qualquer pessoa.

```sql
SELECT item 
FROM instancia_item
WHERE inventario = 2;

---

SELECT t.item, COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome) AS nome
FROM instancia_item t
LEFT JOIN arma a 
ON a.id = t.item
LEFT JOIN ferramenta f 
ON f.id = t.item
LEFT JOIN comida c 
ON c.id = t.item
LEFT JOIN medicamento m 
ON m.id = t.item
LEFT JOIN utilizavel u 
ON u.id = t.item
WHERE t.inventario = 2;
```

> Perguntar se coloca um JOIN aqui.

---
<center>

# Jogador

</center>

* Ver (habilidade_briga, vida e força) de um jogador X.

```sql
SELECT habilidade_briga, vida, forca
FROM Jogador
WHERE id = 1;
```

* Ver (nome, tempo_vida, gangue e nivel) de um jogador X.

```sql
SELECT nome, tempo_vida, gangue, nivel
FROM Jogador
WHERE id = 1;
```

* Buscar missão de um jogador. (JOIN)

```sql
SELECT j.nome, m.nome, m.descricao
FROM jogador j
LEFT JOIN missao m 
ON j.missao = m.id
WHERE j.id = 1;
```

* Buscar Lugar de um jogador. (JOIN)

```sql
SELECT l.nome, l.descricao
FROM Jogador j
LEFT JOIN lugar l
ON l.id = j.lugar
WHERE j.id = 1;
```

---
<center>

# Informante

</center>

* Ver o nome do informante.

```sql
SELECT nome
FROM Informante
WHERE id = 19;
```

---

<center>

# Policial

</center>

* Ver quais policiais são corruptos.

```sql
SELECT nome
FROM Policial
WHERE corrupto = true;
```

* Ver estatisticas de um policial X.

```sql
SELECT nome, lugar, regiao, corrupto
FROM Policial
WHERE id = 16;
```

---
<center>

# Prisioneiro

</center>

* Ver quais Prisioneiro estão em uma gangue X.

```sql
SELECT nome
FROM Prisioneiro
WHERE gangue = 'polvo';
```

* Ver (habilidade_briga, vida e forca) de um prisioneiro X.

```sql
SELECT habilidade_briga, vida, forca
FROM Prisioneiro
WHERE id = 3;
```

* Ver nome de um prisioneiro X.

```sql
SELECT nome
FROM Prisioneiro
WHERE id = 3;
```

---
<center>

# Prisão

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

---

SELECT u.nome
FROM lista_fabricacao t
LEFT JOIN utilizavel u 
ON u.id = t.item
WHERE t.fabricacao = 1;
```

> Inspiração:

<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei2.png?raw=true"/>
</div>


* Ver fabricações possiveis com um item especifico.

```sql
SELECT (item_fabricavel) FROM lista_fabricacao
WHERE item = 20;

---

SELECT COALESCE(a.nome, f.nome) AS nome
FROM lista_fabricacao l
LEFT JOIN arma a
ON a.id = l.fabricacao
LEFT JOIN ferramenta f
on f.id = l.fabricacao
WHERE l.item = 20;

```

> Inspiração:

<center>
<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei1.gif?raw=true"/>
</div>

</center>


* Ver todas as fabricações de um livro. 

```sql
SELECT * FROM fabricacao
WHERE livro_fabricacao = 2;

---

SELECT COALESCE(a.nome, f.nome) AS nome
FROM fabricacao l
LEFT JOIN arma a
ON a.id = l.item_fabricavel
LEFT JOIN ferramenta f
on f.id = l.item_fabricavel
WHERE l.livro_fabricacao = 2;
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

```sql  (junção de nome e id da missão com o nome do lugar )

SELECT  m.id, m.nome, l.nome
FROM missao m
LEFT JOIN lugar l 
ON m.lugar = l.id
ORDER BY m.id;

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
SELECT tipo 
FROM item
WHERE id = 1;
```

---
<center>

# Item_Fabricavel

</center>

* Ver o tipo do item fabricavel especifico.

```sql
SELECT tipo 
FROM item_fabricavel
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
SELECT nome, tamanho, descricao, dano 
FROM arma
WHERE id = 8;
```

---
<center>

# Ferramenta

</center>

* Ver os atributos de ferramenta.

```sql
SELECT nome, tamanho, descricao, utilidade 
FROM ferramenta
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
| :--------: | :----: | --------------------- | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento. | [João Antonio G.](https://github.com/joaoseisei) |
| 14/08/2024 | `1.1`  | adiciona dql pessoa   | [Júlio Cesar](https://github.com/Julio1099)      |

</div>