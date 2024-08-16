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
\pi_{\text{jog.nome}, \text{mis.nome}, \text{mis.descricao}} \left( \sigma_{\text{j.id} = 1} \left( \text{jogador} \bowtie \text{missao} \right) \right)
$$

## Buscar Lugar de um jogador. (JOIN)

$$
\pi_{\text{lug.nome}, \text{lug.descricao}} \left( \sigma_{\text{jog.id} = 1} \left( \text{Jogador} \bowtie \text{lugar} \right) \right)
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
\tau_{lug.nome} \left( \pi_{lug.nome, reg.nome} \left( \sigma_{ori.lugar\_origem = 10} \left( (\text{lugar\_origem\_destino} \bowtie_{o.lugar\_destino = lug.id} \text{lugar}) \bowtie_{lug.regiao = reg.id} \text{regiao} \right) \right) \right)
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
\tau_{\text{COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome)}} \left( \pi_{t.item, \text{COALESCE(arm.nome, fer.nome, com.nome, med.nome, uti.nome)} \rightarrow \text{nome}} \left( \sigma_{lis.fabricacao = 12} \left( \text{lista\_fabricacao} \bowtie_{arm.id = lis.item} \text{arma} \bowtie_{fer.id = lis.item} \text{ferramenta} \bowtie_{com.id = lis.item} \text{comida} \bowtie_{med.id = lis.item} \text{medicamento} \bowtie_{uti.id = lis.item} \text{utilizavel} \right) \right) \right)
$$


## Ver fabricações possiveis com um item especifico.

$$
\tau_{\text{COALESCE(arm.nome, fer.nome)}} \left( \pi_{\text{COALESCE(arm.nome, fer.nome)} \rightarrow \text{nome}} \left( \sigma_{lis.item = 20} \left( \text{lista\_fabricacao} \bowtie_{lis.fabricacao = arm.id} \text{arma} \bowtie_{lis.fabricacao = fer.id} \text{ferramenta} \right) \right) \right)
$$


## Ver todas as fabricações de um livro. 

$$
\tau_{\text{COALESCE(arm.nome, fer.nome)}} \left( \pi_{\text{COALESCE(arm.nome, fer.nome)} \rightarrow \text{nome}} \left( \sigma_{fab.livro\_fabricacao = 2} \left( \text{fabricacao} \bowtie_{fab.item\_fabricavel = arm.id} \text{arma} \bowtie_{fab.item\_fabricavel = fer.id} \text{ferramenta} \right) \right) \right)
$$

---
<center>

# Missao

</center>

## Ver o item que uma missao vai dar.

$$
\pi_{\text{COALESCE(com.nome, uti.nome, med.nome)} \rightarrow \text{nome}, \text{COALESCE(com.descricao, uti.descricao, med.descricao)} \rightarrow \text{descricao}} \left( \sigma_{mis.id = 1} \left( \text{missao} \bowtie_{mis.item\_nao\_fabricavel = com.id} \text{comida} \bowtie_{mis.item\_nao\_fabricavel = uti.id} \text{utilizavel} \bowtie_{mis.item\_nao\_fabricavel = med.id} \text{medicamento} \right) \right)
$$

## Ver o lugar que uma missao está.

$$
\pi_{\text{lugar.nome}, \text{lugar.descricao}} \left( \sigma_{\text{missao.id} = 2} \left( \text{missao} \bowtie_{\text{missao.lugar} = \text{lugar.id}} \text{lugar} \right) \right)
$$

## Ver o (nome, descrição) de uma missão.

$$
\pi_{\text{nome}, \text{descricao}} \left( \sigma_{\text{id} = 3} \left( \text{missao} \right) \right)
$$

---
<center>

# Item

</center>

## Ver o tipo de um item especifico.

$$
\pi_{\text{tipo}} \left( \sigma_{\text{id} = 1} \left( \text{item} \right) \right)
$$

---
<center>

# Item_Fabricavel

</center>

## Ver o tipo do item fabricavel especifico.

$$
\pi_{\text{tipo}} \left( \sigma_{\text{id} = 1} \left( \text{item\_fabricavel} \right) \right)
$$

---
<center>

# Item_Não_Fabricavel

</center>

## Ver o id, o tipo do item e o seu nome especifico.

$$
\pi_{\text{tipo}} \left( \sigma_{\text{id} = 17} \left( \text{item\_nao\_fabricavel} \right) \right)
$$

---
<center>

# Arma

</center>

## Ver os atributos de arma.

$$
\pi_{\text{nome}, \text{tamanho}, \text{descricao}, \text{dano}} \left( \sigma_{\text{id} = 8} \left( \text{arma} \right) \right)
$$

---
<center>

# Ferramenta

</center>

## Ver os atributos de ferramenta.

$$
\pi_{\text{nome}, \text{tamanho}, \text{descricao}, \text{utilidade}} \left( \sigma_{\text{id} = 2} \left( \text{ferramenta} \right) \right)
$$

---
<center>

# Comida

</center>

## Ver os atributos de comida.

$$
\pi_{\text{nome}, \text{tamanho}, \text{descricao}, \text{raridade}, \text{quantidade}, \text{recuperacao\_vida}} \left( \sigma_{\text{id} = 32} \left( \text{comida} \right) \right)
$$

---
<center>

# Medicamento

</center>

## Ver os atributos de medicamento.

$$
\pi_{\text{nome}, \text{tamanho}, \text{descricao}, \text{raridade}, \text{cura}, \text{quantidade}} \left( \sigma_{\text{id} = 29} \left( \text{medicamento} \right) \right)
$$

---
<center>

# Utilizavel

</center>

## Ver os atributos de utilizavel.

$$
\pi_{\text{nome}, \text{tamanho}, \text{descricao}, \text{raridade}, \text{quantidade}, \text{durabilidade}} \left( \sigma_{\text{ID} = 18} \left( \text{utilizavel} \right) \right)
$$

---
<center>

# Instancia_item

</center>

$$
\pi_{\text{ins.inventario}, \text{inv.inventario\_ocupado}, \text{tamanho\_calculado}} \left( \sigma_{\text{inv.inventario\_ocupado} \neq \text{tamanho\_calculado}} \left( \gamma_{\text{t.inventario}, \text{inv.inventario\_ocupado}; \text{tamanho\_calculado} = \text{SUM(COALESCE(arm.tamanho, fer.tamanho, com.tamanho, med.tamanho, uti.tamanho))}} \left( (\text{instancia\_item} \bowtie_{\text{ins.item} = \text{arm.id}} \text{arma}) \bowtie_{\text{ins.item} = \text{fer.id}} \text{ferramenta} \bowtie_{\text{ins.item} = \text{com.id}} \text{comida} \bowtie_{\text{ins.item} = \text{med.id}} \text{medicamento} \bowtie_{\text{ins.item} = \text{uti.id}} \text{utilizavel} \bowtie_{\text{ins.inventario} = \text{inv.id}} \text{inventario} \right) \right) \right)
$$

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                 | Autores                                          |
| :--------: | :----: | ------------------------- | ------------------------------------------------ |
| 28/07/2024 | `1.0`  | Criação do documento.     | [João Antonio G.](https://github.com/joaoseisei) |
| 14/08/2024 | `1.1`  | Atualização do documento. | [Júlio Cesar](https://github.com/Julio1099)      |
| 15/08/2024 | `1.2`  | Adição de novos itens.    | [Júlio Cesar](https://github.com/Julio1099)      |
| 16/08/2024 | `1.3`  | Adição de nova formatação.    | [Júlio Cesar](https://github.com/Julio1099)      |

</div>