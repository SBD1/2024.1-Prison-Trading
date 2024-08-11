<center>

# Normalização

</center>

---

<center>

# O que é?

</center>

> Normalização é uma técnica criada para melhoria do projeto removendo as redundâncias, complexidades desnecessárias e inconsistências.


[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Primeira Forma Normal)

[//]: # ()
[//]: # (</center>)

[//]: # ()
[//]: # (> Para estar na primeira forma normal todos os atributos são Monovalorados e Atômicos.)

[//]: # (>)

[//]: # (> O nosso projeto respeita a primeira forma normal, pois a partir da versão `2.0` removemos os atributos multivalorados de Pessoa e Gangue. Além disso, o projeto não possui atributos compostos.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Segunda Forma Normal)

[//]: # ()
[//]: # (</center>)

[//]: # ()
[//]: # (> Deve estar na 1ª Forma Normal e os atributos comuns não dependem parcialmente de qualquer chave.)

[//]: # (>)

[//]: # (> Única entidade que apresentava esse erro era o Lugar:)

[//]: # ()
[//]: # (### Lugar:)

[//]: # (> descricao_lugar não depende parcialmente de qualquer chave.)

[//]: # (> )

[//]: # (> lugar_anterior depende parcialmente da chave primária.)

[//]: # ()
[//]: # (<div align="center">)

[//]: # (<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/NORM0.png?raw=true"/></div>)

[//]: # (</div>)

[//]: # ()
[//]: # (> Criamos uma tabela associativa para o lugar atual e lugar anterior, ambas sendo chaves estrangeiras de Lugar, isso resolve o problema de um atributo comum depender da chave primária.)

[//]: # ()
[//]: # ()
[//]: # (<div align="center">)

[//]: # (<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/NORM1.png?raw=true"/></div>)

[//]: # (</div>)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Terceira Forma Normal)

[//]: # ()
[//]: # (</center>)

[//]: # ()
[//]: # (> Deve estar na 2ª. Forma Normal, os atributos comuns não dependem transitivamente de qualquer superchave.)

[//]: # (> )

[//]: # (> Possivel erro pode estar em atributos derivados, no projeto existem 2 atributos derivados, o inventario_ocupado da tabela Inventario e respeito_jogador da Tabela Jogador.)

[//]: # (> )

[//]: # (> Decidimos remover o respeito pois o mesmo era redundante, tempo_vida_jogador determinava respeito_jogador, preferimos remover esse elemento.)

[//]: # (> )

[//]: # (> inventario_ocupado não possuia dependencia transitiva de qualquer superchave.)

[//]: # (> )

[//]: # (> Além disso não existe outros atributos comuns com dependencias transitivas de qualquer superchave.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Forma Normal de Boyce-Codd)

[//]: # ()
[//]: # (</center>)

[//]: # ()
[//]: # (> Versão mais abrangente da 2ª. e 3ª Forma Normal. Além disso para estar na forma nomal de Boyce-Codd é necessário que:)

[//]: # ()
[//]: # (* Não existam mais que uma chave candidata.)

[//]: # ()
[//]: # (* Não existam pelo menos duas chaves candidatas compostas.)

[//]: # ()
[//]: # (* Não exista intersceção entre chaves compostas.)

[//]: # ()
[//]: # (> No nosso projeto não possuimos mais que uma chave candidata e não possuimos duas ou mais chaves candidatas compostas, também não existe intersceção entre chaves compostas, como o projeto já estava na 2ª. e 3ª forma normal e ele satisfaz as condições específicas de Boyce-Codd então ele está na forma normal de Boyce-Codd.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Quarta Forma Normal)

[//]: # ()
[//]: # (</center>)

[//]: # ()
[//]: # (> Última forma normal, necessário está na forma normal de Boyce-Codd, além disso não pode ter dependência multivalorada.)

[//]: # (> )

[//]: # (> Embora `Instancia_Item` possa parecer ferir essa forma normal isso não se aplica, pois as chaves estrangeiras da instancia possuem valores únicos, não é possível uma instancia está em uma fabricacao e lugar ao mesmo tempo, isso garante a exclusividade.)

[//]: # (> )

[//]: # (> Nenhuma Tabela possui dependência multivalorada, logo o projeto está na 4ª forma normal.)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (<center>)

[//]: # ()
[//]: # (# Análise de cada tabela)

[//]: # ()
[//]: # (</center>)

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

> id, tipo

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Instancia_Item

> id_item ➡ item, lugar, inventario

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id_item), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Item_Fabricavel

> id, tipo


* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Item_Nao_Fabricavel

> id, tipo

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Ferramenta

> id ➡ nome, tamanho, descricao, utilidade

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Arma

> id ➡ nome, tamanho, dano, descricao

* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A tabela está em 2FN, pois a chave primária id determina todos os outros atributos.
* 3ª Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

# Tabela Comida

> id ➡ nome, tamanho, descricao

* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A tabela está em 2FN, pois a chave primária id determina todos os outros atributos.
* 3ª Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

# Tabela Medicamento

> id ➡ nome, tamanho, descricao


* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A tabela está em 2FN, pois a chave primária id determina todos os outros atributos.
* 3ª Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

# Tabela Utilizavel

> id ➡ nome, tamanho, descricao, durabilidade


* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A tabela está em 2FN, pois a chave primária id determina todos os outros atributos.
* 3ª Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

# Tabela Fabricacao

> id_item_fabricavel ➡ item_fabricavel, livro_fabricacao

1° Forma Normal: Todos os atributos são atômicos e monovalorados.
2° Forma Normal: Há somente um único atributo como chave (id_item_fabricavel), logo não há atributos comuns dependentes parcialmente de uma chave.
3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Lista_Fabricacao

> item, fabricacao ➡ (não possui outros atributos dependentes)

* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A chave composta item, fabricacao determina completamente qualquer outro atributo (no caso, não há outros atributos na tabela).
* 3ª Forma Normal: Não há dependências transitivas porque não há atributos comuns na tabela.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata. Neste caso, a chave composta item, fabricacao é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

# Tabela Livro_Fabricacao

> id ➡ nome

1° Forma Normal: Todos os atributos são atômicos e monovalorados.
2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Prisao

> id ➡ nome, descricao

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Regiao

> id ➡ nome, descricao, prisoes

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Lugar

> id ➡ id_regiao, nome, descricao, regiao


* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há dependências funcionais totais, portanto a tabela está em 2FN.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Lugar_Origem_Destino

> lugar_origem, lugar_destino ➡ (sem atributos adicionais dependentes)

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: A tabela já está em 2FN, pois as dependências funcionais são totais.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Pessoa

> id ➡ tipo

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Inventario

> id_pessoa ➡ pessoa, tamanho, tamanho_ocupado

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id_pessoa), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Prisioneiro

> id ➡ lugar, nome, habilidade_briga, vida, forca, gangue

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Policial

> id ➡ lugar, nome, corrupto

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Informante

> id ➡ lugar, nome, dano

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Jogador

> id  ➡ lugar, missao, nome, habilidade_briga, vida, forca, tempo_vida, gangue, nivel

* 1° Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2° Forma Normal: Há somente um único atributo como chave (id), logo não há atributos comuns dependentes parcialmente de uma chave.
* 3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Inventario

> id_pessoa ➡ pessoa, tamanho, tamanho_ocupado

1° Forma Normal: Todos os atributos são atômicos e monovalorados.
2° Forma Normal: Há somente um único atributo como chave (id_pessoa), logo não há atributos comuns dependentes parcialmente de uma chave.
3° Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
4° Forma Normal: Não há dependências multivaloradas.

---

# Tabela Missao

> id ➡ item_nao_fabricavel, lugar, nome, descricao

* 1ª Forma Normal: Todos os atributos são atômicos e monovalorados.
* 2ª Forma Normal: A tabela está em 2FN, pois a chave primária id determina todos os outros atributos.
* 3ª Forma Normal: Nenhum atributo comum depende transitivamente de qualquer superchave.
* Forma Normal de Boyce-Codd: Para cada dependência funcional, o lado esquerdo é uma chave candidata.
* 4ª Forma Normal: Não há dependências multivaloradas.

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                                     | Autores                                                                                                                                          |
|:----------:|:------:|-----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 19/07/2024 | `1.0`  | Criação do documento.                         | [João Antonio G.](https://github.com/joaoseisei)                                                                                                 |
| 20/07/2024 | `1.1`  | Normalização do projeto.                      | [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 11/08/2024 | `1.2`  | Adiciona informações extras para cada tabela. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                 |

</div>