<center>

# Dicionário de Dados

</center>

Este documento serve como a documentação para o dicionário de dados do sistema.

#### Atalhos:

* [Item](#item--insnomeins-utilizavel-descricao-)
* [Instancia_Item](#instancia_item--insnome-nome_inst-id_inventario-nome_lugarins-)
* [Pessoa](#pessoa--insid_pessoa-nome_lugarins-nome_pessoa-tipo_pessoa-)

---
### Item { <ins>nome_item</ins>, descricao_item, tamanho_item, tipo_item }

> Item é uma tabela para guardar informações de itens presentes no jogo.

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|:---------------------:|
|   nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |     CHAR (20) [a-z, A-Z]     |      PRIMARY KEY      |
| descricao_item |         Atributo que descreve um breve resumo da função do item mencionado          |    CHAR (150) [a-z, A-Z]     |       NOT NULL        |
|  tamanho_item  |            Atributo que define o espaço ocupado pelo item no inventário             |             INT              |  NOT NULL, DEFAULT 1  |
|   tipo_item    |         Atributo que define o tipo do item (utilizável, arma ou consumível)         | ENUM('util', 'arma', 'cons') |       NOT NULL        |

---

### Consumivel { <ins>nome_item</ins>, descricao_item, tamanho_item, quantidade_consumivel, efeito_consumivel }

> Consumivel é uma tabela para guardar informações sobre itens que podem ser consumidos no jogo.

|         Nome          |                                  Definição Lógica                                   | Tipo e Formato de Dado | Restrições de Domínio |
|:---------------------:|:-----------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|       nome_item       | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
|    descricao_item     |         Atributo que descreve um breve resumo da função do item mencionado          | CHAR (150) [a-z, A-Z]  |       NOT NULL        |
|     tamanho_item      |            Atributo que define o espaço ocupado pelo item no inventário             |          INT           |  NOT NULL, DEFAULT 1  |
| quantidade_consumivel |           Atributo que define a quantidade do item que pode ser consumido           |          INT           |  NOT NULL, DEFAULT 1  |
|   efeito_consumivel   |              Atributo que descreve o efeito causado ao consumir o item              |  CHAR (30) [a-z, A-Z]  |       NOT NULL        |

---

### Arma { <ins>nome_item</ins>, descricao_item, tamanho_item,  }

> Arma é uma tabela para guardar informações sobre itens que podem ser utilizados como armas no jogo.

|      Nome      |                                  Definição Lógica                                   | Tipo e Formato de Dado | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|   nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
| descricao_item |         Atributo que descreve um breve resumo da função do item mencionado          | CHAR (150) [a-z, A-Z]  |       NOT NULL        |
|  tamanho_item  |            Atributo que define o espaço ocupado pelo item no inventário             |          INT           |  NOT NULL, DEFAULT 1  |
|   dano_arma    |            Atributo que define a quantidade de dano causado por uma arma            |          INT           |       NOT NULL        |
| arma_equipada  |              Atributo que indica se a arma está equipada pelo jogador               |        BOOLEAN         |       NOT NULL        |

---

### Utilizavel

> Utilizavel é uma tabela para guardar informações sobre itens que podem ser utilizados no jogo.

|       Nome        |                                  Definição Lógica                                   | Tipo e Formato de Dado | Restrições de Domínio |
|:-----------------:|:-----------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|     nome_item     | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
|  descricao_item   |         Atributo que descreve um breve resumo da função do item mencionado          | CHAR (150) [a-z, A-Z]  |       NOT NULL        |
|   tamanho_item    |            Atributo que define o espaço ocupado pelo item no inventário             |          INT           |  NOT NULL, DEFAULT 1  |
| efeito_utilizavel |              Atributo que descreve o efeito causado ao utilizar o item              |  CHAR (30) [a-z, A-Z]  |       NOT NULL        |

---
### Instancia_Item { <ins>nome_inst, nome_item, id_inventario, nome_lugar</ins> }

> Instancia_Item será utilizado por pessoas para realização de trocas e o mesmo faz parte do inventário de toda pessoa.
>
> Observação importante: a instância de item ou estará em um inventário ou em um lucal, nunca os dois ao mesmo tempo e nunca com as duas chaves estrangeiras nulas, ou uma vai estar nula ou outra vai estar.

|         Nome         |                                                        Definição Lógica                                                        | Tipo e Formato de Dado | Restrições de Domínio |
|:--------------------:|:------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
| nome_inst, nome_item | Chave composta de nome_inst e nome_item, nome_item vem da chave primaria da tabela Item, ambas sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
|    id_inventario     |                   Chave estrangeira referenciando a tabela Inventario, inventário onde a Instancia_Item está                   |         SERIAL         |      FOREIGN KEY      |
|      nome_lugar      |                        Chave estrangeira referenciando a tabela Lugar, lugar onde a Instancia_Item está                        |  CHAR (25) [a-z, A-Z]  |      FOREIGN KEY      |

---

### Fabricacao { <ins>nome_fabri, nome_item, nome_livro_fabri</ins> }

> Fabricacao é uma tabela que registra os processos de fabricação de itens no jogo.

|         Nome          |                                                        Definição Lógica                                                         | Tipo e Formato de Dado | Restrições de Domínio |
|:---------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
| nome_fabri, nome_item | Chave composta de nome_fabri e nome_item, nome_item vem da chave primaria da tabela Item, ambas sem caracteres especiais (~Ç@!) |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |
|   nome_livro_fabri    |                   Chave estrangeira referenciando a tabela Inventario, inventário onde a Instancia_Item está                    |  CHAR (20) [a-z, A-Z]  |      FOREIGN KEY      |

---

### Livro_Fabricacoes { <ins>nome_livro_fabri</ins> }

> Fabricacao é uma tabela que registra os processos de fabricação de itens no jogo.

|         Nome          |                                                        Definição Lógica                                                         | Tipo e Formato de Dado | Restrições de Domínio |
|:---------------------:|:-------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|   nome_livro_fabri    |                                   Chave primária onde armazena o nome do livro de fabricações                                   |  CHAR (20) [a-z, A-Z]  |      PRIMARY KEY      |

---
### Inventario { <ins>id_pessoa, id_inventario</ins>, tamanho_inventario, inventario_ocupado }

> Inventário é a tabela que contém as instâncias de item, cada inventário pertence exclusivamente a uma única pessoa.

|           Nome           | Definição Lógica                                                              | Tipo e Formato de Dado | Restrições de Domínio |
|:------------------------:|-------------------------------------------------------------------------------|:----------------------:|:---------------------:|
| id_pessoa, id_inventario | Chave composta do id_pessoa e id_inventario                                   |         SERIAL         |      PRIMARY KEY      |
|    tamanho_inventario    | Atributo que definirá o tamanho máximo de itens que podem estar no inventário |          INT           |  NOT NULL, DEFAULT 5  |
|    inventario_ocupado    | Atributo que definirá quantos itens tem o inventário                          |          INT           |  NOT NULL, DEFAULT 0  |

---
### Pessoa { <ins>id_pessoa, nome_lugar</ins>, nome_pessoa, tipo_pessoa }

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
### Prisioneiro { <ins>id_pessoa, id_jogador</ins>, nome_pessoa, habilidade_briga_prisioneiro, vida_prisioneiro, forca_prisioneiro, gangue_prisioneiro }

> Prisioneiro é uma tabela que contém informações sobre prisioneiros no jogo.

|             Nome             |                                     Definição Lógica                                     | Tipo e Formato de Dado | Restrições de Domínio |
|:----------------------------:|:----------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|          id_pessoa           |                 Chave primária que terá um identificador único da pessoa                 |         SERIAL         |      PRIMARY KEY      |
|         nome_pessoa          | Atributo que define o nome da pessoa completa mencionada sem caracteres especiais (~Ç@!) |  CHAR (60) [a-z, A-Z]  |       NOT NULL        |
| habilidade_briga_prisioneiro |           Atributo que indica a habilidade de briga do prisioneiro em combate            |          INT           |  NOT NULL, DEFAULT 2  |
|       vida_prisioneiro       |               Atributo que representa a quantidade de vida do prisioneiro                |          INT           | NOT NULL, DEFAULT 10  |
|      forca_prisioneiro       |                  Atributo que define a força do prisioneiro em combate                   |          INT           |  NOT NULL, DEFAULT 2  |
|      gangue_prisioneiro      |                Atributo que define a gangue a qual o prisioneiro pertence                |  CHAR (20) [a-z, A-Z]  |       NOT NULL        |
|          id_jogador          |                   Chave estrangeira referenciando a tabela de jogador                    |         SERIAL         | FOREIGN KEY, NOT NULL |

---

### Jogador { <ins>id_pessoa</ins>, nome_pessoa, habilidade_briga_jogador, vida_jogador, forca_jogador, respeito_jogador, tempo_vida_jogador, gangue_jogador }

> Jogador é uma tabela que contém informações sobre os jogadores no jogo.

|           Nome           |                                     Definição Lógica                                     | Tipo e Formato de Dado | Restrições de Domínio |
|:------------------------:|:----------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|        id_pessoa         |                 Chave primária que terá um identificador único da pessoa                 |         SERIAL         |      PRIMARY KEY      |
|       nome_pessoa        | Atributo que define o nome da pessoa completa mencionada sem caracteres especiais (~Ç@!) |  CHAR (60) [a-z, A-Z]  |       NOT NULL        |
| habilidade_briga_jogador |             Atributo que indica a habilidade de briga do jogador em combate              |          INT           |  NOT NULL, DEFAULT 2  |
|       vida_jogador       |                 Atributo que representa a quantidade de vida do jogador                  |          INT           | NOT NULL, DEFAULT 10  |
|      forca_jogador       |                    Atributo que define a força do jogador em combate                     |          INT           |  NOT NULL, DEFAULT 2  |
|     respeito_jogador     |       Atributo que indica o nível de respeito do jogador entre outros personagens        |          INT           |       NOT NULL        |
|    tempo_vida_jogador    |                  Atributo que indica o tempo de vida do jogador no jogo                  |          INT           |       NOT NULL        |
|      gangue_jogador      |                  Atributo que define a gangue a qual o jogador pertence                  |  CHAR (20) [a-z, A-Z]  |       NOT NULL        |

---

### Policial { <ins>id_pessoa</ins>, nome_pessoa, policial_corrupto }

> Policial é uma tabela que contém informações sobre policiais no jogo.

|       Nome        |                                     Definição Lógica                                     | Tipo e Formato de Dado | Restrições de Domínio |
|:-----------------:|:----------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|     id_pessoa     |                 Chave primária que terá um identificador único da pessoa                 |         SERIAL         |      PRIMARY KEY      |
|    nome_pessoa    | Atributo que define o nome da pessoa completa mencionada sem caracteres especiais (~Ç@!) |  CHAR (60) [a-z, A-Z]  |       NOT NULL        |
| policial_corrupto |            Atributo que indica se o policial é corrupto (verdadeiro ou falso)            |        BOOLEAN         |       NOT NULL        |

---

### Informante { <ins>id_pessoa</ins>, nome_pessoa, dano_informante }

> Informante é uma tabela que contém informações sobre informantes no jogo.

|      Nome       |                                     Definição Lógica                                     | Tipo e Formato de Dado | Restrições de Domínio |
|:---------------:|:----------------------------------------------------------------------------------------:|:----------------------:|:---------------------:|
|    id_pessoa    |                 Chave primária que terá um identificador único da pessoa                 |         SERIAL         |      PRIMARY KEY      |
|   nome_pessoa   | Atributo que define o nome da pessoa completa mencionada sem caracteres especiais (~Ç@!) |  CHAR (60) [a-z, A-Z]  |       NOT NULL        |
| dano_informante |                 Atributo que indica o dano que o informante pode causar                  |          INT           |       NOT NULL        |


---

### Regiao { <ins>nome_regiao</ins>, descricao_regiao }

> Região é uma tabela que contém informações de cada região no jogo.

|       Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Restrições de Domínio       |
|:----------------:|:-----------------------------------------------------------------------------------:|:----------------------:|-----------------------------|
|   nome_regiao    | Chave primaria contendo o nome da região mencionado sem caracteres especiais (~Ç@!) |  CHAR (15) [a-z, A-Z]  | PRIMARY KEY                 |
| descricao_regiao |             Atributo contendo uma breve descrição da região mencionada              | CHAR (200) [a-z, A-Z]  | NOT NULL                    |

---
### Lugar { <ins>nome_lugar, nome_regiao</ins>, descricao_especifica_lugar, lugar_anterior }

> Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica.

|            Nome            |                                                     Definição Lógica                                                     | Tipo e Formato de Dado | Restrição             |
|:--------------------------:|:------------------------------------------------------------------------------------------------------------------------:|:----------------------:|-----------------------|
|         nome_lugar         |                         Chave primaria nome do lugar mencionado sem caracteres especiais (~Ç@!)                          |  CHAR (25) [a-z, A-Z]  | PRIMARY KEY           |
| descricao_especifica_lugar | Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente sem caracteres especiais (~Ç@!) | CHAR (200) [a-z, A-Z]  | NOT NULL              |
|       lugar_anterior       |                                  Atributo que contém o lugar de origem, sala de origem                                   |  CHAR (25) [a-z, A-Z]  | NOT NULL              |
|        nome_regiao         |                       Chave estrangeira que contém o nome da região na qual aquele lugar pertence                        |  CHAR (15) [a-z, A-Z]  | FOREIGN KEY, NOT NULL |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |                 Descrição                  | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:------------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 15/07/2024 | `1.0`  |           Criação do documento.            | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 16/07/2024 | `1.1`  | Atualização e detalhamento de informações. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 17/07/2024 | `2.0`  |         Aumenta escopo do projeto.         | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |

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


# Tabela Prisao 
|                 |   |   
|-----------------|---| 
| **Descrição**   |Prisão é uma tabela que contém informações da prisão do jogo.|
| **Observações** |  Não possui chave estrangeira. | 

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|   id_prisao     |Chave primária que define o número de identificação da prisão |       SERIAL      |   -  |      PRIMARY KEY      |
| nome_prisao  |        nome da prisão sem caracteres especiais (~ç@!)         |       CHAR [a-z, A-Z]        | 25     |       NOT NULL        |
---
# Tabela Regiao

|                 |   |   
|-----------------|---| 
| **Descrição**   | Região é uma tabela que contém informações de cada região no jogo. |
| **Observações** |  Possui chave estrangeira vindo de `Prisao`. |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  nome_regiao    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |       CHAR [a-z, A-Z]        | 25     |      PRIMARY KEY      |
|  descricao_regiao |         Atributo contendo uma breve descrição da região mencionada          |       TEXT         | -     |       NOT NULL        |
|  prisao  |            Chave estrangeira vindo de prisão             |             SERIAL              | -       |  FOREIGN KEY, NOT NULL  |
---
# Tabela Lugar 


|                 |   |   
|-----------------|---| 
| **Descrição**   |  Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica.
| **Observações** |  Possui chave estrangeira vindo de `Regiao`. |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  nome_lugar    | Chave primaria nome do lugar mencionado sem caracteres especiais  (~Ç@!) |       CHAR [a-z, A-Z]        | 25     |      PRIMARY KEY      |
|  descricao_lugar |         Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente sem caracteres especiais (~Ç@!)          |       TEXT        | -     |       NOT NULL        |
|       lugar_anterior       |                                  Atributo que contém o lugar de origem, sala de origem                                   |  CHAR  [a-z, A-Z]| 25 | NOT NULL              |
|  regiao  |            Chave estrangeira que contém o nome da região na qual aquele lugar pertence             |             CHAR [a-z, A-Z]              | 25       |  FOREIGN KEY, NOT NULL  |
---

# Tabela Pessoa 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Pessoa é uma tabela que contém informações generalizadas de cada pessoa no jogo.
| **Observações** | Possui chave estrangeira vindo de `Lugar`.   |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  id_pessoa    | Chave primária que define o número de identificação do personagem mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_pessoa |          Nome e sobrenome da pessoa mencionada          |      CHAR [a-z, A-Z]        |   60   |       NOT NULL        |
|       tipo_pessoa       |                                 atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador)                                   |  ENUM('poli', 'pris', 'info', 'joga') | - | NOT NULL              |
|  lugar  |            Chave estrangeira vindo de lugar            |             CHAR  [a-z, A-Z]            | 25       |  FOREIGN KEY, NOT NULL  |
---

# Tabela Inventario 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Inventário é uma tabela que contém informações de cada inventário no jogo.
| **Observações** | Possui chave estrangeira vindo de `pessoa`.   |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
| id_inventario    | Chave primária que define o número de identificação do inventário mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  tamanho_inventario |   Atributo que define o  tamanho do inventário total do jogador          |      INT [1-5]       |   -  |       NOT NULL        |
|       inventario ocupado       |                                 Atributo derivado para a identificação se o inventário está cheio ou não.                                   |  BOOLEAN | - | NOT NULL              |
|  pessoa  |            Chave estrangeira vindo de pessoa            |             SERIAL              | -       |  FOREIGN KEY, NOT NULL  |
---

# Tabela Prisioneiro 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Prisioneiro é uma tabela que contém informações especializadas de cada prisioneiro no jogo.
| **Observações** |  Possui chave estrangeira vindo de `Lugar`. |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  id_pessoa    | Chave primária que define o número de identificação do personagem mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_pessoa |          Nome e sobrenome da pessoa mencionada          |      CHAR [a-z, A-Z]        |   60   |       NOT NULL        |
|       tipo_pessoa       |                                 atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador)                                   |  ENUM ('poli', 'pris', 'info', 'joga') | - | NOT NULL              |
|  gangue_prisioneiro |          atributo que determina qual gangue o prisioneiro é afiliado. tendo 2 opções, polvo e palhaço.          |      ENUM ( 'polvo', 'palhaco')       |  -   |       NOT NULL        |
|  habilidade_briga_prisioneiro |          A possível habilidade de luta de um prisioneiro. Multiplica o dano junto do atributo força.          |      INT [1-10]     |   -  |       NOT NULL        |
|  vida_prisioneiro |          atibuto que determina a quantidade de vida que um prisioneiro possui.          |      INT [1-10]      |   -   |       NOT NULL        |
|  força_prisioneiro |         atibuto que determina a quantidade de força que um prisioneiro possui.          |      INT  [1-10]     |   -   |       NOT NULL        |
|  lugar  |            chave estrangeira vindo de lugar            |             CHAR              | 25       |  FOREIGN KEY, NOT NULL  |
---

# Tabela Policial 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Policial é uma tabela que contém informações especializadas de cada policial no jogo.
| **Observações** |  Possui chave estrangeira vindo de `Lugar`.  |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  id_pessoa    | Chave primária que define o número de identificação do personagem mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_pessoa |          Nome e sobrenome da pessoa mencionada          |      CHAR [a-z, A-Z]        |   60   |       NOT NULL        |
|       tipo_pessoa       |                                 atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador)                                   |  ENUM('poli', 'pris', 'info', 'joga') | - | NOT NULL              |
|  policial_corrupto |          Esse atributo denomina se um policial é corrupto ou não.          |      BOOLEAN         |   -   |       NOT NULL        |
|  lugar  |            Chave estrangeira vindo de lugar            |             CHAR   [a-z, A-Z]          | 25       |  FOREIGN KEY, NOT NULL  |

---

# Tabela Informante 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Informante é uma classe que fica oculta, e quando um jogador tenta atacar ou negociar com o mesmo, sofre uma penalidade em tempo de vida.
| **Observações** |  Possui chave estrangeira vindo de `Lugar`.  |

|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  id_pessoa    | Chave primária que define o número de identificação do personagem mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_pessoa |          Nome e sobrenome da pessoa mencionada          |      CHAR [a-z, A-Z]        |   60   |       NOT NULL        |
|       tipo_pessoa       |                                 Atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador)                                   |  ENUM('poli', 'pris', 'info', 'joga') | - | NOT NULL              |
|  dano_info |          Inteiro que irá matar instantaneamente um jogador          |      INT        |   -   |       NOT NULL, DEFAULT 200        |
|  lugar  |            Chave estrangeira vindo de lugar            |             CHAR    [a-z, A-Z]          | 25       |  FOREIGN KEY, NOT NULL  |

---

# Tabela Jogador 

|                 |   |   
|-----------------|---| 
| **Descrição**   |  Jogador é uma tabela que contém informações especializadas do jogador no jogo.
| **Observações** |  Possui chave estrangeira vindo de `Lugar`.  |


|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|  id_pessoa    | Chave primária que define o número de identificação do personagem mencionado |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_pessoa |          Nome e sobrenome da pessoa mencionada          |      CHAR [a-z, A-Z]        |   60   |       NOT NULL        |
|       tipo_pessoa       |                                 Atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador)                                   |  ENUM('poli', 'pris', 'info', 'joga') | - | NOT NULL              |
|   habilidade_briga_jogador |          A possível habilidade de luta de um jogador. Ter conhecimento de boxe contaria como um exemplo          |      INT        |   1-10   |       NOT NULL        |
|  vida_jogador |          atibuto que determina a quantidade de vida que um jogador possui.          |      INT  [1-10]      |   -   |       NOT NULL        |
|  força_jogador |          atibuto que determina a quantidade de força que um jogador possui.          |      INT   [1-10]     |   -  |       NOT NULL        |
|  respeito_jogador |          atributo derivado que determina quanto respeito um jogador possui          |      INT   [1-10]     |   -  |       NOT NULL        |
|  tempo_vida_jogador |          atibuto que determina quanto tempo de vida restante um jogador possui.          |      INT   [1-10]     |  -   |       NOT NULL        |
|  gangue_jogador |          atributo que determina qual gangue o jogador é afiliado.  tendo 2 opções, polvo e palhaço.         |     ENUM  ('polvo', 'palhaco')      |   -   |       NOT NULL        |
|  missao |         Atributo que determina qual a missão atual do jogador.          |      CHAR   [a-z, A-Z]      |   25   |   FOREIGN KEY,    NOT NULL        |
|  lugar  |            chave estrangeira vindo de lugar            |             CHAR         [a-z, A-Z]     | 25       |  FOREIGN KEY, NOT NULL  |

---

# Tabela Missão 

|                 |   |   
|-----------------|---| 
| **Descrição**   | Missão é uma tabela que contém informações especializadas de cada missão no jogo.
| **Observações** |  Possui chave estrangeira vindo de `Pessoa`.  |


|      Nome      |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
| id_missao   | Chave primária que define o número de identificação da missão mencionada. |       SERIAL        | -     |      PRIMARY KEY      |
|  nome_missao |          Nome da missão sem caracteres especiais (~ç@!)          |      CHAR   [a-z, A-Z]      |  60   |       NOT NULL        |
|      descricao_missao       |                                 uma descrição detalhando os objetivos necessários para completar a missão atual.                                   |  TEXT | - | NOT NULL              |
|  Item_Nao_Fabricavel  |            esse atributo determina qual a recompensa da missão. A recompensa de uma missão sempre é um item não fabricável.            |             CHAR [a-z, A-Z]              | 25       |  FOREIGN KEY, NOT NULL  |
|  lugar  |            chave estrangeira vindo de lugar            |             CHAR         [a-z, A-Z]     | 25       |  FOREIGN KEY, NOT NULL  |
---

