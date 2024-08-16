<center>

# Álgebra Relacional

</center>

---

> Álgebra relacional é um conjunto de operações matemáticas que manipulam e consultam dados em bancos de dados relacionais, servindo como base teórica para operações em tabelas e extração sistemática de informações.

---

<center>

# Pessoa

</center>

* Ver o tipo de uma pessoa.

$$
\pi_{\text{tipo}} \left( \sigma_{\text{id} = 3} (\text{Pessoa}) \right)
$$

---
<center>

# Inventario

## Acessar o inventario de qualquer pessoa (tamanho_ocupado... todos os atributos).

$$
\pi_{\text{pessoa}, \text{tamanho}, \text{inventario\_ocupado}} \left( \sigma_{\text{pessoa} = 2} (\text{Inventario}) \right)
$$

## Ver os itens do inventário de qualquer pessoa.

$$
\pi_{\text{item}} \left( \sigma_{\text{inventario} = 2} (\text{instancia\_item}) \right)
$$

---

$$
\pi_{t.\text{item}, \text{nome}} \left( \sigma_{t.\text{inventario} = 2} \left( \text{instancia\_item} \bowtie \left( \text{arma} \cup \text{ferramenta} \cup \text{comida} \cup \text{medicamento} \cup \text{utilizavel} \right) \right) \right)
$$

---

# Jogador

## Ver (habilidade_briga, vida e força) de um jogador X.

$$
\pi_{\text{habilidade\_briga}, \text{vida}, \text{forca}} \left( \sigma_{\text{id} = 1} (\text{Jogador}) \right)
$$

## Ver (nome, tempo_vida, gangue e nivel) de um jogador X.

$$
\pi_{\text{nome}, \text{tempo\_vida}, \text{gangue}, \text{nivel}} \left( \sigma_{\text{id} = 1} (\text{Jogador}) \right)
$$

## Buscar missão de um jogador. (JOIN)

$$
\pi_{\text{j.nome}, \text{m.nome}, \text{m.descricao}} \left( \sigma_{\text{j.id} = 1} \left( \text{jogador} \bowtie \text{missao} \right) \right)
$$

## Buscar Lugar de um jogador. (JOIN)

$$
\pi_{\text{l.nome}, \text{l.descricao}} \left( \sigma_{\text{j.id} = 1} \left( \text{Jogador} \bowtie \text{lugar} \right) \right)
$$

---
<center>

# Informante

</center>

## Ver o nome do informante.

$$
\pi_{\text{nome}} \left( \sigma_{\text{id} = 19} (\text{Informante}) \right)
$$

---

<center>

# Policial

</center>

## Ver quais policiais são corruptos.

$$
\pi_{\text{nome}} \left( \sigma_{\text{corrupto} = \text{true}} (\text{Policial}) \right)
$$

## Ver estatisticas de um policial X.

$$
\pi_{\text{nome}, \text{lugar}, \text{regiao}, \text{corrupto}} \left( \sigma_{\text{id} = 16} (\text{Policial}) \right)
$$

---
<center>

# Prisioneiro

</center>

## Ver quais Prisioneiro estão em uma gangue X.

$$
\pi_{\text{nome}} \left( \sigma_{\text{gangue} = 'polvo'} (\text{Prisioneiro}) \right)
$$

## Ver (habilidade_briga, vida e forca) de um prisioneiro X.

$$
\pi_{\text{habilidade\_briga}, \text{vida}, \text{forca}} \left( \sigma_{\text{id} = 3} (\text{Prisioneiro}) \right)
$$


## Ver nome de um prisioneiro X.

$$
\pi_{\text{nome}} \left( \sigma_{\text{id} = 3} (\text{Prisioneiro}) \right)
$$

---
<center>

# Prisao

</center>

## Ver (nome, descricao, motim) de uma prisão X.

$$
\pi_{\text{nome}, \text{descricao}, \text{motim}} \left( \sigma_{\text{id} = 1} (\text{Prisao}) \right)
$$

---
<center>

# Regiao

$$
\pi_{\text{nome}, \text{descricao}} \left( \sigma_{\text{id} = 6} (\text{regiao}) \right)
$$

---
<center>

# Lugar

</center>

## Ver todas as conexões de um lugar X.

$$
\tau_{l.nome} \left( \pi_{l.nome, r.nome} \left( \sigma_{o.lugar\_origem = 10} \left( (\text{lugar\_origem\_destino} \bowtie_{o.lugar\_destino = l.id} \text{lugar}) \bowtie_{l.regiao = r.id} \text{regiao} \right) \right) \right)
$$

## Ver quais pessoas estão em um lugar X.

?????

## Ver quais itens estão em um lugar X.

$$
\tau_{\text{pessoa}} \left( \pi_{\text{nome} \rightarrow \text{pessoa}} \left( \sigma_{\text{lugar} = 22} \left( \left( \pi_{\text{nome}, \text{lugar}} (\text{jogador}) \right) \cup \left( \pi_{\text{nome}, \text{lugar}} (\text{policial}) \right) \cup \left( \pi_{\text{nome}, \text{lugar}} (\text{prisioneiro}) \right) \cup \left( \pi_{\text{nome}, \text{lugar}} (\text{informante}) \right) \right) \right) \right)
$$
---

<center>

# Fabricaçao

</center>

## Ver uma fabricação especifica.

$$
\tau_{\text{COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome)}} \left( \pi_{t.item, \text{COALESCE(a.nome, f.nome, c.nome, m.nome, u.nome)} \rightarrow \text{nome}} \left( \sigma_{t.fabricacao = 12} \left( \text{lista\_fabricacao} \bowtie_{a.id = t.item} \text{arma} \bowtie_{f.id = t.item} \text{ferramenta} \bowtie_{c.id = t.item} \text{comida} \bowtie_{m.id = t.item} \text{medicamento} \bowtie_{u.id = t.item} \text{utilizavel} \right) \right) \right)
$$


## Ver fabricações possiveis com um item especifico.

$$
\tau_{\text{COALESCE(a.nome, f.nome)}} \left( \pi_{\text{COALESCE(a.nome, f.nome)} \rightarrow \text{nome}} \left( \sigma_{l.item = 20} \left( \text{lista\_fabricacao} \bowtie_{l.fabricacao = a.id} \text{arma} \bowtie_{l.fabricacao = f.id} \text{ferramenta} \right) \right) \right)
$$


## Ver todas as fabricações de um livro. 

$$
\tau_{\text{COALESCE(a.nome, f.nome)}} \left( \pi_{\text{COALESCE(a.nome, f.nome)} \rightarrow \text{nome}} \left( \sigma_{l.livro\_fabricacao = 2} \left( \text{fabricacao} \bowtie_{l.item\_fabricavel = a.id} \text{arma} \bowtie_{l.item\_fabricavel = f.id} \text{ferramenta} \right) \right) \right)
$$

---
<center>

# Missao

</center>

## Ver o item que uma missao vai dar.

?????

## Ver o lugar que uma missao está.

?????

## Ver o (nome, descrição) de uma missão.

?????

---
<center>

# Item

</center>

## Ver o tipo de um item especifico.

?????

---
<center>

# Item_Fabricavel

</center>

## Ver o tipo do item fabricavel especifico.

?????

---
<center>

# Item_Não_Fabricavel

</center>

## Ver o id, o tipo do item e o seu nome especifico.

?????

---
<center>

# Arma

</center>

## Ver os atributos de arma.

?????

---
<center>

# Ferramenta

</center>

## Ver os atributos de ferramenta.

?????

---
<center>

# Comida

</center>

## Ver os atributos de comida.

?????

---
<center>

# Medicamento

</center>

## Ver os atributos de medicamento.

?????
---
<center>

# Utilizavel

</center>

## Ver os atributos de utilizavel.

?????

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
| 14/08/2024 | `1.1`  | Atualização do documento. | [Júlio Cesar](https://github.com/Julio1099) |

</div>