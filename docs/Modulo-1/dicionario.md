<center>

# Dicionário de Dados

</center>

Este documento serve como a documentação para o dicionário de dados do sistema.

---

# Tabela Item

|                 |                                                                                                               |   
|-----------------|---------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Item que será utilizado no jogo. Serve como origem para as tabelas `Item_Fabricavel` e `Item_Nao_Fabricavel`. |
| **Observações** | Não possui chaves estrangeiras.                                                                               | 

|      Nome      |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|   tipo_item    |    Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)    |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|  tamanho_item  |            Atributo que define o espaço que o item ocupará no inventário            |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item |         Atributo que descreve um breve resumo da função do item mencionado          |          TEXT          | -       |       NOT NULL        |

---

# Tabela Instancia_Item

|                 |                                                                                                                          |   
|-----------------|--------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Instancia_item é uma entidade fraca que é usada instanciar itens, a mesma é utilizada em Lugar, Inventario e Fabricacao. |
| **Observações** | Possui as chaves estrangeiras da entidade `Lugar`, `Inventario` e `Fabricacao`.                                          | 

|      Nome      |                                                 Definição Lógica                                                 | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------:|:----------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_ist, item | Chave composta de nome_inst e item, item é chave primária da tabela Item, ambas sem caracteres especiais (~Ç@!)) |    CHAR [a-z, A-Z]     | 50      |      PRIMARY KEY      |
|     lugar      |               Chave estrangeira referenciando a tabela Lugar, Lugar onde a instância de item está                |    CHAR [a-z, A-Z]     | -       |      FOREIGN KEY      |
|   inventario   |          Chave estrangeira referenciando a tabela Inventário, Inventário onde a instância de item está           |         SERIAL         | -       |      FOREIGN KEY      |
|   fabricacao   |       Chave estrangeira referenciando a tabela Fabricação, Fabricação onde a instância de item é utilizada       |    CHAR [a-z, A-Z]     | 25      |      FOREIGN KEY      |

---

# Tabela Caracterizador_Item

|                 |                                                                                                                           |   
|-----------------|---------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva. |
| **Observações** | Tipo possui os valores `fabr` para `Item_Fabricavel` e `nfab` para `Item_Nao_Fabricavel`.                                 | 

|   Nome    |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_item | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| tipo_item |                         Atributo que define o tipo do item                          |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |

---

# Tabela Item_Fabricavel

|                 |                               |   
|-----------------|-------------------------------| 
| **Descrição**   | Tabela de itens fabricáveis.  |
| **Observações** | Não possui chave estrangeira. | 

|      Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|    tipo_item    |    Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)    |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|  tamanho_item   |            Atributo que define o espaço que o item ocupará no inventário            |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item  |         Atributo que descreve um breve resumo da função do item mencionado          |          TEXT          | -       |       NOT NULL        |
| tipo_fabricavel | Atributo que define o tipo do item fabricável ('ferr' = ferramenta, 'arma' = arma)  |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |

---

# Tabela Caracterizador_Item_Fabricavel

|                 |                                                                                                                                      |   
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva. |
| **Observações** | Tipo possui os valores `ferr` para `Ferramenta` e `arma` para `Arma`.                                                                | 

|      Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| tipo_fabricavel |                    Atributo que define o tipo do item fabricável                    |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |

---

# Tabela Item_Nao_Fabricavel

|                 |                                                                                                           |   
|-----------------|-----------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela de itens que não podem ser fabricados e só são obtidos através de missão ou encontrando em lugares |
| **Observações** |     Não possui chave estrangeira.                                                                         | 

|          Nome           |                                              Definição Lógica                                               |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|        nome_item        |             Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!)             |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
|      tamanho_item       |                        Atributo que define o espaço que o item ocupará no inventário                        |             INT              | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                     Atributo que descreve um breve resumo da função do item mencionado                      |             TEXT             | -       |       NOT NULL        |
| raridade_nao_fabricavel | Atributo que define a raridade de um item, podendo ter 3 possiveis valores (0=normal, 1=raro e 2=ultrararo) |          INT [0-2]           | -       |  NOT NULL, DEFAULT 0  |
|   tipo_nao_fabricavel   | Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel)  | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |

---

# Tabela Caracterizador_Item_Nao_Fabricavel

|                 |                                                                                                                                          |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Não Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva. |
| **Observações** | Tipo possui os valores `comi` para `Comida`, `medi` para `Medicamento` e `util` para `Utilizavel`.                                       | 

|        Nome         |                                  Definição Lógica                                   |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-------------------:|:-----------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|      nome_item      | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
| tipo_nao_fabricavel |                    Atributo que define o tipo do item fabricável                    | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |

---

# Tabela Ferramenta

|                 |                                                  |   
|-----------------|--------------------------------------------------| 
| **Descrição**   | Tabela de ferramentas, que podem ser utilizadas. |
| **Observações** | Não possui chave estrangeira.                    | 

|         Nome         |                                     Definição Lógica                                      | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------------:|:-----------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|      nome_item       | Chave primária que define o nome da ferramenta mencionada sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|     tamanho_item     |               Atributo que define o espaço que o item ocupará no inventário               |          INT           | -       |  NOT NULL, DEFAULT 1  |
|    descricao_item    |            Atributo que descreve um breve resumo da função do item mencionado             |          TEXT          | -       |       NOT NULL        |
| utilidade_ferramenta |                      Atributo que descreve a utilidade da ferramenta                      |          TEXT          | -       |       NOT NULL        |

---

# Tabela Arma

|                 |                                                                            |   
|-----------------|----------------------------------------------------------------------------| 
| **Descrição**   | Tabela de armas, que podem ser usadas para ferir prisioneiros e jogadores. |
| **Observações** | Não possui chave estrangeira.                                              | 

|      Nome       |                                       Definição Lógica                                       | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:--------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    |     Chave primária que define o nome da arma mencionada sem caracteres especiais (~Ç@!)      |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|  tamanho_item   |                Atributo que define o espaço que o item ocupará no inventário                 |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item  |              Atributo que descreve um breve resumo da função do item mencionado              |          TEXT          | -       |       NOT NULL        |
|    dano_arma    |                Atributo que define o dano que uma arma pode dar em uma pessoa                |          INT           | -       |       NOT NULL        |
|  arma_equipada  | Atributo que define se um jogador está com a arma equipada na mão ou escondida no inventário |        BOOLEAN         | -       |       NOT NULL        |

---

# Tabela Comida

|                 |                                                                                                                                                            |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar comidas que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados a comida some do inventário do jogador. |
| **Observações** | Não possui chave estrangeira.                                                                                                                              | 

|          Nome           |                                                          Definição Lógica                                                          | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------------------:|:----------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|        nome_item        |                       Chave primária que define o nome da comida mencionada sem caracteres especiais (~Ç@!)                        |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|      tamanho_item       |                                   Atributo que define o espaço que o item ocupará no inventário                                    |          INT           | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                                 Atributo que descreve um breve resumo da função do item mencionado                                 |          TEXT          | -       |       NOT NULL        |
| raridade_nao_fabricavel |             Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo              |       INT [0-2]        | -       |  NOT NULL, DEFAULT 0  |
|    quantidade_comida    |                Atributo que define a quantidade disponivel de uma comida por espaço, (EX: 3 pães ocupam 1 tamanho)                 |          INT           | -       |       NOT NULL        |
|    qualidade_comida     | Atributo que define a qualidade da comida, quanto mais qualidade mais vida a comida pode recuperar, (0=normal, 1=bom, 2=excelente) |       INT [0-2]        | -       |  NOT NULL, DEFAULT 0  |

---

# Tabela Medicamento

|                 |                                                                                                                                                                      |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar medicamentos que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados o medicamento some do inventário do jogador. |
| **Observações** | Não possui chave estrangeira.                                                                                                                                        | 

|          Nome           |                                                               Definição Lógica                                                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|        nome_item        |                          Chave primária que define o nome do medicamento mencionado sem caracteres especiais (~Ç@!)                          |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|      tamanho_item       |                                        Atributo que define o espaço que o item ocupará no inventário                                         |          INT           | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                                      Atributo que descreve um breve resumo da função do item mencionado                                      |          TEXT          | -       |       NOT NULL        |
| raridade_nao_fabricavel |                 Atributo que define a raridade de um item, podendo ter 3 possiveis valores (0=normal, 1=raro e 2=ultrararo)                  |       INT [0-2]        | -       |  NOT NULL, DEFAULT 0  |
|    cura_medicamento     |                                       Atributo que define quanto de vida um medicamento pode recuperar                                       |          INT           | -       |       NOT NULL        |
|  qualidade_medicamento  | Atributo que define a qualidade do medicamento, quanto mais qualidade mais vida o medicamento pode recuperar, (0=normal, 1=bom, 2=excelente) |       INT [0-2]        | -       |  NOT NULL, DEFAULT 0  |

---

# Tabela Utilizavel

|                 |                                                                                                                                   |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar itens que podem eventualmente serem utilizados, caso sejam utilizados o item some do inventário do jogador. |
| **Observações** | Não possui chave estrangeira.                                                                                                     | 

|          Nome           |                                              Definição Lógica                                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|        nome_item        |       Chave primária que define o nome do item utilizavel mencionado sem caracteres especiais (~Ç@!)        |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|      tamanho_item       |                        Atributo que define o espaço que o item ocupará no inventário                        |          INT           | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                     Atributo que descreve um breve resumo da função do item mencionado                      |          TEXT          | -       |       NOT NULL        |
| raridade_nao_fabricavel | Atributo que define a raridade de um item, podendo ter 3 possiveis valores (0=normal, 1=raro e 2=ultrararo) |       INT [0-2]        | -       |  NOT NULL, DEFAULT 0  |
|    efeito_utilizavel    |                              Atributo que define o efeito do item utilizável.                               |          TEXT          | -       |       NOT NULL        |

---

# Tabela Fabricacao

|                 |                                                                                                                               |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar a fabricação de um item fabricável, é uma entidade fraca de Item_Fabricavel (todo item tem fabricação). |
| **Observações** | Possui chave estrangeira de `Item_Fabricavel`.                                                                                | 

|             Nome              |                                                                     Definição Lógica                                                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_fabri, livro_fabricacoes | Chave composta de nome_fabri e livro_fabricacoes, livro_fabricacoes é chave primária da tabela Livro_Fabricacoes, ambas sem caracteres especiais (~Ç@!)) |    CHAR [a-z, A-Z]     | 50      |      PRIMARY KEY      |
|        item_fabricacao        |                                   Chave estrangeira referenciando a tabela Item_Fabricacao, Item_Fabricacao resultante                                   |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

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
| **Observações** | Possui chave estrangeira vindo de `Prisao`.                        |

|       Nome       |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:----------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   nome_regiao    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| descricao_regiao |             Atributo contendo uma breve descrição da região mencionada              |          TEXT          | -       |       NOT NULL        |
|      prisao      |                          Chave estrangeira vindo de prisão                          |         SERIAL         | -       | FOREIGN KEY, NOT NULL |

---

# Tabela Lugar

|                 |                                                                                                  |   
|-----------------|--------------------------------------------------------------------------------------------------| 
| **Descrição**   | Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica. |
| **Observações** | Possui chave estrangeira vindo de `Regiao`.                                                      |

|      Nome       |                                                     Definição Lógica                                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   nome_lugar    |                         Chave primaria nome do lugar mencionado sem caracteres especiais  (~Ç@!)                         |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| descricao_lugar | Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente sem caracteres especiais (~Ç@!) |          TEXT          | -       |       NOT NULL        |
| lugar_anterior  |                                  Atributo que contém o lugar de origem, sala de origem                                   |    CHAR  [a-z, A-Z]    | 25      |       NOT NULL        |
|     regiao      |                       Chave estrangeira que contém o nome da região na qual aquele lugar pertence                        |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Pessoa

|                 |                                                                                  |   
|-----------------|----------------------------------------------------------------------------------| 
| **Descrição**   | Pessoa é uma tabela que contém informações generalizadas de cada pessoa no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Lugar`.                                       |

|    Nome     |                                                                        Definição Lógica                                                                        |        Tipo e Formato de Dado        | Tamanho | Restrições de Domínio |
|:-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------:|---------|:---------------------:|
|  id_pessoa  |                                          Chave primária que define o número de identificação do personagem mencionado                                          |                SERIAL                | -       |      PRIMARY KEY      |
| nome_pessoa |                                                  Atributo que define o nome e sobrenome da pessoa mencionada                                                   |           CHAR [a-z, A-Z]            | 60      |       NOT NULL        |
| tipo_pessoa | Atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador) | ENUM('poli', 'pris', 'info', 'joga') | -       |       NOT NULL        |
|    lugar    |                                                                Chave estrangeira vindo de lugar                                                                |           CHAR  [a-z, A-Z]           | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Caracterizador_Pessoa

|                 |                                                                                                                              |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar uma Pessoa, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva. |
| **Observações** | Tipo possui os valores `poli` para `Policial`, `pris` para `Prisioneiro`, `info` para `Informante` e `joga` para `Jogador`.  | 

|    Nome     |                                                                        Definição Lógica                                                                        |        Tipo e Formato de Dado        | Tamanho | Restrições de Domínio |
|:-----------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------:|:------------------------------------:|---------|:---------------------:|
|  id_pessoa  |                                          Chave primária que define o número de identificação do personagem mencionado                                          |                SERIAL                | -       |      PRIMARY KEY      |
| tipo_pessoa | atributo para identificação de qual tipo de classe o personagem mencionado participa. (poli = policial, pris = prisioneiro, info = informante, joga = jogador) | ENUM('poli', 'pris', 'info', 'joga') | -       |       NOT NULL        |

---

# Tabela Inventario

|                 |                                                                            |   
|-----------------|----------------------------------------------------------------------------| 
| **Descrição**   | Inventário é uma tabela que contém informações de cada inventário no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Pessoa`.                                |

|        Nome        |                               Definição Lógica                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:------------------:|:----------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   id_inventario    | Chave primária que define o número de identificação do inventário mencionado |         SERIAL         | -       |      PRIMARY KEY      |
| tamanho_inventario |        Atributo que define o  tamanho do inventário total do jogador         |       INT [1-5]        | -       |       NOT NULL        |
| inventario ocupado |   Atributo derivado para a identificação se o inventário está cheio ou não   |        BOOLEAN         | -       |       NOT NULL        |
|       pessoa       |                      Chave estrangeira vindo de pessoa                       |         SERIAL         | -       | FOREIGN KEY, NOT NULL |

---

# Tabela Prisioneiro

|                 |                                                                                             |   
|-----------------|---------------------------------------------------------------------------------------------| 
| **Descrição**   | Prisioneiro é uma tabela que contém informações especializadas de cada prisioneiro no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Lugar`.                                                  |

|             Nome             |                                                Definição Lógica                                                |        Tipo e Formato de Dado         | Tamanho | Restrições de Domínio |
|:----------------------------:|:--------------------------------------------------------------------------------------------------------------:|:-------------------------------------:|---------|:---------------------:|
|          id_pessoa           |                  Chave primária que define o número de identificação do personagem mencionado                  |                SERIAL                 | -       |      PRIMARY KEY      |
|         nome_pessoa          |                          Atributo que define o nome e sobrenome da pessoa mencionada                           |            CHAR [a-z, A-Z]            | 60      |       NOT NULL        |
|      gangue_prisioneiro      |          Atributo que determina qual gangue o prisioneiro é afiliado. tendo 2 opções, polvo e palhaço          |      ENUM ( 'polvo', 'palhaco')       | -       |       NOT NULL        |
| habilidade_briga_prisioneiro | Atributo que define a possível habilidade de luta de um prisioneiro. Multiplica o dano junto do atributo força |              INT [1-10]               | -       |       NOT NULL        |
|       vida_prisioneiro       |                     Atributo que determina a quantidade de vida que um prisioneiro possui                      |              INT [1-10]               | -       |       NOT NULL        |
|      força_prisioneiro       |                     Atributo que determina a quantidade de força que um prisioneiro possui                     |              INT  [1-10]              | -       |       NOT NULL        |
|            lugar             |                                        Chave estrangeira vindo de lugar                                        |                 CHAR                  | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Policial

|                 |                                                                                       |   
|-----------------|---------------------------------------------------------------------------------------| 
| **Descrição**   | Policial é uma tabela que contém informações especializadas de cada policial no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Lugar`.                                            |

|       Nome        |                               Definição Lógica                               |        Tipo e Formato de Dado        | Tamanho | Restrições de Domínio |
|:-----------------:|:----------------------------------------------------------------------------:|:------------------------------------:|---------|:---------------------:|
|     id_pessoa     | Chave primária que define o número de identificação do personagem mencionado |                SERIAL                | -       |      PRIMARY KEY      |
|    nome_pessoa    |         Atributo que define o nome e sobrenome da pessoa mencionada          |           CHAR [a-z, A-Z]            | 60      |       NOT NULL        |
| policial_corrupto |              Atributo denomina se um policial é corrupto ou não              |               BOOLEAN                | -       |       NOT NULL        |
|       lugar       |                       Chave estrangeira vindo de lugar                       |          CHAR   [a-z, A-Z]           | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Informante

|                 |                                                                                                                                           |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Informante é uma classe que fica oculta, e quando um jogador tenta atacar ou negociar com o mesmo, sofre uma penalidade em tempo de vida. |
| **Observações** | Possui chave estrangeira vindo de `Lugar`.                                                                                                |

|    Nome     |                               Definição Lógica                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------:|:----------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|  id_pessoa  | Chave primária que define o número de identificação do personagem mencionado |         SERIAL         | -       |      PRIMARY KEY      |
| nome_pessoa |         Atributo que define o nome e sobrenome da pessoa mencionada          |    CHAR [a-z, A-Z]     | 60      |       NOT NULL        |
|  dano_info  |          Atributo inteiro que irá matar instantaneamente um jogador          |          INT           | -       | NOT NULL, DEFAULT 200 |
|    lugar    |                       Chave estrangeira vindo de lugar                       |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Jogador

|                 |                                                                                |   
|-----------------|--------------------------------------------------------------------------------| 
| **Descrição**   | Jogador é uma tabela que contém informações especializadas do jogador no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Lugar` e `Missao`.                          |

|           Nome           |                                                  Definição Lógica                                                  |   Tipo e Formato de Dado   | Tamanho | Restrições de Domínio |
|:------------------------:|:------------------------------------------------------------------------------------------------------------------:|:--------------------------:|---------|:---------------------:|
|        id_pessoa         |                    Chave primária que define o número de identificação do personagem mencionado                    |           SERIAL           | -       |      PRIMARY KEY      |
|       nome_pessoa        |                            Atributo que define o nome e sobrenome da pessoa mencionada                             |      CHAR [a-z, A-Z]       | 60      |       NOT NULL        |
| habilidade_briga_jogador | Atributo que define a possível habilidade de luta de um jogador. Ter conhecimento de boxe contaria como um exemplo |         INT [1-10]         | -       |       NOT NULL        |
|       vida_jogador       |                         Atributo que determina a quantidade de vida que um jogador possui                          |         INT [1-10]         | -       |       NOT NULL        |
|      força_jogador       |                         Atributo que determina a quantidade de força que um jogador possui                         |         INT [1-10]         | -       |       NOT NULL        |
|     respeito_jogador     |                         Atributo derivado que determina quanto respeito um jogador possui                          |         INT [1-10]         | -       |       NOT NULL        |
|    tempo_vida_jogador    |                       Atributo que determina quanto tempo de vida restante um jogador possui                       |         INT [1-10]         | -       |       NOT NULL        |
|      gangue_jogador      |             Atributo que determina qual gangue o jogador é afiliado.  tendo 2 opções, polvo e palhaço              | ENUM  ('polvo', 'palhaco') | -       |       NOT NULL        |
|          missao          |                               Atributo que determina qual a missão atual do jogador                                |      CHAR [a-z, A-Z]       | 25      | FOREIGN KEY, NOT NULL |
|          lugar           |                                          Chave estrangeira vindo de lugar                                          |      CHAR [a-z, A-Z]       | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Missão

|                 |                                                                                   |   
|-----------------|-----------------------------------------------------------------------------------| 
| **Descrição**   | Missão é uma tabela que contém informações especializadas de cada missão no jogo. |
| **Observações** | Possui chave estrangeira vindo de `Lugar` e `Item_Nao_Fabricavel`.                |

|        Nome         |                                              Definição Lógica                                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|      id_missao      |                  Chave primária que define o número de identificação da missão mencionada.                  |         SERIAL         | -       |      PRIMARY KEY      |
|     nome_missao     |                    Atributo que define o nome da missão sem caracteres especiais (~ç@!)                     |    CHAR [a-z, A-Z]     | 60      |       NOT NULL        |
|  descricao_missao   |    Atributo que define uma descrição detalhando os objetivos necessários para completar a missão atual.     |          TEXT          | -       |       NOT NULL        |
| Item_Nao_Fabricavel | Atributo determina qual a recompensa da missão. A recompensa de uma missão sempre é um item não fabricável. |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |
|        lugar        |                                      Chave estrangeira vindo de lugar                                       |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

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