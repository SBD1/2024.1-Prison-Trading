<center>

# Dicionário de Dados

</center>

Este documento serve como a documentação para o dicionário de dados do sistema.

#### Atalhos:

# Tabela Item

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|      Nome      |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|   nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|   tipo_item    |    Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)    |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|  tamanho_item  |           Atributo que define o espaço que o item ocupará no inventário             |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item |         Atributo que descreve um breve resumo da função do item mencionado          |          TEXT          | -       |       NOT NULL        |

---

# Tabela Instancia_Item

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|      Nome      |                                                 Definição Lógica                                                 | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------:|:----------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_ist, item | Chave composta de nome_inst e item, item é chave primária da tabela Item, ambas sem caracteres especiais (~Ç@!)) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|     lugar      |               Chave estrangeira referenciando a tabela Lugar, Lugar onde a instância de item está                |    CHAR [a-z, A-Z]     | -       |      FOREIGN KEY      |
|   inventario   |          Chave estrangeira referenciando a tabela Inventário, Inventário onde a instância de item está           |         SERIAL         | -       |      FOREIGN KEY      |
|   fabricacao   |       Chave estrangeira referenciando a tabela Fabricação, Fabricação onde a instância de item é utilizada       |    CHAR [a-z, A-Z]     | 25      |      FOREIGN KEY      |

---

# Tabela CEC_Item

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|   Nome    |                                  Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------:|:-----------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_item | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| tipo_item |    Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)    |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |

---

# Tabela Item_Fabricavel

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|      Nome       |                                    Definição Lógica                                    | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:--------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    |  Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!)   |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|    tipo_item    |     Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)      |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|  tamanho_item   |             Atributo que define o espaço que o item ocupará no inventário              |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item  |           Atributo que descreve um breve resumo da função do item mencionado           |          TEXT          | -       |       NOT NULL        |
| tipo_fabricavel | Atributo que define o tipo do item fabricável ('ferr' = ferramenta, 'arma' = arma)     |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |

---

# Tabela CEC_Item_Fabricavel

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|      Nome       |                                   Definição Lógica                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    | Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!)  |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
| tipo_fabricavel | Atributo que define o tipo do item fabricável ('ferr' = ferramenta, 'arma' = arma)   |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |

---

# Tabela Item_Nao_Fabricavel

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|          Nome           |                                              Definição Lógica                                              |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:----------------------------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|        nome_item        |            Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!)             |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
|        tipo_item        |               Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)                |     ENUM('fabr', 'nfab')     | -       |       NOT NULL        |
|      tamanho_item       |                       Atributo que define o espaço que o item ocupará no inventário                        |             INT              | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                     Atributo que descreve um breve resumo da função do item mencionado                     |             TEXT             | -       |       NOT NULL        |
| raridade_nao_fabricavel | Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo  |          INT [0-2]           | -       |  NOT NULL, DEFAULT 0  |
|   tipo_nao_fabricavel   | Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel) | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |

---

# Tabela CEC_Item_Nao_Fabricavel

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|        Nome         |                                              Definição Lógica                                               |    Tipo e Formato de Dado     | Tamanho | Restrições de Domínio |
|:-------------------:|:-----------------------------------------------------------------------------------------------------------:|:-----------------------------:|---------|:---------------------:|
|      nome_item      |             Chave primária que define o nome do item mencionado sem caracteres especiais (~Ç@!)             |        CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
| tipo_nao_fabricavel | Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel)  | ENUM('comi', 'medi', 'util')  | -       |       NOT NULL        |

---

# Tabela Ferramenta

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|         Nome         |                                     Definição Lógica                                      | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------------:|:-----------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|      nome_item       | Chave primária que define o nome da ferramenta mencionada sem caracteres especiais (~Ç@!) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|      tipo_item       |       Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)       |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|     tamanho_item     |               Atributo que define o espaço que o item ocupará no inventário               |          INT           | -       |  NOT NULL, DEFAULT 1  |
|    descricao_item    |            Atributo que descreve um breve resumo da função do item mencionado             |          TEXT          | -       |       NOT NULL        |
|   tipo_fabricavel    |    Atributo que define o tipo do item fabricável ('ferr' = ferramenta, 'arma' = arma)     |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |
| utilidade_ferramenta |                      Atributo que descreve a utilidade da ferramenta                      |          TEXT          | -       |       NOT NULL        |

---

# Tabela Arma

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|      Nome       |                                       Definição Lógica                                       | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------------:|:--------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
|    nome_item    |     Chave primária que define o nome da arma mencionada sem caracteres especiais (~Ç@!)      |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|    tipo_item    |        Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)         |  ENUM('fabr', 'nfab')  | -       |       NOT NULL        |
|  tamanho_item   |                Atributo que define o espaço que o item ocupará no inventário                 |          INT           | -       |  NOT NULL, DEFAULT 1  |
| descricao_item  |              Atributo que descreve um breve resumo da função do item mencionado              |          TEXT          | -       |       NOT NULL        |
| tipo_fabricavel |      Atributo que define o tipo do item fabricável ('ferr' = ferramenta, 'arma' = arma)      |  ENUM('ferr', 'arma')  | -       |       NOT NULL        |
|    dano_arma    |                Atributo que define o dano que uma arma pode dar em uma pessoa                |          INT           | -       |       NOT NULL        |
|  arma_equipada  | Atributo que define se um jogador está com a arma equipada na mão ou escondida no inventário |        BOOLEAN         | -       |       NOT NULL        |

---

# Tabela Comida

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|          Nome           |                                                       Definição Lógica                                                        |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:-----------------------------------------------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|        nome_item        |                     Chave primária que define o nome da comida mencionada sem caracteres especiais (~Ç@!)                     |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
|        tipo_item        |                         Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)                         |     ENUM('fabr', 'nfab')     | -       |       NOT NULL        |
|      tamanho_item       |                                 Atributo que define o espaço que o item ocupará no inventário                                 |             INT              | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                              Atributo que descreve um breve resumo da função do item mencionado                               |             TEXT             | -       |       NOT NULL        |
| raridade_nao_fabricavel |           Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo           |          INT [0-2]           | -       |  NOT NULL, DEFAULT 0  |
|   tipo_nao_fabricavel   |          Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel)           | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |
|    quantidade_comida    |              Atributo que define a quantidade disponivel de uma comida por espaço, (EX: 3 pães ocupam 1 tamanho)              |             INT              | -       |       NOT NULL        |
|    qualidade_comida     | Atributo que define a qualidade da comida, quanto mais qualidade mais vida a comida pode recuperar, (0=ruim, 1=normal, 2=bom) |             INT              | -       |  NOT NULL, DEFAULT 1  |

---

# Tabela Medicamento

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|          Nome           |                                                            Definição Lógica                                                             |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:---------------------------------------------------------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|        nome_item        |                       Chave primária que define o nome do medicamento mencionado sem caracteres especiais (~Ç@!)                        |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
|        tipo_item        |                              Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)                              |     ENUM('fabr', 'nfab')     | -       |       NOT NULL        |
|      tamanho_item       |                                      Atributo que define o espaço que o item ocupará no inventário                                      |             INT              | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                                   Atributo que descreve um breve resumo da função do item mencionado                                    |             TEXT             | -       |       NOT NULL        |
| raridade_nao_fabricavel |                Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo                |          INT [0-2]           | -       |  NOT NULL, DEFAULT 0  |
|   tipo_nao_fabricavel   |               Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel)                | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |
|    cura_medicamento     |                                    Atributo que define quanto de vida um medicamento pode recuperar                                     |             INT              | -       |       NOT NULL        |
|  qualidade_medicamento  | Atributo que define a qualidade do medicamento, quanto mais qualidade mais vida o medicamento pode recuperar, (0=ruim, 1=normal, 2=bom) |             INT              | -       |  NOT NULL, DEFAULT 1  |

---

# Tabela Utilizavel

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|          Nome           |                                              Definição Lógica                                              |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:----------------------------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|        nome_item        |       Chave primária que define o nome do item utilizavel mencionado sem caracteres especiais (~Ç@!)       |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |
|        tipo_item        |               Atributo que define o tipo do item (fabr = fabricável, nfab = não fabricável)                |     ENUM('fabr', 'nfab')     | -       |       NOT NULL        |
|      tamanho_item       |                       Atributo que define o espaço que o item ocupará no inventário                        |             INT              | -       |  NOT NULL, DEFAULT 1  |
|     descricao_item      |                     Atributo que descreve um breve resumo da função do item mencionado                     |             TEXT             | -       |       NOT NULL        |
| raridade_nao_fabricavel | Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo  |          INT [0-2]           | -       |  NOT NULL, DEFAULT 0  |
|   tipo_nao_fabricavel   | Atributo que define o tipo do item fabricável ('comi' = comida, 'medi' = medicamento, 'util' = utilizavel) | ENUM('comi', 'medi', 'util') | -       |       NOT NULL        |
|    efeito_utilizavel    |                              Atributo que define o efeito do item utilizável.                              |             TEXT             | -       |       NOT NULL        |

---

# Tabela Fabricacao

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|             Nome              |                                                                     Definição Lógica                                                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------------------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|:----------------------:|---------|:---------------------:|
| nome_fabri, livro_fabricacoes | Chave composta de nome_fabri e livro_fabricacoes, livro_fabricacoes é chave primária da tabela Livro_Fabricacoes, ambas sem caracteres especiais (~Ç@!)) |    CHAR [a-z, A-Z]     | 25      |      PRIMARY KEY      |
|        item_fabricacao        |                                   Chave estrangeira referenciando a tabela Item_Fabricacao, Item_Fabricacao resultante                                   |    CHAR [a-z, A-Z]     | 25      | FOREIGN KEY, NOT NULL |

---

# Tabela Livro_Fabricacoes

|                 |   |   
|-----------------|---| 
| **Descrição**   | - |
| **Observações** |   | 

|          Nome           |                                     Definição Lógica                                     |    Tipo e Formato de Dado    | Tamanho | Restrições de Domínio |
|:-----------------------:|:----------------------------------------------------------------------------------------:|:----------------------------:|---------|:---------------------:|
|    nome_livro_fabri     | Chave primária que define o nome do Livro de Fabricações sem caracteres especiais (~Ç@!) |       CHAR [a-z, A-Z]        | 25      |      PRIMARY KEY      |

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
| 17/07/2024 | `2.1`  |    Corrige mapeamento de generalização     | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |

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



