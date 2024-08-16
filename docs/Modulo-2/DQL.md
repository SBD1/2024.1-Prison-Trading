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
FROM pessoa
WHERE id = 3;
```

---
<center>

# Inventario

</center>

* Acessar o inventario de uma pessoa X e ver os atributos (pessoa, tamanho e inventario_ocupado).

```sql
SELECT pessoa, tamanho, inventario_ocupado
FROM inventario
WHERE pessoa = 2;
```

* Ver os itens do inventario de uma pessoa X.

```sql
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
WHERE t.inventario = 2
ORDER BY COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome);
```

---
<center>

# Jogador

</center>

* Ver (habilidade_briga, vida e força) de um jogador X.

```sql
SELECT habilidade_briga, vida, forca
FROM jogador
WHERE id = 1;
```

* Ver (nome, tempo_vida, gangue e nivel) de um jogador X.

```sql
SELECT nome, tempo_vida, gangue, nivel
FROM jogador
WHERE id = 1;
```

* Buscar missão de um jogador. 

```sql
SELECT j.nome, m.nome, m.descricao
FROM jogador j
LEFT JOIN missao m 
ON j.missao = m.id
WHERE j.id = 1;
```

* Buscar Lugar de um jogador. 

```sql
SELECT l.nome, l.descricao
FROM jogador j
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
FROM informante
WHERE id = 19;
```

---

<center>

# Policial

</center>

* Ver quais policiais são corruptos.

```sql
SELECT nome
FROM policial
WHERE corrupto = true;
```

* Ver estatisticas de um policial X.

```sql
SELECT nome, lugar, regiao, corrupto
FROM policial
WHERE id = 16;
```

---
<center>

# Prisioneiro

</center>

* Ver quais Prisioneiro estão em uma gangue X.

```sql
SELECT nome
FROM prisioneiro
WHERE gangue = 'polvo';
```

* Ver (habilidade_briga, vida e forca) de um prisioneiro X.

```sql
SELECT habilidade_briga, vida, forca
FROM prisioneiro
WHERE id = 3;
```

* Ver nome de um prisioneiro X.

```sql
SELECT nome
FROM prisioneiro
WHERE id = 3;
```

---
<center>

# Prisao

</center>

* Ver (nome, descricao, motim) de uma prisão X.

```sql
SELECT nome, descricao, motim
FROM prisao
WHERE id = 1;
```

---
<center>

# Regiao

</center>

* Ver (nome, descricao) de uma região X.

```sql
SELECT nome, descricao
FROM regiao
WHERE id = 6;
```

---
<center>

# Lugar

</center>

* Ver todas as conexões de um lugar X.

```sql
SELECT l.nome, r.nome
FROM lugar_origem_destino o
JOIN lugar l
ON o.lugar_destino = l.id
JOIN regiao r
ON l.regiao = r.id
WHERE o.lugar_origem = 10
ORDER BY l.nome;
```

* Ver quais pessoas estão em um lugar X.

```sql
WITH Pessoas AS (
    SELECT nome, lugar FROM jogador
    UNION ALL
    SELECT nome, lugar FROM policial
    UNION ALL
    SELECT nome, lugar FROM prisioneiro
    UNION ALL
    SELECT nome, lugar FROM informante
)
SELECT nome AS pessoa
FROM Pessoas
WHERE lugar = 22
ORDER BY pessoa;

---

SELECT nome AS pessoa
FROM (
    SELECT nome FROM jogador WHERE lugar = 22
    UNION ALL
    SELECT nome FROM policial WHERE lugar = 22
    UNION ALL
    SELECT nome FROM prisioneiro WHERE lugar = 22
    UNION ALL
    SELECT nome FROM informante WHERE lugar = 22
) AS pessoas
ORDER BY pessoa;

----

SELECT jog.nome AS pessoa
FROM jogador jog
WHERE jog.lugar = 22

UNION ALL

SELECT pol.nome AS pessoa
FROM policial pol
WHERE pol.lugar = 22

UNION ALL

SELECT pri.nome AS pessoa
FROM prisioneiro pri
WHERE pri.lugar = 22

UNION ALL

SELECT inf.nome AS pessoa
FROM informante inf
WHERE inf.lugar = 22

ORDER BY pessoa;
```

* Ver quais itens estão em um lugar X.

```sql
SELECT COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome) AS nome
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
WHERE t.lugar = 11
ORDER BY COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome);
```
---

<center>

# Fabricaçao

</center>

* Ver uma fabricação específica.

```sql
SELECT t.item, COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome) AS nome
FROM lista_fabricacao t
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
WHERE t.fabricacao = 12
ORDER BY COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome);
```

> Inspiração:

<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei2.png?raw=true"/>
</div>


* Ver fabricações possiveis com um item específico.

```sql
SELECT COALESCE(a.nome, f.nome) AS nome
FROM lista_fabricacao l
LEFT JOIN arma a
ON a.id = l.fabricacao
LEFT JOIN ferramenta f
on f.id = l.fabricacao
WHERE l.item = 20
ORDER BY COALESCE(a.nome, f.nome);
```

> Inspiração:

<center>
<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei1.gif?raw=true"/>
</div>

</center>


* Ver todas as fabricações de um livro específico. 

```sql
SELECT COALESCE(a.nome, f.nome) AS nome
FROM fabricacao l
LEFT JOIN arma a
ON a.id = l.item_fabricavel
LEFT JOIN ferramenta f
on f.id = l.item_fabricavel
WHERE l.livro_fabricacao = 2
ORDER BY COALESCE(a.nome, f.nome);
```

---
<center>

# Missão

</center>

* Ver o item que uma missão X vai dar.

```sql
SELECT COALESCE(c.nome, u.nome, r.nome) AS nome, COALESCE(c.descricao, u.descricao, r.descricao) AS descricao
FROM missao m
LEFT JOIN comida c
ON m.item_nao_fabricavel = c.id
LEFT JOIN utilizavel u
ON m.item_nao_fabricavel = u.id
LEFT JOIN medicamento r
ON m.item_nao_fabricavel = r.id
WHERE m.id = 1;
```

* Ver o lugar que uma missão X está.

```sql
SELECT lugar.nome, lugar.descricao
FROM missao, lugar
WHERE missao.lugar = lugar.id AND missao.id = 2;
```

* Ver o (nome, descrição) de uma missão específica.

```sql
SELECT nome, descricao
FROM missao m
WHERE id = 3;
```

---
<center>

# Item

</center>

* Ver o tipo de um item específico.

```sql
SELECT tipo 
FROM item
WHERE id = 1;
```

---
<center>

# Item_Fabricavel

</center>

* Ver o tipo do item fabricavel específico.

```sql
SELECT tipo 
FROM item_fabricavel
WHERE id = 1;
```

---
<center>

# Item_Não_Fabricavel

</center>

* Ver o tipo do item não fabricavel e o seu nome especifico.

```sql
SELECT tipo 
FROM item_nao_fabricavel
WHERE id = 17;
```

---
<center>

# Arma

</center>

* Ver os atributos de uma arma específica.

```sql
SELECT nome, tamanho, descricao, dano 
FROM arma
WHERE id = 8;
```

---
<center>

# Ferramenta

</center>

* Ver os atributos de uma ferramenta específica.

```sql
SELECT nome, tamanho, descricao, utilidade 
FROM ferramenta
WHERE id = 2;
```

---
<center>

# Comida

</center>

* Ver os atributos de uma comida específica.

```sql
SELECT nome, tamanho, descricao, raridade, quantidade, recuperacao_vida
FROM comida
WHERE id = 32;
```

---
<center>

# Medicamento

</center>

* Ver os atributos de um medicamento específico.

```sql
SELECT nome, tamanho, descricao, raridade, cura, quantidade
FROM medicamento
WHERE id = 29;
```

---
<center>

# Utilizavel

</center>

* Ver os atributos de um utilizavel específico.

```sql
SELECT nome, tamanho, descricao, raridade, quantidade, durabilidade
FROM utilizavel
WHERE ID = 18;
```

---

<center>

# Outos

</center>

> Comando usado para verificar inconsistencias no tamanho_ocupado do inventario, optamos por usar um SUM
> ao invés de um COUNT pois itens tem tamanhos diferentes. O COALESCE foi usado para colocar todos os tamanhos em
> uma única coluna para fazermos o SUM em cima dela.
>
> O comando irá retornar tuplas que tem o tamanho_ocupado inconsistente.

```sql
SELECT t.inventario, i.inventario_ocupado, SUM(COALESCE(a.tamanho, f.tamanho, c.tamanho, m.tamanho, u.tamanho)) AS tamanho_calculado
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
LEFT JOIN inventario i
ON t.inventario = i.id
GROUP BY t.inventario, i.inventario_ocupado
HAVING i.inventario_ocupado != SUM(COALESCE(a.tamanho, f.tamanho, c.tamanho, m.tamanho, u.tamanho))
ORDER BY t.inventario;
```

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                   | Autores                                          |
| :--------: | :----: | --------------------------- | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.       | [João Antonio G.](https://github.com/joaoseisei) |
| 14/08/2024 | `1.1`  | adiciona dql pessoa         | [Júlio Cesar](https://github.com/Julio1099)      |
| 14/08/2024 | `1.2`  | adiciona dql parte fernando | [Fernando Gabriel](https://github.com/show-dawn) |


</div>
