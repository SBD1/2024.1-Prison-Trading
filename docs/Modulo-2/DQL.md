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
SELECT t.item, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM instancia_item t
LEFT JOIN arma arm
ON arm.id = t.item
LEFT JOIN ferramenta fer
ON fer.id = t.item
LEFT JOIN comida com
ON com.id = t.item
LEFT JOIN medicamento med
ON med.id = t.item
LEFT JOIN utilizavel uti
ON uti.id = t.item
WHERE t.inventario = 2
ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);
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
SELECT jog.nome, mis.nome, mis.descricao
FROM jogador jog
LEFT JOIN missao mis 
ON jog.missao = mis.id
WHERE jog.id = 1;
```

* Buscar Lugar de um jogador. 

```sql
SELECT lug.nome, lug.descricao
FROM jogador jog
LEFT JOIN lugar lug
ON lug.id = jog.lugar
WHERE jog.id = 1;
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
SELECT lug.nome, reg.nome
FROM lugar_origem_destino ori
JOIN lugar lug
ON ori.lugar_destino = lug.id
JOIN regiao reg
ON lug.regiao = reg.id
WHERE ori.lugar_origem = 10
ORDER BY lug.nome;
```

* Ver quais pessoas estão em um lugar X.

```sql
WITH Pessoas AS (
    SELECT id, nome, lugar FROM jogador
    UNION ALL
    SELECT id, nome, lugar FROM policial
    UNION ALL
    SELECT id, nome, lugar FROM prisioneiro
    UNION ALL
    SELECT id, nome, lugar FROM informante
)
SELECT pes.nome, tip.tipo
FROM pessoas pes, pessoa tip
WHERE pes.id = tip.id AND pes.lugar = 22
ORDER BY tip.tipo, pes.nome;
```

* Ver quais itens estão em um lugar X.

```sql
SELECT COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM instancia_item ins
LEFT JOIN arma arm 
ON arm.id = ins.item
LEFT JOIN ferramenta fer 
ON fer.id = ins.item
LEFT JOIN comida com 
ON com.id = ins.item
LEFT JOIN medicamento med 
ON med.id = ins.item
LEFT JOIN utilizavel uti 
ON uti.id = ins.item
WHERE ins.lugar = 11
ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);
```
---

<center>

# Fabricaçao

</center>

* Ver uma fabricação específica.

```sql
SELECT lis.item, COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome) AS nome
FROM lista_fabricacao lis
LEFT JOIN arma arm 
ON arm.id = lis.item
LEFT JOIN ferramenta fer 
ON fer.id = lis.item
LEFT JOIN comida com 
ON com.id = lis.item
LEFT JOIN medicamento med 
ON med.id = lis.item
LEFT JOIN utilizavel uti 
ON uti.id = lis.item
WHERE lis.fabricacao = 12
ORDER BY COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome);
```

> Inspiração:

<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei2.png?raw=true"/>
</div>


* Ver fabricações possiveis com um item específico.

```sql
SELECT COALESCE(arm.nome, fer.nome) AS nome
FROM lista_fabricacao lis
LEFT JOIN arma arm
ON arm.id = lis.fabricacao
LEFT JOIN ferramenta fer
ON fer.id = lis.fabricacao
WHERE lis.item = 20
ORDER BY COALESCE(arm.nome, fer.nome);
```

> Inspiração:

<center>
<div align="center">
    <img style="width: 25vw;" src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/random/jei1.gif?raw=true"/>
</div>

</center>


* Ver todas as fabricações de um livro específico. 

```sql
SELECT COALESCE(arm.nome, fer.nome) AS nome
FROM fabricacao fab
LEFT JOIN arma arm
ON arm.id = fab.item_fabricavel
LEFT JOIN ferramenta fer
ON fer.id = fab.item_fabricavel
WHERE fab.livro_fabricacao = 2
ORDER BY COALESCE(arm.nome, fer.nome);
```

---
<center>

# Missão

</center>

* Ver o item que uma missão X vai dar.

```sql
SELECT COALESCE(com.nome, uti.nome, med.nome) AS nome, COALESCE(com.descricao, uti.descricao, med.descricao) AS descricao
FROM missao mis
LEFT JOIN comida com
ON mis.item_nao_fabricavel = com.id
LEFT JOIN utilizavel uti
ON mis.item_nao_fabricavel = uti.id
LEFT JOIN medicamento med
ON mis.item_nao_fabricavel = med.id
WHERE mis.id = 1;
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
SELECT ins.inventario, inv.inventario_ocupado, SUM(COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho)) AS tamanho_calculado
FROM instancia_item ins
LEFT JOIN arma arm 
ON arm.id = ins.item
LEFT JOIN ferramenta fer 
ON fer.id = ins.item
LEFT JOIN comida com 
ON com.id = ins.item
LEFT JOIN medicamento med 
ON med.id = ins.item
LEFT JOIN utilizavel uti 
ON uti.id = ins.item
LEFT JOIN inventario inv
ON ins.inventario = inv.id
GROUP BY ins.inventario, inv.inventario_ocupado
HAVING inv.inventario_ocupado != SUM(COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho))
ORDER BY ins.inventario;
```

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                   | Autores                                          |
| :--------: | :----: | --------------------------- | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.       | [João Antonio G.](https://github.com/joaoseisei) |
| 14/08/2024 | `1.1`  | adiciona dql Julio         | [Júlio Cesar](https://github.com/Julio1099)      |
| 14/08/2024 | `1.2`  | adiciona dql parte fernando | [Fernando Gabriel](https://github.com/show-dawn) |
| 16/08/2024 | `1.3`  | Formatação dql Julio         | [Júlio Cesar](https://github.com/Julio1099)      |

</div>
