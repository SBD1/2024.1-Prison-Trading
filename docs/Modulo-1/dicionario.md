# Dicionário de dados

Esquema de Relação

---
## Item { <ins>nome</ins>, utilizavel, descricao }

> Item é uma tabela para guardar informações de itens presentes no jogo.

|      Nome       |                                     Definição Lógica                                     | Tipo e Formato de Dado | Restrições de Domínio  |
|:---------------:|:----------------------------------------------------------------------------------------:|:----------------------:|:----------------------:|
|    nome_item    |   Chave primaria que define o nome do item mencionado sem caracteres especiais (~Ç@!)    |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY       |
| utilizavel_item | Atributo que define se o item é utilizável, ou apenas para troca (como cigarro ou moeda) |        BOOLEANO        |        NOT NULL        |
| descricao_item  |           Atributo que descreve um breve resumo da função do item mencionado.            | CHAR (150) [a-z, A-Z]  |        NOT NULL        |


---
## Instancia_Item { <ins>nome, nome_inst, id_inventario, nome_lugar</ins> }

> Instancia_Item será utilizado por pessoas para realização de trocas e o mesmo faz parte do inventário de toda pessoa.
>
> Observação importante: a instância de item ou estará em um inventário ou em um lucal, nunca os dois ao mesmo tempo e nunca com as duas chaves estrangeiras nulas, ou uma vai estar nula ou outra vai estar.

|         Nome         |                                                        Definição Lógica                                                        | Tipo e Formato de Dado | Restrições de Domínio |
|:--------------------:|:------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
| nome_inst, nome_item | Chave composta de nome_inst e nome_item, nome_item vem da chave primaria da tabela Item, ambas sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
|    id_inventario     |                   Chave estrangeira referenciando a tabela Inventario, inventário onde a Instancia_Item está                   |         SERIAL         |      FOREIGN KEY      |
|      nome_lugar      |                        Chave estrangeira referenciando a tabela Lugar, lugar onde a Instancia_Item está                        |  CHAR (25) [a-z, A-Z]  |      FOREIGN KEY      |

---
## Pessoa { <ins>id_pessoa, nome_lugar</ins>, nome_pessoa, tipo_pessoa }

> Pessoa é uma Entidade Generica a mesma possui informações básicas de pessoas e irá se ramificar em Jogador, Prisioneiro e Policial. 
> 
> Observação importante: a Pessoa sempre estará em um local, logo a chave estrangeira nome_lugar nunca deve ser nula.

|    Nome     |                                     Definição Lógica                                     |    Tipo e Formato de Dado    | Restrições de Domínio  |
|:-----------:|:----------------------------------------------------------------------------------------:|:----------------------------:|:----------------------:|
|  id_pessoa  |                 Chave primária que terá um identificador único da pessoa                 |            SERIAL            |      PRIMARY KEY       |
| nome_pessoa | Atributo que define o nome da pessoa completo mencionada sem caracteres especiais (~Ç@!) |     CHAR (60) [a-z, A-Z]     |        NOT NULL        |
| tipo_pessoa |         Atributo que definirá o tipo da pessoa, tendo apenas 3 valores possiveis         | ENUM('POLI', 'JOGA', 'PRIS') |        NOT NULL        |
| nome_lugar  |         Chave estrangeira referenciando a tabela Lugar, lugar onde a Pessoa está         |     CHAR (25) [a-z, A-Z]     | FOREIGN KEY, NOT NULL  |

---
## Inventario { <ins>id_pessoa, id_inventario</ins> }

> Inventário é a tabela que contém as instâncias de item, cada inventário pertence exclusivamente a uma única pessoa.

|           Nome           |               Definição Lógica                | Tipo e Formato de Dado |    Restrições de Domínio     |
|:------------------------:|-----------------------------------------------|:----------------------:|:----------------------------:|
| id_pessoa, id_inventario | Chave composta do id_pessoa e id_inventario   |         SERIAL         |         PRIMARY KEY          |

---
## Regiao { <ins>nome</ins>, descricao }

> Região é uma tabela que contém informações de cada região no jogo.

|       Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Restrições de Domínio       |
|:----------------:|:-----------------------------------------------------------------------------------:|:----------------------:|-----------------------------|
|   nome_regiao    | Chave primaria contendo o nome da região mencionado sem caracteres especiais (~Ç@!) |  CHAR (15) [a-z, A-Z]  | PRIMARY KEY                 |
| descricao_regiao |             Atributo contendo uma breve descrição da região mencionada              | CHAR (200) [a-z, A-Z]  | NOT NULL                    |

---
## Lugar { <ins>nome_lugar, nome_regiao</ins>, descricao_especifica, lugar_anterior }

> Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica.

|            Nome            |                                                     Definição Lógica                                                     | Tipo e Formato de Dado | Restrição             |
|:--------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:----------------------:|-----------------------|
|         nome_lugar         |                         Chave primaria nome do lugar mencionado sem caracteres especiais (~Ç@!)                          |  CHAR (25) [a-z, A-Z]  | PRIMARY KEY           |
| descricao_especifica_lugar | Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente sem caracteres especiais (~Ç@!) | CHAR (200) [a-z, A-Z]  | NOT NULL              |
|       lugar_anterior       |                                  Atributo que contém o lugar de origem, sala de origem                                   |  CHAR (25) [a-z, A-Z]  | NOT NULL              |
|        nome_regiao         |                       Chave estrangeira que contém o nome da região na qual aquele lugar pertence                        |  CHAR (15) [a-z, A-Z]  | FOREIGN KEY, NOT NULL |

## Prisioneiro { <ins>id_pessoa</ins>, nome_pessoa, gangue }

>

tabela

---
## Jogador { <ins>id_pessoa</ins>, nome_pessoa, corrupto }

>

tabela

---
## Policial { <ins>id_pessoa</ins>, nome_pessoa, tempo_vida, respeito, gangue }

>

tabela

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |                 Descrição                  | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:------------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 15/07/2024 | `1.0`  |           Criação do documento.            | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 16/07/2024 | `1.1`  | Atualização e detalhamento de informações. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |

</div>


[//]: # (SUBLINHADO <ins>aaaaa</ins>)
[//]: # (SUBLINHADO PONTILHADO <span style="text-decoration: underline; text-decoration-style: dotted;">texto sublinhado pontilhado</span>)

[//]: # (---)

[//]: # ()
[//]: # ()
[//]: # (## Item { <ins>nome</ins>, utilizavel, descricao })

[//]: # (## Instancia_Item { <ins>nome, nome_inst, id_inventario, nome_lugar</ins> })

[//]: # ()
[//]: # ()
[//]: # (## Pessoa { <ins>id_pessoa, nome_lugar</ins>, nome_pessoa, tipo_pessoa })

[//]: # (## Inventario { <ins>id_pessoa, id_inventario</ins> })

[//]: # ()
[//]: # ()
[//]: # (## Regiao { <ins>nome</ins>, descricao })

[//]: # (## Lugar { <ins>nome, nome_regiao</ins>, descricao_especifica, lugar_anterior })

[//]: # ()
[//]: # ()
[//]: # ()
[//]: # ()
[//]: # (## Prisioneiro { <ins>id_pessoa</ins>, nome_pessoa, gangue })

[//]: # (## Jogador { <ins>id_pessoa</ins>, nome_pessoa, corrupto })

[//]: # (## Policial { <ins>id_pessoa</ins>, nome_pessoa, tempo_vida, respeito, gangue })



