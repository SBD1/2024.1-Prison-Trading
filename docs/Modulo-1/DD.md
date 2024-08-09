<center>

# Dicionário de Dados

</center>

---

<center>

# O que é?

</center>

> Este documento serve como a documentação para o dicionário de dados do sistema. Ele descreve cada elemento de dados
> utilizado pelo sistema, explicando o que são, onde estão armazenados e como se relacionam.

<div style="margin: 0 auto; width: fit-content;">

| Tabelas                                              |
|:-----------------------------------------------------|
| [Item](#tabela-item)                                 |
| [Instancia_Item](#tabela-instancia_item)             |
| [Item_Fabricavel](#tabela-item_fabricavel)           |
| [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel)   |
| [Ferramenta](#tabela-ferramenta)                     |
| [Arma](#tabela-arma)                                 |
| [Comida](#tabela-comida)                             |
| [Medicamento](#tabela-medicamento)                   |
| [Utilizavel](#tabela-utilizavel)                     |
| [Fabricacao](#tabela-fabricacao)                     |
| [Lista_Fabricacao](#tabela-livro_fabricacao)         |
| [Livro_Fabricacoes](#tabela-livro_fabricacao)        |
| [Prisao](#tabela-prisao)                             |
| [Regiao](#tabela-regiao)                             |
| [Lugar](#tabela-lugar)                               |
| [Lugar_Origem_Destino](#tabela-lugar_origem_destino) |
| [Pessoa](#tabela-pessoa)                             |
| [Inventario](#tabela-inventario)                     |
| [Prisioneiro](#tabela-prisioneiro)                   |
| [Policial](#tabela-policial)                         |
| [Informante](#tabela-informante)                     |
| [Jogador](#tabela-jogador)                           |
| [Missao](#tabela-missao)                             |

</div>

---

# Tabela Item

|                 |                                                                                                                                                                 |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item.                               |
| **Observações** | Tipo possui os valores `fabricavel` para [Item_Fabricavel](#tabela-item_fabricavel) e `nao_fabricavel` para [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel). | 

| Nome | Definição Lógica                                            | Tipo e Formato de Dado               | Tamanho | Restrições de Domínio |
|:-----|:------------------------------------------------------------|:-------------------------------------|---------|:----------------------|
| id   | Chave primária que define o número de identificação do item | SERIAL                               | -       | PRIMARY KEY           |
| tipo | Atributo que define o tipo do item                          | ENUM('fabricavel', 'nao_fabricavel') | -       | NOT NULL              |

---

# Tabela Instancia_Item

|                 |                                                                                                                                        |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Instancia_item é uma entidade fraca que é usada instanciar itens, a mesma é utilizada em Lugar, Inventario e Fabricacao.               |
| **Observações** | Possui as chaves estrangeiras da entidade [Lugar](#tabela-lugar), [Inventario](#tabela-inventario) e [Fabricacao](#tabela-fabricacao). | 

| Nome       | Definição Lógica                                                                                     | Tipo e Formato de Dado | Tamanho | Restrições de Domínio  |
|:-----------|:-----------------------------------------------------------------------------------------------------|:-----------------------|---------|:-----------------------|
| id, item   | Chave composta de id e item, item é chave primária da tabela Item                                    | SERIAL                 | -       | PRIMARY KEY            |
| item       | Chave estrangeira referenciando a tabela Item, Item onde a instância de item está                    | INTEGER                | -       | FOREIGN KEY,  NOT NULL |
| lugar      | Chave estrangeira referenciando a tabela Lugar, Lugar onde a instância de item está                  | INTEGER                | -       | FOREIGN KEY, NULL      |
| inventario | Chave estrangeira referenciando a tabela Inventario, Inventario onde a instância de item é utilizada | INTEGER                | -       | FOREIGN KEY, NULL      |

---------

# Tabela Item_Fabricavel

|                 |                                                                                                                                                         |   
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item_Fabricavel. |
| **Observações** | Tipo possui os valores `ferramenta` para [Ferramenta](#tabela-ferramenta)  e `arma` para [Arma](#tabela-arma).                                          | 

| Nome | Definição Lógica                                                       | Tipo e Formato de Dado     | Tamanho | Restrições de Domínio    |
|:-----|:-----------------------------------------------------------------------|:---------------------------|---------|:-------------------------|
| id   | Chave primária que define o número de identificação do item fabricavel | INTEGER                    | -       | PRIMARY KEY, FOREIGN KEY |
| tipo | Atributo que define o tipo do item fabricável                          | ENUM('ferramenta', 'arma') | -       | NOT NULL                 |

---

# Tabela Item_Nao_Fabricavel

|                 |                                                                                                                                                                            |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar um Item Não Fabricável, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva de Item_Nao_Fabricavel.            |
| **Observações** | Tipo possui os valores `comida` para [Comida](#tabela-comida), `medicamento` para [Medicamento](#tabela-medicamento) e `utilizavel` para [Utilizavel](#tabela-utilizavel). | 

| Nome | Definição Lógica                                                           | Tipo e Formato de Dado                      | Tamanho | Restrições de Domínio    |
|:-----|:---------------------------------------------------------------------------|:--------------------------------------------|---------|:-------------------------|
| id   | Chave primária que define o número de identificação do item não fabricavel | INTEGER                                     | -       | PRIMARY KEY, FOREIGN KEY |
| tipo | Atributo que define o tipo do item não fabricável                          | ENUM('comida', 'medicamento', 'utilizavel') | -       | NOT NULL                 |

---

# Tabela Ferramenta

|                 |                                                                                                                             |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela de ferramentas, que podem ser utilizadas.                                                                            |
| **Observações** | A Tabela [Item_Fabricavel](#tabela-item_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

| Nome      | Definição Lógica                                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio    |
|:----------|:-------------------------------------------------------------------|:-----------------------|---------|:-------------------------|
| id        | Chave primária que define o número de identificação da ferramenta  | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY |
| nome      | Atributo que define o nome da ferramenta mencionada                | CHAR                   | 25      | UNIQUE, NOT NULL         |
| tamanho   | Atributo que define o espaço que o item ocupará no inventário      | SMALLINT               | -       | NOT NULL, DEFAULT 1      |
| descricao | Atributo que descreve um breve resumo da função do item mencionado | TEXT                   | -       | NOT NULL                 |
| utilidade | Atributo que descreve a utilidade da ferramenta                    | TEXT                   | -       | NOT NULL                 |

---

# Tabela Arma

|                 |                                                                                                                             |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela de armas, que podem ser usadas para ferir prisioneiros e jogadores.                                                  |
| **Observações** | A Tabela [Item_Fabricavel](#tabela-item_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

| Nome      | Definição Lógica                                                   | Tipo e Formato de Dado | Tamanho | Restrições de Domínio    |
|:----------|:-------------------------------------------------------------------|:-----------------------|---------|:-------------------------|
| id        | Chave primária que define o número de identificação da arma        | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY |
| nome      | Atributo que define o nome da arma mencionada                      | CHAR                   | 25      | UNIQUE, NOT NULL         |
| tamanho   | Atributo que define o espaço que o item ocupará no inventário      | SMALLINT               | -       | NOT NULL, DEFAULT 1      |
| descricao | Atributo que descreve um breve resumo da função do item mencionado | TEXT                   | -       | NOT NULL                 |
| dano      | Atributo que define o dano que uma arma pode dar em uma pessoa     | SMALLINT               | -       | NOT NULL                 |

---

# Tabela Comida

|                 |                                                                                                                                                            |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar comidas que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados a comida some do inventário do jogador. |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira.                        | 

| Nome       | Definição Lógica                                                                                          | Tipo e Formato de Dado | Tamanho | Restrições de Domínio                                 |
|:-----------|:----------------------------------------------------------------------------------------------------------|:-----------------------|---------|:------------------------------------------------------|
| id         | Chave primária que define o número de identificação da comida                                             | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY                              |
| nome       | Atributo que define o nome da comida mencionada                                                           | CHAR                   | 25      | UNIQUE, NOT NULL                                      |
| tamanho    | Atributo que define o espaço que o item ocupará no inventário                                             | SMALLINT               | -       | NOT NULL, DEFAULT 1                                   |
| descricao  | Atributo que descreve um breve resumo da função do item mencionado                                        | TEXT                   | -       | NOT NULL                                              |
| raridade   | Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo | SMALLINT               | -       | NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2) |
| quantidade | Atributo que define a quantidade disponivel de uma comida por espaço, (EX: 3 pães ocupam 1 tamanho)       | SMALLINT               | -       | NOT NULL                                              |

---

# Tabela Medicamento

|                 |                                                                                                                                                                      |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar medicamentos que podem eventualmente serem utilizados para curar o jogador, caso sejam utilizados o medicamento some do inventário do jogador. |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira.                                  | 

| Nome      | Definição Lógica                                                                                          | Tipo e Formato de Dado | Tamanho | Restrições de Domínio                                 |
|:----------|:----------------------------------------------------------------------------------------------------------|:-----------------------|---------|:------------------------------------------------------|
| id        | Chave primária que define o número de identificação do medicamento                                        | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY                              |
| nome      | Atributo que define o nome do medicamento mencionado                                                      | CHAR                   | 25      | UNIQUE, NOT NULL                                      |
| tamanho   | Atributo que define o espaço que o item ocupará no inventário                                             | SMALLINT               | -       | NOT NULL, DEFAULT 1                                   |
| descricao | Atributo que descreve um breve resumo da função do item mencionado                                        | TEXT                   | -       | NOT NULL                                              |
| raridade  | Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo | SMALLINT               | -       | NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2) |
| cura      | Atributo que define quanto de vida um medicamento pode recuperar                                          | SMALLINT               | -       | NOT NULL                                              |

---

# Tabela Utilizavel

|                 |                                                                                                                                     |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar itens que podem eventualmente serem utilizados, caso sejam utilizados o item some do inventário do jogador.   |
| **Observações** | A Tabela [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel) possui os mesmos nome_item como chave primária e é a chave estrangeira. | 

| Nome             | Definição Lógica                                                                                          | Tipo e Formato de Dado | Tamanho | Restrições de Domínio                                 |
|:-----------------|:----------------------------------------------------------------------------------------------------------|:-----------------------|---------|:------------------------------------------------------|
| id               | Chave primária que define o número de identificação do item utilizável                                    | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY                              |
| nome             | Atributo que define o nome do utilizavel mencionado                                                       | CHAR                   | 25      | UNIQUE, NOT NULL                                      |
| tamanho          | Atributo que define o espaço que o item ocupará no inventário                                             | SMALLINT               | -       | NOT NULL, DEFAULT 1                                   |
| descricao_efeito | Atributo que descreve um breve resumo da função e do efeito, sobre um item mencionado                     | TEXT                   | -       | NOT NULL                                              |
| raridade         | Atributo que define a raridade de um item, podendo ter 3 possiveis valores 0=normal, 1=raro e 2=ultrararo | SMALLINT               | -       | NOT NULL, DEFAULT 0, CHECK (raridade BETWEEN 0 AND 2) |
| quantidade       | Atributo que define a quantidade disponivel de um medicamento por espaço                                  | SMALLINT               | -       | NOT NULL                                              |
| efeito           | Atributo que define o efeito do item utilizável.                                                          | TEXT                   | -       | NOT NULL                                              |

---

# Tabela Fabricacao

|                 |                                                                                                                                                          |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela para armazenar a fabricação de um item fabricável, é uma entidade fraca de [Item_Fabricavel](#tabela-item_fabricavel) (todo item tem fabricação). |
| **Observações** | Possui chave estrangeira de [Livro_Fabricacao](#tabela-livro_fabricacao) e chave composta com [Item_Fabricavel](#tabela-item_fabricavel).                | 

| Nome                | Definição Lógica                                                                                                                         | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| id, item_fabricavel | Chave composta de id e item_fabricavel, item_fabricavel é chave primária da tabela Item_Fabricavel                                       | SERIAL                 | -       | PRIMARY KEY           |
| item_fabricavel     | Chave estrangeira que tem o valor da chave primária de Item_Fabricavel, usada para compor a chave composta                               | INTEGER                | -       | FOREIGN KEY, NOT NULL |
| livro_fabricacao    | Chave estrangeira referenciando a tabela Livro_Fabricacao, livro onde a fabricacao está                                                  | INTEGER                | -       | FOREIGN KEY, NOT NULL |

---
# Tabela Lista_Fabricacao

|                 |                                                                                                                                   |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Lista_Fabricacao é uma tabela que contém informações de cada fabricacao e os itens envolvidos, foi criada uma tabela associativa. |
| **Observações** | Só possui chaves estrangeiras vindo de [Fabricacao](#tabela-fabricacao) e [Item](#tabela-item)                                    |

| Nome       | Definição Lógica                                                                           | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----------|:-------------------------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| fabricacao | Chave estrangeira que tem o valor da chave primária de Fabricacao, resultado da fabricacao | INTEGER                | -       | FOREIGN KEY, NOT NULL |
| item       | Chave estrangeira que tem o valor da chave primária de Item, item usado na fabricacao      | INTEGER                | -       | FOREIGN KEY, NOT NULL |

---

# Tabela Livro_Fabricacao

|                 |                                                                |   
|-----------------|----------------------------------------------------------------| 
| **Descrição**   | É usado para armazenar fabricações (como os itens são feitos). |
| **Observações** | Não possui chave estrangeira.                                  | 

| Nome | Definição Lógica                                                           | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:-----|:---------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| id   | Chave primária que define o número de identificação do livro de fabricação | SERIAL                 | -       | PRIMARY KEY           |
| nome | Atributo que define o nome do livro de fabricação mencionado               | CHAR                   | 25      | UNIQUE, NOT NULL      |

---

# Tabela Prisao

|                 |                                                               |   
|-----------------|---------------------------------------------------------------| 
| **Descrição**   | Prisão é uma tabela que contém informações da prisão do jogo. |
| **Observações** | Não possui chave estrangeira.                                 | 

| Nome     | Definição Lógica                                              | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:---------|:--------------------------------------------------------------|:-----------------------|---------|:----------------------|
| id       | Chave primária que define o número de identificação da prisão | SERIAL                 | -       | PRIMARY KEY           |
| nome     | Atributo que define o nome da prisão                          | CHAR                   | 25      | NOT NULL              |
| objetivo | Atributo que define o objetivo para conseguir fugir da prisão | TEXT                   | -       | NOT NULL              |

---

# Tabela Regiao

|                 |                                                                    |   
|-----------------|--------------------------------------------------------------------| 
| **Descrição**   | Região é uma tabela que contém informações de cada região no jogo. |
| **Observações** | Possui chave estrangeira vindo de [Prisao](#tabela-prisao).        |

| Nome      | Definição Lógica                                                               | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:----------|:-------------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| id        | Chave primária que define o número de identificação da Região                  | SERIAL                 | -       | PRIMARY KEY           |
| nome      | Atributo que define o nome do região mencionado                                | CHAR                   | 25      | UNIQUE, NOT NULL      |
| prisao    | Chave estrangeira vindo de prisão                                              | INTEGER                | -       | FOREIGN KEY, NOT NULL |
| descricao | Atributo contendo uma breve descrição da região mencionada                     | TEXT                   | -       | NOT NULL              |

---

# Tabela Lugar

|                 |                                                                                                                                                    |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Lugar é uma tabela que contém informações de cada local, bem como uma descrição mais especifica, é uma entidade fraca de [Regiao](#tabela-regiao). |
| **Observações** | Possui chave composta vindo de [Regiao](#tabela-regiao).                                                                                           |

| Nome            | Definição Lógica                                                                                                      | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:----------------|:----------------------------------------------------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| id, regiao      | Chave composta de nome_lugar e regiao, regiao é a chave primária de Regiao                                            | SERIAL                 | -       | PRIMARY KEY           |
| nome            | Atributo que define o nome do lugar mencionado                                                                        | CHAR                   | 25      | UNIQUE, NOT NULL      |
| regiao          | Chave estrangeira que tem o valor da chave primária de regiao, usada para compor a chave composta                     | INTEGER                | -       | FOREIGN KEY, NOT NULL |
| descricao_lugar | Atributo que contém uma descrição mais especifica de um lugar, como detalhes do ambiente                              | TEXT                   | -       | NOT NULL              |

---

# Tabela Lugar_Origem_Destino

|                 |                                                                                                                                                    |   
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Lugar_Origem_Destino é uma tabela que contém informações de cada lugar, foi obtido através da 2 forma normal onde é criado uma tabela associativa. |
| **Observações** | Só possui chaves estrangeiras vindo de [Lugar](#tabela-lugar), o lugar de origem e o lugar de destino.                                             |

| Nome          | Definição Lógica                                                                                        | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
|:--------------|:--------------------------------------------------------------------------------------------------------|:-----------------------|---------|:----------------------|
| lugar_origem  | Chave estrangeira que tem o valor da chave primária de lugar, usada para identificar o lugar de origem  | INTEGER                | -       | FOREIGN KEY, NOT NULL |
| lugar_destino | Chave estrangeira que tem o valor da chave primária de lugar, usada para identificar o lugar de destino | INTEGER                | -       | FOREIGN KEY, NOT NULL |

---

# Tabela Pessoa

|                 |                                                                                                                                                                                                                             |   
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Tabela usada para caracterizar uma Pessoa, criada a partir do mapeamento de uma abstração e generalizaçao total e exclusiva.                                                                                                |
| **Observações** | Tipo possui os valores `prisioneiro` para [Prisioneiro](#tabela-prisioneiro), `policia` para [Policial](#tabela-policial), `informante` para [Informante](#tabela-informante) e `jogador` para [Jogador](#tabela-jogador) . | 

| Nome | Definição Lógica                                                                     | Tipo e Formato de Dado                                  | Tamanho | Restrições de Domínio |
|:-----|:-------------------------------------------------------------------------------------|:--------------------------------------------------------|---------|:----------------------|
| id   | Chave primária que define o número de identificação do personagem mencionado         | SERIAL                                                  | -       | PRIMARY KEY           |
| tipo | atributo para identificação de qual tipo de classe o personagem mencionado participa | ENUM('policia', 'prisioneiro', 'informante', 'jogador') | -       | NOT NULL              |

---

# Tabela Inventario

|                 |                                                                                                                                                                         |   
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Inventário é uma tabela que contém informações de cada inventário no jogo, é uma entidade fraca de [Pessoa](#tabela-pessoa), todo inventário está relacionado a pessoa. |
| **Observações** | Possui chave composta vindo de [Pessoa](#tabela-pessoa).                                                                                                                |

| Nome               | Definição Lógica                                                                                                              | Tipo e Formato de Dado | Tamanho | Restrições de Domínio                                |
|:-------------------|:------------------------------------------------------------------------------------------------------------------------------|:-----------------------|---------|:-----------------------------------------------------|
| id, pessoa         | Chave composta de id e pessoa, pessoa é a chave primária de pessoa. Define o número de identificação do inventário mencionado | SERIAL                 | -       | PRIMARY KEY                                          |
| pessoa             | Chave estrangeira que tem o valor da chave primária de pessoa, usada para compor a chave composta                             | INTEGER                | -       | FOREIGN KEY, NOT NULL                                |
| tamanho            | Atributo que define o  tamanho do inventário total do jogador                                                                 | SMALLINT               | -       | NOT NULL, DEFAULT 5                                  |
| inventario_ocupado | Atributo derivado para definir quantos itens tem no invetário                                                                 | SMALLINT               | -       | NOT NULL, CHECK (inventario_ocupado BETWEEN 0 AND 5) |

---

# Tabela Prisioneiro

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Prisioneiro é uma tabela que contém informações especializadas de cada prisioneiro no jogo.                                                                                        |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

| Nome             | Definição Lógica                                                                                               | Tipo e Formato de Dado   | Tamanho | Restrições de Domínio                               |
|:-----------------|:---------------------------------------------------------------------------------------------------------------|:-------------------------|---------|:----------------------------------------------------|
| id               | Chave primária que define o número de identificação do personagem mencionado                                   | INTEGER                  | -       | PRIMARY KEY, FOREIGN KEY                            |
| lugar            | Chave estrangeira vindo de lugar                                                                               | INTEGER                  | -       | FOREIGN KEY, NOT NULL                               |
| nome             | Atributo que define o nome e sobrenome da pessoa mencionada                                                    | CHAR                     | 60      | NOT NULL                                            |
| habilidade_briga | Atributo que define a possível habilidade de luta de um prisioneiro. Multiplica o dano junto do atributo força | SMALLINT                 | -       | NOT NULL, CHECK (habilidade_briga BETWEEN 1 AND 10) |
| vida             | Atributo que determina a quantidade de vida que um prisioneiro possui                                          | SMALLINT                 | -       | NOT NULL, CHECK (vida BETWEEN 1 AND 10)             |
| forca            | Atributo que determina a quantidade de força que um prisioneiro possui                                         | SMALLINT                 | -       | NOT NULL, CHECK (forca BETWEEN 1 AND 10)            |
| gangue           | Atributo que determina qual gangue o prisioneiro é afiliado. tendo 2 opções, polvo e palhaco                   | ENUM('polvo', 'palhaco') | -       | NOT NULL                                            |

---

# Tabela Policial

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Policial é uma tabela que contém informações especializadas de cada policial no jogo.                                                                                              |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

| Nome     | Definição Lógica                                                             | Tipo e Formato de Dado | Tamanho | Restrições de Domínio    |
|:---------|:-----------------------------------------------------------------------------|:-----------------------|---------|:-------------------------|
| id       | Chave primária que define o número de identificação do personagem mencionado | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY |
| lugar    | Chave estrangeira vindo de lugar                                             | INTEGER                | -       | FOREIGN KEY, NOT NULL    |
| nome     | Atributo que define o nome e sobrenome da pessoa mencionada                  | CHAR                   | 60      | NOT NULL                 |
| corrupto | Atributo denomina se um policial é corrupto ou não                           | BOOLEAN                | -       | NOT NULL                 |

---

# Tabela Informante

|                 |                                                                                                                                                                                    |   
|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Informante é uma classe que fica oculta, e quando um jogador tenta atacar ou negociar com o mesmo, sofre uma penalidade em tempo de vida.                                          |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

| Nome  | Definição Lógica                                                             | Tipo e Formato de Dado | Tamanho | Restrições de Domínio    |
|:------|:-----------------------------------------------------------------------------|:-----------------------|---------|:-------------------------|
| id    | Chave primária que define o número de identificação do personagem mencionado | INTEGER                | -       | PRIMARY KEY, FOREIGN KEY |
| lugar | Chave estrangeira vindo de lugar                                             | INTEGER                | -       | FOREIGN KEY, NOT NULL    |
| nome  | Atributo que define o nome e sobrenome da pessoa mencionada                  | CHAR                   | 60      | NOT NULL                 |
| dano  | Atributo inteiro que irá matar instantaneamente um jogador                   | SMALLINT               | -       | NOT NULL, DEFAULT 200    |

---

# Tabela Jogador

|                 |                                                                                                                                                                                                               |   
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Jogador é uma tabela que contém informações especializadas do jogador no jogo.                                                                                                                                |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar) e [Missao](#tabela-missao), além disso id_pessoa é possui a mesma chave primária em [Pessoa](#tabela-pessoa) e possui chave estrangeira com a mesma. |

| Nome             | Definição Lógica                                                                                                   | Tipo e Formato de Dado   | Tamanho | Restrições de Domínio                               |
|:-----------------|:-------------------------------------------------------------------------------------------------------------------|:-------------------------|---------|:----------------------------------------------------|
| id               | Chave primária que define o número de identificação do personagem mencionado                                       | INTEGER                  | -       | PRIMARY KEY, FOREIGN KEY                            |
| lugar            | Chave estrangeira vindo de lugar                                                                                   | INTEGER                  | -       | FOREIGN KEY, NOT NULL                               |
| missao           | Atributo que determina qual a missão atual do jogador                                                              | INTEGER                  | -       | FOREIGN KEY, NOT NULL                               |
| nome             | Atributo que define o nome e sobrenome da pessoa mencionada                                                        | CHAR                     | 60      | NOT NULL                                            |
| habilidade_briga | Atributo que define a possível habilidade de luta de um jogador. Ter conhecimento de boxe contaria como um exemplo | SMALLINT                 | -       | NOT NULL, CHECK (habilidade_briga BETWEEN 1 AND 10) |
| vida             | Atributo que determina a quantidade de vida que um jogador possui                                                  | SMALLINT                 | -       | NOT NULL, CHECK (vida BETWEEN 1 AND 10)             |
| forca            | Atributo que determina a quantidade de força que um jogador possui                                                 | SMALLINT                 | -       | NOT NULL, CHECK (forca BETWEEN 1 AND 10)            |
| tempo_vida       | Atributo que determina quanto tempo de vida restante um jogador possui                                             | SMALLINT                 | -       | NOT NULL, CHECK (tempo_vida BETWEEN 1 AND 10)       |
| gangue           | Atributo que determina qual gangue o jogador é afiliado.  tendo 2 opções, polvo e palhaco                          | ENUM('polvo', 'palhaco') | -       | NOT NULL                                            |

---

# Tabela Missao

|                 |                                                                                                                |   
|-----------------|----------------------------------------------------------------------------------------------------------------| 
| **Descrição**   | Missão é uma tabela que contém informações especializadas de cada missão no jogo.                              |
| **Observações** | Possui chave estrangeira vindo de [Lugar](#tabela-lugar) e [Item_Nao_Fabricavel](#tabela-item_nao_fabricavel). |

| Nome      | Definição Lógica                                                                                           | Tipo e Formato de Dado | Tamanho | Restrições de Domínio |
| :-------- | :--------------------------------------------------------------------------------------------------------- | :--------------------- | ------- | :-------------------- |
| id        | Chave primária que define o número de identificação da missão mencionada                                   | SERIAL                 | -       | PRIMARY KEY           |
| item      | Atributo determina qual a recompensa da missão. A recompensa de uma missão sempre é um item não fabricável | INTEGER                | -       | FOREIGN KEY           |
| lugar     | Chave estrangeira vindo de lugar                                                                           | INTEGER                | -       | FOREIGN KEY           |
| nome      | Atributo que define o nome da missão mencionada                                                            | CHAR                   | 25      | NOT NULL              |
| descricao | Atributo que define uma descrição detalhando os objetivos necessários para completar a missão atual        | TEXT                   | -       | NOT NULL              |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |                 Descrição                 | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:-----------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 17/07/2024 | `1.0`  |        Aumenta escopo do projeto.         | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 15/07/2024 | `1.1`  | Adiciona dicionário refatorado de pessoa. | [Fernando Gabriel](https://github.com/show-dawn)                                                                                                                                                        |
| 15/07/2024 | `1.2`  |    Termina de refatorar o dicionário.     | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 20/07/2024 | `1.3`  |   Corrige generalizações e abstrações.    | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 20/07/2024 | `1.4`  |           Correção dicionário.            | [Júlio Cesar](https://github.com/Julio1099), [João Antonio G.](https://github.com/joaoseisei)                                                                                                           |
| 20/07/2024 | `1.5`  |            Normaliza trabalho.            | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 05/08/2024 | `1.6`  |           Correção dicionário.            | [Júlio Cesar](https://github.com/Julio1099)                                                                                                                                                             |
| 06/08/2024 | `1.8`  |           Altera tipo de dados.           | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |

</div>