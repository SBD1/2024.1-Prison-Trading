# Mapeamento

Esquema de Relação

---
## Item { <ins>nome</ins>, utilizavel, descricao }

Item será utilizado por pessoas para realizaçao de trocas e o mesmo faz parte do inventario de toda pessoa.

|    Nome    |                           Definição Lógica                           |  Tipo e Formato de Dado  | Restrição   |
|:----------:|:--------------------------------------------------------------------:|:------------------------:|-------------|
|    nome    |       Nome do item mencionado sem caracteres especiais (~Ç@!)        |  VARCHAR (20) a-z, A-Z   | PRIMARY KEY |
| utilizavel | Se o item é utilizável, ou apenas para troca (como cigarro ou moeda) |         BOOLEANO         | NOT NULL    |
| descricao  |            Um breve resumo da funçao do item mencionado.             | VARCHAR (150)   a-z, A-Z | NOT NULL    |

---
## Instancia_Item { <ins>nome, nome_inst, id_inventario, nome_lugar</ins> }

|      Nome       |                           Definição Lógica                           | Tipo e Formato de Dado | Restrição             |
|:---------------:|:--------------------------------------------------------------------:|:----------------------:|-----------------------|
| nome, nome_inst |       Nome do item mencionado sem caracteres especiais (~Ç@!)        | VARCHAR (20) a-z, A-Z  | PRIMARY KEY           |
|  id_inventario  |            Um breve resumo da funçao do item mencionado.             |          Int           | FOREIGN KEY, NOT NULL |
|   nome_lugar    |                                                                      | VARCHAR (25) a-z, A-Z  | FOREIGN KEY, NULL     |

> PERGUNTAR SE O NOME DE LUGAR PODE SER NULL

---
## Pessoa { <ins>id_pessoa, nome_lugar</ins>, nome_pessoa, tipo_pessoa }

|    Nome     |                           Definição Lógica                           | Tipo e Formato de Dado | Restrição             |
|:-----------:|:--------------------------------------------------------------------:|:----------------------:|-----------------------|
|  id_pessoa  |       Nome do item mencionado sem caracteres especiais (~Ç@!)        |          Int           | PRIMARY KEY           |
| nome_pessoa |            Um breve resumo da funçao do item mencionado.             | VARCHAR (60) a-z, A-Z  | NOT NULL              |
| tipo_pessoa |                                                                      |          Enum          | NOT NULL              |
| nome_lugar  | Se o item é utilizável, ou apenas para troca (como cigarro ou moeda) | VARCHAR (25) a-z, A-Z  | FOREIGN KEY, NOT NULL |

---
## Inventario { <ins>id_pessoa, id_inventario</ins> }

|           Nome           |                           Definição Lógica                           | Tipo e Formato de Dado | Restrição             |
|:------------------------:|:--------------------------------------------------------------------:|:----------------------:|-----------------------|
| id_pessoa, id_inventario |       Nome do item mencionado sem caracteres especiais (~Ç@!)        |          Int           | PRIMARY KEY           |

---
## Regiao { <ins>nome</ins>, descricao }

|    Nome     |                           Definição Lógica                           | Tipo e Formato de Dado | Restrição             |
|:-----------:|:--------------------------------------------------------------------:|:----------------------:|-----------------------|
|    nome     |       Nome do item mencionado sem caracteres especiais (~Ç@!)        | VARCHAR (15) a-z, A-Z  | PRIMARY KEY           |
|  descricao  |            Um breve resumo da funçao do item mencionado.             | VARCHAR (200) a-z, A-Z | NOT NULL              |

---
## Lugar { <ins>nome_lugar, nome_regiao</ins>, descricao_especifica, lugar_anterior }

|         Nome         |                           Definição Lógica                           | Tipo e Formato de Dado | Restrição             |
|:--------------------:|:--------------------------------------------------------------------:|:----------------------:|-----------------------|
|      nome_lugar      |       Nome do item mencionado sem caracteres especiais (~Ç@!)        | VARCHAR (25) a-z, A-Z  | PRIMARY KEY           |
| descricao_especifica |            Um breve resumo da funçao do item mencionado.             | VARCHAR (200) a-z, A-Z | NOT NULL              |
|    lugar_anterior    |                                                                      | VARCHAR (25) a-z, A-Z  | NOT NULL              |
|     nome_regiao      | Se o item é utilizável, ou apenas para troca (como cigarro ou moeda) | VARCHAR (15) a-z, A-Z  | FOREIGN KEY, NOT NULL |

[//]: # (SUBLINHADO <ins>aaaaa</ins>)
[//]: # (SUBLINHADO PONTILHADO <span style="text-decoration: underline; text-decoration-style: dotted;">texto sublinhado pontilhado</span>)

---


## Item { <ins>nome</ins>, utilizavel, descricao }
## Instancia_Item { <ins>nome, nome_inst, id_inventario, nome_lugar</ins> }


## Pessoa { <ins>id_pessoa, nome_lugar</ins>, nome_pessoa, tipo_pessoa }
## Inventario { <ins>id_pessoa, id_inventario</ins> }


## Regiao { <ins>nome</ins>, descricao }
## Lugar { <ins>nome, nome_regiao</ins>, descricao_especifica, lugar_anterior }




## Prisioneiro {nome, utilizavel, descricao}
## Jogador {nome, utilizavel, descricao}
## Policial {nome, utilizavel, descricao}



