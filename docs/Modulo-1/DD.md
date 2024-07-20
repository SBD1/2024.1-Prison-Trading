<center>

# Dicionário de Dados

</center>

---

<center>

# O que é?

</center>

> Este documento serve como a documentação para o dicionário de dados do sistema. Ele descreve cada elemento de dados utilizado pelo sistema, explicando o que são, onde estão armazenados e como se relacionam.

<div style="margin: 0 auto; width: fit-content;">

| Tabelas                                            |
|:---------------------------------------------------|
| [Item](#tabela-item)                               |
| [Instancia_Item](#tabela-instancia_item)           |
| [Item_Fabricavel](#tabela-item_fabricavel)         |
| [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) |
| [Ferramenta](#tabela-ferramenta)                   |
| [Arma](#tabela-arma)                               |
| [Comida](#tabela-comida)                           |
| [Medicamento](#tabela-medicamento)                 |
| [Utilizavel](#tabela-utilizavel)                   |
| [Fabricacao](#tabela-fabricacao)                   |
| [Livro_Fabricacoes](#tabela-livro_fabricacoes)     |
| [Prisao](#tabela-prisao)                           |
| [Regiao](#tabela-regiao)                           |
| [Lugar](#tabela-lugar)                             |
| [Pessoa](#tabela-pessoa)                           |
| [Inventario](#tabela-inventario)                   |
| [Prisioneiro](#tabela-prisioneiro)                 |
| [Policial](#tabela-policial)                       |
| [Informante](#tabela-informante)                   |
| [Jogador](#tabela-jogador)                         |
| [Missao](#tabela-missao)                           |

</div>

---
<center>

# Tabela Item

</center>

|                 |                                                                                                                                                 |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item.               |
| **Observações** | Tipo possui os valores `fabr` para [Item_Fabricavel](#tabela-item_fabricavel) e `nfab` para [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel). | 

|   Nome    |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_item | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| tipo_item |                         Atributo que define o tipo do item                          |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |

---

# Tabela Instancia_Item

|                 |                                                                                                                                        |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Instancia_item é uma entidade fraca que é usada instanciar itens, a mesma é utilizada em Lugar, Inventario e Fabricacao.               |
| **Observações** | Possui as chaves estrangeiras da entidade [Lugar](#tabela-lugar), [Inventario](#tabela-inventario) e [Fabricacao](#tabela-fabricacao). | 

|      Nome      |                                                 Definição Lógica                                                 | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------:|:----------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_ist, item | Chave composta de nome_inst e item, item é chave primária da tabela Item, ambas sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 50      |      PRIMARY KEY      |
|     item      |                Chave estrangeira referenciando a tabela Item, Item onde a instância de item está                |    CHAR [a-z, A-Z]     | 25       |      FOREIGN KEY,  NOT NULL      |
|     lugar      |               Chave estrangeira referenciando a tabela Lugar, Lugar onde a instância de item está                |    CHAR [a-z, A-Z]     | -       |      FOREIGN KEY      |
|   inventario   |          Chave estrangeira referenciando a tabela Inventário, Inventário onde a instância de item está           |         SERIAL         | -       |      FOREIGN KEY      |
|   fabricacao   |       Chave estrangeira referenciando a tabela Fabricação, Fabricação onde a instância de item é utilizada       |    CHAR [a-z, A-Z]     | 25      |      FOREIGN KEY      |

--------

# Tabela Item_Fabricavel

|                 |                                                                                                                                                         |   
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item_Fabricavel. |
| **Observações** |  Tipo possui os valores `ferr` para [Ferramenta](#tabela-ferramenta)  e `arma` para [Arma](#tabela-arma).                                               | 

|      Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY, FOREIGN KEY      |
| tipo_fabricavel |                    Atributo que define o tipo do item fabricável                    |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |

---

# Tabela Item_Nao_Fabricavel

|                 |                                                                                                                                                                 |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Não Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item_Nao_Fabricavel. |
| **Observações** |  Tipo possui os valores `comi` para [Comida](#tabela-comida), `medi` para [Medicamento](#tabela-medicamento) e `util` para [Utilizavel](#tabela-utilizavel).    | 

|        Nome         |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-------------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|      nome_item      | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY, FOREIGN KEY      |
| tipo_nao_fabricavel |                  Atributo que define o tipo do item não fabricável                  | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |

---

# Tabela Ferramenta

|                 |                                                                                                                             |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela de ferramentas, que podem ser utilizadas.                                                                            |
| **Observações** | A Tabela [Item_Fabricavel](#tabela-item_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

|         Nome         |                                     Definição Lógica                                      | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:--------------------:|:-----------------------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|      nome_item       | Chave primária que define o nome da ferramenta mencionada sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      | PRIMARY KEY, FOREIGN KEY |
|     tamanho_item     |               Atributo que define o espaço que o item ocupará no inventário               |          INT           | -       |   NOT NULL, DEFAULT 1    |
|    descricao_item    |            Atributo que descreve um breve resumo da função do item mencionado             |          TEXT          | -       |         NOT NULL         |
| utilidade_ferramenta |                      Atributo que descreve a utilidade da ferramenta                      |          TEXT          | -       |         NOT NULL         |

---

# Tabela Arma

|                 |                                                                                                                             |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela de armas, que podem ser usadas para ferir prisioneiros e jogadores.                                                  |
| **Observações** | A Tabela [Item_Fabricavel](#tabela-item_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

|      Nome       |                                       Definição Lógica                                       | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:---------------:|:--------------------------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|    nome_item    |     Chave primária que define o nome da arma mencionada sem caracteres especiais (~Ç@!)      |    CHAR [a-z, A-Z]     | 25      | PRIMARY KEY, FOREIGN KEY |
|  tamanho_item   |                Atributo que define o espaço que o item ocupará no inventário                 |          INT           | -       |   NOT NULL, DEFAULT 1    |
| descricao_item  |              Atributo que descreve um breve resumo da função do item mencionado              |          TEXT          | -       |         NOT NULL         |
|    dano_arma    |                Atributo que define o dano que uma arma pode dar em uma pessoa                |          INT           | -       |         NOT NULL         |
|  arma_equipada  | Atributo que define se um jogador está com a arma equipada na mão ou escondida no inventário |        BOOLEAN         | -       |         NOT NULL         |

---

# Tabela Comida

|                 |                                                                                                                                                            |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar comidas que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados a comida some do inventário do jogador. |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira.                        | 

|          Nome           |                                                          Definição Lógica                                                          | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:-----------------------:|:----------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|        nome_item        |                       Chave primária que define o nome da comida mencionada sem caracteres especiais (~Ç@!)                        |    CHAR [a-z, A-Z]     | 25      | PRIMARY KEY, FOREIGN KEY |
|      tamanho_item       |                                   Atributo que define o espaço que o item ocupará no inventário                                    |          INT           | -       |   NOT NULL, DEFAULT 1    |
|     descricao_item      |                                 Atributo que descreve um breve resumo da função do item mencionado                                 |          TEXT          | -       |         NOT NULL         |
| raridade_nao_fabricavel |             Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo              |       INT [0-2]        | -       |   NOT NULL, DEFAULT 0    |
|    quantidade_comida    |                Atributo que define a quantidade disponivel de uma comida por espaço, (EX: 3 pães ocupam 1 tamanho)                 |          INT           | -       |         NOT NULL         |
|    qualidade_comida     | Atributo que define a qualidade da comida, quanto mais qualidade mais vida a comida pode recuperar, (0=normal, 1=bom, 2=excelente) |       INT [0-2]        | -       |   NOT NULL, DEFAULT 0    |

---

# Tabela Medicamento

|                 |                                                                                                                                                                      |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar medicamentos que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados o medicamento some do inventário do jogador. |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira.                                  | 

|          Nome           |                                                               Definição Lógica                                                               | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:-----------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|        nome_item        |                          Chave primária que define o nome do medicamento mencionado sem caracteres especiais (~Ç@!)                          |    CHAR [a-z, A-Z]     | 25      | PRIMARY KEY, FOREIGN KEY |
|      tamanho_item       |                                        Atributo que define o espaço que o item ocupará no inventário                                         |          INT           | -       |   NOT NULL, DEFAULT 1    |
|     descricao_item      |                                      Atributo que descreve um breve resumo da função do item mencionado                                      |          TEXT          | -       |         NOT NULL         |
| raridade_nao_fabricavel |                 Atributo que define a raridade de um item, podendo ter 3 possiveis valores (0=normal, 1=raro e 2=ultrararo)                  |       INT [0-2]        | -       |   NOT NULL, DEFAULT 0    |
|    cura_medicamento     |                                       Atributo que define quanto de vida um medicamento pode recuperar                                       |          INT           | -       |         NOT NULL         |
|  qualidade_medicamento  | Atributo que define a qualidade do medicamento, quanto mais qualidade mais vida o medicamento pode recuperar, (0=normal, 1=bom, 2=excelente) |       INT [0-2]        | -       |   NOT NULL, DEFAULT 0    |

---

# Tabela Utilizavel

|                 |                                                                                                                                     |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar itens que podem eventualmente serem utilizados, caso sejam utilizados o item some do inventário do jogador.   |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

|          Nome           |                                              Definição Lógica                                               | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|        nome_item        |       Chave primária que define o nome do item utilizavel mencionado sem caracteres especiais (~Ç@!)        |    CHAR [a-z, A-Z]     | 25      | PRIMARY KEY, FOREIGN KEY |
|      tamanho_item       |                        Atributo que define o espaço que o item ocupará no inventário                        |          INT           | -       |   NOT NULL, DEFAULT 1    |
|     descricao_item      |                     Atributo que descreve um breve resumo da função do item mencionado                      |          TEXT          | -       |         NOT NULL         |
| raridade_nao_fabricavel | Atributo que define a raridade de um item, podendo ter 3 possiveis valores (0=normal, 1=raro e 2=ultrararo) |       INT [0-2]        | -       |   NOT NULL, DEFAULT 0    |
|    efeito_utilizavel    |                              Atributo que define o efeito do item utilizável.                               |          TEXT          | -       |         NOT NULL         |

---

# Tabela Fabricacao

|                 |                                                                                                                                                          |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar a fabricação de um item fabricável, é uma entidade fraca de [Item_Fabricavel](#tabela-item_fabricavel) (todo item tem fabricação). |
| **Observações** |  Possui chave estrangeira de [Livro_Fabricacoes](#tabela-livro_fabricacoes) e chave composta com [Item_Fabricavel](#tabela-item_fabricavel).             | 

|            Nome             |                                                                  Definição Lógica                                                                  | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_fabri, item_fabricavel | Chave composta de nome_fabri e item_fabricavel, item_fabricavel é chave primária da tabela Item_Fabricavel, ambas sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 50      |      PRIMARY KEY      |
|       item_fabricavel       |                     Chave estrangeira que tem o valor da chave primária de Item_Fabricavel, usada para compor a chave composta                     |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |
|      livro_fabricacao       |                             Chave estrangeira referenciando a tabela Livro_Fabricacoes, livro onde a fabricacao está                              |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Livro_Fabricacoes

|                 |                                                                |   
|-----------------|----------------------------------------------------------------| 
| **Descrição**   | É usado para armazenar fabricações (como os itens são feitos). |
| **Observações** | Não possui chave estrangeira.                                  | 

|       Nome       |                                     Definição Lógica                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:----------------:|:----------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_livro_fabri | Chave primária que define o nome do Livro de Fabricações sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |

---

# Tabela Prisao

|                 |                                                               |   
|-----------------|---------------------------------------------------------------| 
| **Descrição**   | Prisão é uma tabela que contém informações da prisão do jogo. |
| **Observações** | Não possui chave estrangeira.                                 | 

|    Nome     |                           Definição Lógica                           | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------:|:--------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|  id_prisao  |    Chave primária que define o número de identificação da prisão     |         SERIAL         | -       |      PRIMARY KEY      |
| nome_prisao | Atributo que define o nome da prisão sem caracteres especiais (~ç@!) |    CHAR [a-z, A-Z]     | 25      |       NOT NULL        |

---

# Tabela Regiao

|                 |                                                                    |   
|-----------------|--------------------------------------------------------------------| 
| **Descrição**   | Região é uma tabela que contém informações de cada região no jogo. |
| **Observações** | Possui chave estrangeira vindo de [Prisao](#tabela-prisao).        |

|       Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:----------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   nome_regiao    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|      prisao      |                          Chave estrangeira vindo de prisão                          |         SERIAL         | -       | FOREIGN KEY, NOT NULL |
| descricao_regiao |             Atributo contendo uma breve descrição da região mencionada              |          TEXT          | -       |       NOT NULL        |

---

# Tabela Lugar

|                 |                                                                                                                                                    |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica, é uma entidade fraca de [Regiao](#tabela-regiao). |
| **Observações** | Possui chave composta vindo de [Regiao](#tabela-regiao).                                                                                           |

|        Nome        |                                                     Definição Lógica                                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:------------------:|:------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_lugar, regiao |       Chave composta de nome_lugar e regiao, regiao é a chave primária de Regiao sem caracteres especiais  (~Ç@!)        |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|       regiao       |            Chave estrangeira que tem o valor da chave primária de regiao, usada para compor a chave composta             |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |
|  descricao_lugar   | Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente sem caracteres especiais (~Ç@!) |          TEXT          | -       |       NOT NULL        |
|   lugar_anterior   |                                  Atributo que contém o lugar de origem, sala de origem                                   |    CHAR  [a-z, A-Z]    | 25      |       NOT NULL        |

---

# Tabela Pessoa

|                 |                                                                                                                                                                                                          |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar uma Pessoa, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva.                                                                             |
| **Observações** | Tipo possui os valores `pris` para [Prisioneiro](#tabela-prisioneiro), `poli` para [Policial](#tabela-policial), `info` para [Informante](#tabela-informante) e `joga` para [Jogador](#tabela-jogador) . | 

|    Nome     |                                   Definição Lógica                                   |        Tipo e Formato de Dado        | Tamanho | Restrições de Domínio |
|:-----------:|:------------------------------------------------------------------------------------:|:------------------------------------:|---------|:---------------------:|
|  id_pessoa  |     Chave primária que define o número de identificação do personagem mencionado     |                SERIAL                | -       |      PRIMARY KEY      |
| tipo_pessoa | atributo para identificação de qual tipo de classe o personagem mencionado participa | ENUM('poli', 'pris', 'info', 'joga') | -       |       NOT NULL        |

---

# Tabela Inventario

|                 |                                                                                                                                                                         |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Inventário é uma tabela que contém informações de cada inventário no jogo, é uma entidade fraca de [Pessoa](#tabela-pessoa), todo inventário está relacionado a pessoa. |
| **Observações** | Possui chave composta vindo de [Pessoa](#tabela-pessoa).                                                                                                                |

|         Nome          |                                                             Definição Lógica                                                             | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| id_inventario, pessoa | Chave composta de id_inventario e pessoa, pessoa é a chave primária de pessoa. Define o número de identificação do inventário mencionado |         SERIAL         | -       |      PRIMARY KEY      |
|        pessoa         |                    Chave estrangeira que tem o valor da chave primária de pessoa, usada para compor a chave composta                     |         SERIAL         | -       | FOREIGN KEY, NOT NULL |
|  tamanho_inventario   |                                      Atributo que define o  tamanho do inventário total do jogador                                       |       INT [1-5]        | -       |       NOT NULL        |
|  inventario ocupado   |                                 Atributo derivado para a identificação se o inventário está cheio ou não                                 |        BOOLEAN         | -       |       NOT NULL        |

---

# Tabela Prisioneiro

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Prisioneiro é uma tabela que contém informações especializadas de cada prisioneiro no jogo.                                                                                        |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

|             Nome             |                                                Definição Lógica                                                |        Tipo e Formato de Dado         | Tamanho |  Restrições de Domínio   |
|:----------------------------:|:--------------------------------------------------------------------------------------------------------------:|:-------------------------------------:|---------|:------------------------:|
|          id_pessoa           |                  Chave primária que define o número de identificação do personagem mencionado                  |                SERIAL                 | -       | PRIMARY KEY, FOREIGN KEY |
|            lugar             |                                        Chave estrangeira vindo de lugar                                        |                 CHAR                  | 25      |  FOREIGN KEY, NOT NULL   |
|         nome_pessoa          |                          Atributo que define o nome e sobrenome da pessoa mencionada                           |            CHAR [a-z, A-Z]            | 60      |         NOT NULL         |
| habilidade_briga_prisioneiro | Atributo que define a possível habilidade de luta de um prisioneiro. Multiplica o dano junto do atributo força |              INT [1-10]               | -       |         NOT NULL         |
|       vida_prisioneiro       |                     Atributo que determina a quantidade de vida que um prisioneiro possui                      |              INT [1-10]               | -       |         NOT NULL         |
|      força_prisioneiro       |                     Atributo que determina a quantidade de força que um prisioneiro possui                     |              INT  [1-10]              | -       |         NOT NULL         |
|      gangue_prisioneiro      |          Atributo que determina qual gangue o prisioneiro é afiliado. tendo 2 opções, polvo e palhaco          |      ENUM ( 'polvo', 'palhaco')       | -       |         NOT NULL         |

---

# Tabela Policial

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Policial é uma tabela que contém informações especializadas de cada policial no jogo.                                                                                              |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

|       Nome        |                               Definição Lógica                               |        Tipo e Formato de Dado        | Tamanho |  Restrições de Domínio   |
|:-----------------:|:----------------------------------------------------------------------------:|:------------------------------------:|---------|:------------------------:|
|     id_pessoa     | Chave primária que define o número de identificação do personagem mencionado |                SERIAL                | -       | PRIMARY KEY, FOREIGN KEY |
|       lugar       |                       Chave estrangeira vindo de lugar                       |          CHAR   [a-z, A-Z]           | 25      |  FOREIGN KEY, NOT NULL   |
|    nome_pessoa    |         Atributo que define o nome e sobrenome da pessoa mencionada          |           CHAR [a-z, A-Z]            | 60      |         NOT NULL         |
| policial_corrupto |              Atributo denomina se um policial é corrupto ou não              |               BOOLEAN                | -       |         NOT NULL         |

---

# Tabela Informante

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Informante é uma classe que fica oculta, e quando um jogador tenta atacar ou negociar com o mesmo, sofre uma penalidade em tempo de vida.                                          |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

|    Nome     |                               Definição Lógica                               | Tipo e Formato de Dado | Tamanho |  Restrições de Domínio   |
|:-----------:|:----------------------------------------------------------------------------:|:----------------------:|---------|:------------------------:|
|  id_pessoa  | Chave primária que define o número de identificação do personagem mencionado |         SERIAL         | -       | PRIMARY KEY, FOREIGN KEY |
|    lugar    |                       Chave estrangeira vindo de lugar                       |    CHAR [a-z, A-Z]     | 25      |  FOREIGN KEY, NOT NULL   |
| nome_pessoa |         Atributo que define o nome e sobrenome da pessoa mencionada          |    CHAR [a-z, A-Z]     | 60      |         NOT NULL         |
|  dano_infomante  |          Atributo inteiro que irá matar instantaneamente um jogador          |          INT           | -       |  NOT NULL, DEFAULT 200   |

---

# Tabela Jogador

|                 |                                                                                                                                                                                                               |   
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Jogador é uma tabela que contém informações especializadas do jogador no jogo.                                                                                                                                |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar) e [Missao](#tabela-missao), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

|           Nome           |                                                  Definição Lógica                                                  |   Tipo e Formato de Dado   | Tamanho |  Restrições de Domínio   |
|:------------------------:|:------------------------------------------------------------------------------------------------------------------:|:--------------------------:|---------|:------------------------:|
|        id_pessoa         |                    Chave primária que define o número de identificação do personagem mencionado                    |           SERIAL           | -       | PRIMARY KEY, FOREIGN KEY |
|          lugar           |                                          Chave estrangeira vindo de lugar                                          |      CHAR [a-z, A-Z]       | 25      |  FOREIGN KEY, NOT NULL   |
|          missao          |                               Atributo que determina qual a missão atual do jogador                                |      CHAR [a-z, A-Z]       | 25      |  FOREIGN KEY, NOT NULL   |
|       nome_pessoa        |                            Atributo que define o nome e sobrenome da pessoa mencionada                             |      CHAR [a-z, A-Z]       | 60      |         NOT NULL         |
| habilidade_briga_jogador | Atributo que define a possível habilidade de luta de um jogador. Ter conhecimento de boxe contaria como um exemplo |         INT [1-10]         | -       |         NOT NULL         |
|       vida_jogador       |                         Atributo que determina a quantidade de vida que um jogador possui                          |         INT [1-10]         | -       |         NOT NULL         |
|      força_jogador       |                         Atributo que determina a quantidade de força que um jogador possui                         |         INT [1-10]         | -       |         NOT NULL         |
|     respeito_jogador     |                         Atributo derivado que determina quanto respeito um jogador possui                          |         INT [1-10]         | -       |         NOT NULL         |
|    tempo_vida_jogador    |                       Atributo que determina quanto tempo de vida restante um jogador possui                       |         INT [1-10]         | -       |         NOT NULL         |
|      gangue_jogador      |             Atributo que determina qual gangue o jogador é afiliado.  tendo 2 opções, polvo e palhaco              | ENUM  ('polvo', 'palhaco') | -       |         NOT NULL         |

---

# Tabela Missao

|                 |                                                                                                                |   
|-----------------|----------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Missão é uma tabela que contém informações especializadas de cada missão no jogo.                              |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar) e [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel). |

|        Nome         |                                              Definição Lógica                                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|      id_missao      |                  Chave primária que define o número de identificação da missão mencionada                  |         SERIAL         | -       |      PRIMARY KEY      |
| item_nao_fabricavel | Atributo determina qual a recompensa da missão. A recompensa de uma missão sempre é um item não fabricável |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |
|        lugar        |                                      Chave estrangeira vindo de lugar                                       |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY |
|     nome_missao     |                    Atributo que define o nome da missão sem caracteres especiais (~ç@!)                     |    CHAR [a-z, A-Z]     | 60      |       NOT NULL        |
|  descricao_missao   |    Atributo que define uma descrição detalhando os objetivos necessários para completar a missão atual     |          TEXT          | -       |       NOT NULL        |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |                 Descrição                 | Autores                                          |
|:----------:|:------:|:-----------------------------------------:|--------------------------------------------------|
| 17/07/2024 | `1.0`  |        Aumenta escopo do projeto.         | [João Antonio G.](https://github.com/joaoseisei) |
| 15/07/2024 | `1.1`  | Adiciona dicionário refatorado de pessoa. | [Fernando Gabriel](https://github.com/show-dawn) |
| 15/07/2024 | `1.2`  |    Termina de refatorar o dicionário.     | [João Antonio G.](https://github.com/joaoseisei) |
| 20/07/2024 | `1.3`  |    Corrige generalizações e abstrações    | [João Antonio G.](https://github.com/joaoseisei) |
| 20/07/2024 | `1.4`  |    Correção dicionário    | [Júlio Cesar](https://github.com/Julio1099), [João Antonio G.](https://github.com/joaoseisei) |

</div>