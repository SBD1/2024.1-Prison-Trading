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

> id ➡ tipo

* **1ª Forma Normal (1FN)**: Na 1FN, cada campo da tabela deve conter apenas um único valor indivisível, e todos os registros da tabela devem ter a mesma estrutura, sem repetições de grupos de atributos. E na tabela item, os atributos `id` e `tipo` atendem a esse critério, garantindo que ela esteja na 1ª Forma Normal.
* **2ª Forma Normal (2FN)**: Para estar em 2FN, é necessário que não haja dependências parciais, ou seja, todos os atributos não-chave devem depender da totalidade da chave primária. Como a tabela possui apenas uma chave primária simples (`id`), e `tipo` depende inteiramente de `id`, a tabela está conforme a 2ª Forma Normal.
* **3ª Forma Normal (3FN)**: Na 3FN, deve-se garantir que todos os atributos não-chave sejam diretamente dependentes da chave primária, sem intermediários. E na tabela item, o atributo `tipo` depende diretamente do `id`, atendendo ao critério da 3ª Forma Normal.
* **Forma Normal de Boyce-Codd (FNBC)**: A FNBC é uma versão mais rigorosa da 3ª Forma Normal. Nela, é exigido que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela item, `id` é uma superchave, garantindo que a FNBC seja cumprida.
* **4ª Forma Normal (4FN)**:  A 4FN exige que não existam dependências multivaloradas, onde um único atributo poderia ser relacionado a múltiplos valores de outro atributo de forma independente. A tabela item, com atributos atômicos e monovalorados, não apresenta tais dependências, satisfazendo assim a 4ª Forma Normal.

---

# Tabela Instancia_Item

> (id, item) ➡ lugar, inventario

* **1ª Forma Normal (1FN)**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela Instancia_Item, todos os atributos (`id`, `item`, `lugar`, `inventario`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.
* **2ª Forma Normal (2FN)**:A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela Instancia_Item, a chave primária composta (`id`, `item`) garante que `lugar` e `inventario` dependam tanto de `id` quanto de `item`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.
* **3ª Forma Normal (3FN)**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela Instancia_Item, `lugar` e `inventario` dependem diretamente da chave primária composta (`id`, `item`), atendendo ao critério da 3ª Forma Normal.
* **Forma Normal de Boyce-Codd (FNBC)**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela Instancia_Item, a chave composta (`id`, `item`) é uma superchave, e não há dependências funcionais violando essa regra. Portanto, a tabela atende à FNBC.
* **4ª Forma Normal (4FN)**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela Instancia_Item, todos os atributos são atômicos e não há tais dependências, satisfazendo assim a 4ª Forma Normal.

---

# Tabela Item_Fabricavel

> id ➡ tipo

* **1ª Forma Normal (1FN)**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Item_Fabricavel`, todos os atributos (`id`, `tipo`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.
* **2ª Forma Normal (2FN)**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Item_Fabricavel`, a chave primária simples `id` garante que o atributo `tipo` dependa completamente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.
* **3ª Forma Normal (3FN)**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Item_Fabricavel`, `tipo` depende diretamente da chave primária `id`, atendendo ao critério da 3ª Forma Normal.
* **Forma Normal de Boyce-Codd (FNBC)**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Item_Fabricavel`, `id` é uma superchave e determina `tipo`, garantindo que a tabela esteja em conformidade com a FNBC.
* **4ª Forma Normal (4FN)**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Item_Fabricavel`, todos os atributos são atômicos e não há tais dependências, satisfazendo assim a 4ª Forma Normal.

---

# Tabela Item_Nao_Fabricavel

> id ➡ tipo

* **1° Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Item_Nao_Fabricavel`, todos os atributos (`id`, `tipo`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2° Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Item_Nao_Fabricavel`, a chave primária é o atributo `id`, e `tipo` depende inteiramente de `id`, garantindo que a tabela esteja em conformidade com a 2ª Forma Normal.

* **3° Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Item_Nao_Fabricavel`, `tipo` depende diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Item_Nao_Fabricavel`, `id` é uma chave candidata, e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4° Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Item_Nao_Fabricavel`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Ferramenta

> id ➡ nome, tamanho, descricao, utilidade

* **1° Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Ferramenta`, todos os atributos (`id`, `nome`, `tamanho`, `descricao`, `utilidade`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2° Forma Normal**: A 2FN requer que não existam dependências parciais, ou seja, todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Ferramenta`, a chave primária é o atributo `id`, e todos os atributos (`nome`, `tamanho`, `descricao`, `utilidade`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3° Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Ferramenta`, todos os atributos (`nome`, `tamanho`, `descricao`, `utilidade`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Ferramenta`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4° Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Ferramenta`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Arma

> id ➡ nome, tamanho, descricao, dano

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Arma`, todos os atributos (`id`, `nome`, `tamanho`, `descricao`, `dano`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Arma`, a chave primária é o atributo `id`, e todos os atributos (`nome`, `tamanho`, `descricao`, `dano`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Arma`, todos os atributos (`nome`, `tamanho`, `descricao`, `dano`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Arma`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Arma`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.

---

# Tabela Comida

> id ➡ nome, tamanho, descricao, raridade, quantidade, recuperacao_vida

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Comida`, todos os atributos (`id`, `nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `recuperacao_vida`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Comida`, a chave primária é o atributo `id`, e todos os atributos (`nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `recuperacao_vida`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Comida`, todos os atributos (`nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `recuperacao_vida`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Comida`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Comida`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.

---

# Tabela Medicamento

> id ➡ nome, tamanho, descricao, raridade, quantidade, cura

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Medicamento`, todos os atributos (`id`, `nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `cura`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Medicamento`, a chave primária é o atributo `id`, e todos os atributos (`nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `cura`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Medicamento`, todos os atributos (`nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `cura`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Medicamento`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Medicamento`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Utilizavel

> id ➡ nome, tamanho, descricao, raridade, quantidade, durabilidade

* **1ª Forma Normal**: Na 1FN, cada atributo da tabela deve ser atômico e não deve haver atributos repetidos ou multivalorados. Na tabela `Utilizavel`, todos os atributos são atômicos e cada célula contém apenas um valor único e indivisível, garantindo conformidade com a 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que todos os atributos não-chave dependam da totalidade da chave primária. Como `id` é a chave primária e todos os atributos (`nome`, `tamanho`, `descricao`, `raridade`, `quantidade`, `durabilidade`) dependem diretamente de `id`, a tabela está na 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, todos os atributos não-chave devem depender diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Utilizavel`, todos os atributos dependem diretamente de `id`, sem dependência transitiva, garantindo que a tabela esteja na 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que cada dependência funcional tenha um lado esquerdo que seja uma chave candidata. A tabela `Utilizavel` está em conformidade com a FNBC, pois `id` é uma chave candidata e todas as dependências funcionais possuem `id` no lado esquerdo.

* **4ª Forma Normal**: A 4FN exige a ausência de dependências multivaloradas, onde um atributo pode ter múltiplos valores independentes. Na tabela `Utilizavel`, todos os atributos são atômicos e não há dependências multivaloradas, atendendo assim à 4ª Forma Normal.

---

# Tabela Fabricacao

> (id, item_fabricavel) livro_fabricacao

* **1ª Forma Normal**: Na 1ª Forma Normal, todos os atributos devem ser atômicos e monovalorados. A tabela `Fabricacao` atende a essa forma, pois todos os atributos são únicos e indivisíveis.

* **2ª Forma Normal**: A 2ª Forma Normal exige que todos os atributos não-chave dependam da totalidade da chave primária. A chave primária composta é `(id, item_fabricavel)`. Todos os atributos (`item_fabricavel`, `livro_fabricacao`) dependem completamente desta chave composta, satisfazendo a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal requer que não haja dependências transitivas de atributos não-chave sobre a chave primária. Na tabela `Fabricacao`, `item_fabricavel` e `livro_fabricacao` são totalmente dependentes da chave primária composta `(id, item_fabricavel)`, e não há dependências transitivas, atendendo assim à 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Fabricacao`, as dependências funcionais são compostas pela chave primária `(id, item_fabricavel)` e todos os atributos são diretamente dependentes desta chave, atendendo à FNBC.

* **4ª Forma Normal**: A 4ª Forma Normal lida com a eliminação de dependências multivaloradas. Na tabela `Fabricacao`, não há atributos que possam ter múltiplos valores independentes, então a tabela está em conformidade com a 4ª Forma Normal.

---

# Tabela Lista_Fabricacao

> item, fabricacao ➡ (não possui outros atributos dependentes)

* **1ª Forma Normal**: A 1ª Forma Normal exige que todos os atributos sejam atômicos e monovalorados. A tabela `Lista_Fabricacao` atende a essa forma, pois `fabricacao` e `item` são ambos valores atômicos e não compostos.

* **2ª Forma Normal**: A 2ª Forma Normal requer que todos os atributos não-chave dependam da totalidade da chave primária. A tabela `Lista_Fabricacao` possui uma chave composta (`fabricacao`, `item`), e todos os atributos (`fabricacao`, `item`) são totalmente dependentes dessa chave composta, portanto, atende à 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Lista_Fabricacao`, não há atributos não-chave adicionais, então não há dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Lista_Fabricacao`, a chave composta (`fabricacao`, `item`) é uma chave candidata e todas as dependências funcionais são baseadas nela. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Lista_Fabricacao` não possui atributos que possam ter múltiplos valores independentes e, portanto, está em conformidade com a 4ª Forma Normal.

---

# Tabela Livro_Fabricacao

> id ➡ nome

* **1ª Forma Normal**: A 1ª Forma Normal exige que todos os atributos sejam atômicos e monovalorados. A tabela `Livro_Fabricacao` atende a essa forma, pois `id` e `nome` são ambos valores atômicos e não compostos.

* **2ª Forma Normal**: A 2ª Forma Normal requer que todos os atributos não-chave dependam da totalidade da chave primária. A tabela `Livro_Fabricacao` possui uma única chave primária (`id`), e o atributo `nome` depende totalmente dessa chave primária. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Livro_Fabricacao`, não há atributos não-chave adicionais, então não há dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Livro_Fabricacao`, a chave primária `id` é uma chave candidata e todas as dependências funcionais são baseadas nela. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Livro_Fabricacao` não possui atributos que possam ter múltiplos valores independentes e, portanto, está em conformidade com a 4ª Forma Normal.


---

# Tabela Prisao

> id, nome, descricao, motim

* **1ª Forma Normal**: A 1ª Forma Normal exige que todos os atributos sejam atômicos e monovalorados. A tabela `Prisao` atende a essa forma, pois `id`, `nome` e `descricao` são valores atômicos e não compostos.

* **2ª Forma Normal**: A 2ª Forma Normal requer que todos os atributos não-chave dependam da totalidade da chave primária. A tabela `Prisao` possui uma única chave primária (`id`), e os atributos `nome` e `descricao` dependem totalmente dessa chave primária. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Prisao`, não há atributos não-chave adicionais, então não há dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Prisao`, a chave primária `id` é uma chave candidata e todas as dependências funcionais são baseadas nela. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Prisao` não possui atributos que possam ter múltiplos valores independentes e, portanto, está em conformidade com a 4ª Forma Normal.


---

# Tabela Regiao

> id ➡ nome, descricao, prisao

* **1ª Forma Normal**: A 1ª Forma Normal requer que todos os atributos sejam atômicos e monovalorados. A tabela `Regiao` está em conformidade com esta forma, pois `id`, `nome`, `descricao` e `prisao` são valores atômicos e não compostos.

* **2ª Forma Normal**: A 2ª Forma Normal exige que todos os atributos não-chave dependam completamente da chave primária. A tabela `Regiao` possui uma única chave primária (`id`), e os atributos `nome`, `descricao` e `prisao` dependem completamente dessa chave primária. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Regiao`, não há atributos adicionais além da chave primária `id` e os atributos dependentes, então não há dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Regiao`, a chave primária `id` é uma chave candidata e todas as dependências funcionais são baseadas nela. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Regiao` não possui atributos que possam ter múltiplos valores independentes, então está em conformidade com a 4ª Forma Normal.

---

# Tabela Lugar

> (id, regiao) ➡ nome, descricao, rota_final_fuga

* **1ª Forma Normal**: A 1ª Forma Normal requer que todos os atributos sejam atômicos e monovalorados. A tabela `Lugar` está em conformidade com esta forma, pois `id`, `nome`, `descricao` e `regiao` são valores atômicos e não compostos.

* **2ª Forma Normal**: A 2ª Forma Normal exige que todos os atributos não-chave dependam completamente da chave primária. A tabela `Lugar` possui uma chave composta `(id, regiao)`, e os atributos `nome` e `descricao` dependem completamente dessa chave composta. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Lugar`, todos os atributos dependem diretamente da chave composta `(id, regiao)`, e não há atributos adicionais que introduzam dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. A chave composta `(id, regiao)` é uma chave candidata para todas as dependências funcionais na tabela `Lugar`, e todas as dependências funcionais são baseadas nela. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Lugar` não possui atributos que possam ter múltiplos valores independentes, então está em conformidade com a 4ª Forma Normal.


---

# Tabela Lugar_Origem_Destino

> (lugar_origem, lugar_destino) ➡ (sem atributos adicionais dependentes)

* **1ª Forma Normal**: A 1ª Forma Normal exige que todos os atributos sejam atômicos e monovalorados. A tabela `Lugar_Origem_Destino` está em conformidade com esta forma, pois `lugar_origem` e `lugar_destino` são valores atômicos e não compostos. Cada célula da tabela contém apenas um valor único.

* **2ª Forma Normal**: A 2ª Forma Normal requer que todos os atributos não-chave dependam completamente da chave primária. A tabela `Lugar_Origem_Destino` tem uma chave primária composta `(lugar_origem, lugar_destino)`, e não há atributos adicionais na tabela além dessa chave. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: A 3ª Forma Normal afirma que não deve haver dependências transitivas entre atributos não-chave e a chave primária. Na tabela `Lugar_Origem_Destino`, não há atributos não-chave adicionais; todos os atributos são parte da chave primária composta. Assim, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A Forma Normal de Boyce-Codd exige que, para cada dependência funcional, o lado esquerdo seja uma chave candidata. Na tabela `Lugar_Origem_Destino`, a chave primária composta `(lugar_origem, lugar_destino)` é uma chave candidata para todas as dependências funcionais, e não há outras dependências funcionais a considerar. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: A 4ª Forma Normal trata de dependências multivaloradas. A tabela `Lugar_Origem_Destino` não possui atributos que possam ter múltiplos valores independentes; cada combinação de `lugar_origem` e `lugar_destino` é única. Portanto, a tabela está em conformidade com a 4ª Forma Normal.

---

# Tabela Pessoa

> id, tipo

* **1ª Forma Normal**: Todos os atributos são atômicos e monovalorados. A tabela `Pessoa` está em conformidade com esta forma, pois `id` e `tipo` são valores atômicos e não compostos.

* **2ª Forma Normal**: Há somente um único atributo como chave (`id`), logo não há atributos comuns dependentes parcialmente de uma chave. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Nenhum atributo comum depende transitivamente de qualquer superchave. Na tabela `Pessoa`, `tipo` não depende de `id` de forma transitiva. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: Para cada dependência funcional, o lado esquerdo é uma chave candidata. A chave primária `id` é uma chave candidata para todas as dependências funcionais na tabela `Pessoa`. Portanto, a tabela atende à Forma Normal de Boyce-Codd.

* **4ª Forma Normal**: Não há dependências multivaloradas na tabela `Pessoa`. Cada valor de `id` corresponde a um único valor de `tipo`, sem múltiplos valores independentes. Portanto, a tabela está em conformidade com a 4ª Forma Normal.


---

# Tabela Inventario

> (id, pessoa) ➡ tamanho, inventario_ocupado

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Inventario`, todos os atributos (`id`, `pessoa`, `tamanho`, `inventario_ocupado`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, ou seja, todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Inventario`, a chave primária é composta por `(id, pessoa)`, e todos os atributos (`tamanho`, `inventario_ocupado`) dependem inteiramente dessa chave composta. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Inventario`, todos os atributos (`tamanho`, `inventario_ocupado`) dependem diretamente da chave composta `(id, pessoa)`, sem introduzir dependências transitivas. Portanto, a tabela está em conformidade com a 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Inventario`, a chave composta `(id, pessoa)` é uma superchave, e todas as dependências funcionais têm `(id, pessoa)` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Inventario`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Prisioneiro

> id, lugar, nome, habilidade_briga, vida, forca, gangue

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Prisioneiro`, todos os atributos (`id`, `lugar`, `nome`, `habilidade_briga`, `vida`, `forca`, `gangue`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Prisioneiro`, a chave primária é o atributo `id`, e todos os atributos (`lugar`, `nome`, `habilidade_briga`, `vida`, `forca`, `gangue`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Prisioneiro`, todos os atributos (`lugar`, `nome`, `habilidade_briga`, `vida`, `forca`, `gangue`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Prisioneiro`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Prisioneiro`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Policial

> id, lugar, nome, corrupto

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Policial`, todos os atributos (`id`, `lugar`, `nome`, `corrupto`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Policial`, a chave primária é o atributo `id`, e todos os atributos (`lugar`, `nome`, `corrupto`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Policial`, todos os atributos (`lugar`, `nome`, `corrupto`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Policial`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Policial`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Informante

> id, lugar, nome, dano

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Informante`, todos os atributos (`id`, `lugar`, `nome`, `dano`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Informante`, a chave primária é o atributo `id`, e todos os atributos (`lugar`, `nome`, `dano`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Informante`, todos os atributos (`lugar`, `nome`, `dano`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Informante`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Informante`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Jogador

> id, lugar, missao, nome, habilidade_briga, vida, forca, tempo_vida, gangue, nivel

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Jogador`, todos os atributos (`id`, `lugar`, `missao`, `nome`, `habilidade_briga`, `vida`, `forca`, `tempo_vida`, `gangue`, `nivel`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Jogador`, a chave primária é o atributo `id`, e todos os atributos (`lugar`, `missao`, `nome`, `habilidade_briga`, `vida`, `forca`, `tempo_vida`, `gangue`, `nivel`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Jogador`, todos os atributos (`lugar`, `missao`, `nome`, `habilidade_briga`, `vida`, `forca`, `tempo_vida`, `gangue`, `nivel`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Jogador`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Jogador`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.


---

# Tabela Missao

> id, item_nao_fabricavel, lugar, nome, descricao

* **1ª Forma Normal**: Na 1FN, cada campo da tabela deve conter apenas um valor indivisível, e todos os registros devem ter uma estrutura uniforme, sem repetições de grupos de atributos. Na tabela `Missao`, todos os atributos (`id`, `item_nao_fabricavel`, `lugar`, `nome`, `descricao`) são atômicos e monovalorados, garantindo que ela esteja na 1ª Forma Normal.

* **2ª Forma Normal**: A 2FN requer que não existam dependências parciais, o que significa que todos os atributos não-chave devem depender da totalidade da chave primária. Na tabela `Missao`, a chave primária é o atributo `id`, e todos os atributos (`item_nao_fabricavel`, `lugar`, `nome`, `descricao`) dependem inteiramente de `id`. Portanto, a tabela está em conformidade com a 2ª Forma Normal.

* **3ª Forma Normal**: Para atender à 3FN, é necessário que todos os atributos não-chave dependam diretamente da chave primária, sem depender de outros atributos não-chave. Na tabela `Missao`, todos os atributos (`item_nao_fabricavel`, `lugar`, `nome`, `descricao`) dependem diretamente de `id`, atendendo ao critério da 3ª Forma Normal.

* **Forma Normal de Boyce-Codd**: A FNBC exige que o lado esquerdo de toda dependência funcional seja uma superchave. Na tabela `Missao`, `id` é uma chave candidata e todas as dependências funcionais têm `id` no lado esquerdo, garantindo que a tabela esteja em conformidade com a FNBC.

* **4ª Forma Normal**: A 4FN requer a ausência de dependências multivaloradas, onde um único atributo pode estar relacionado a múltiplos valores de outro atributo independentemente. Na tabela `Missao`, todos os atributos são atômicos e não há dependências multivaloradas, satisfazendo assim a 4ª Forma Normal.

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                                     | Autores                                                                                                                                          |
| :--------: | :----: | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| 19/07/2024 | `1.0`  | Criação do documento.                         | [João Antonio G.](https://github.com/joaoseisei)                                                                                                 |
| 20/07/2024 | `1.1`  | Normalização do projeto.                      | [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 11/08/2024 | `1.2`  | Adiciona informações extras para cada tabela. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                 |
| 12/08/2024 | `1.3`  | Atualiza normalização                         | [Júlio Cesar](https://github.com/Julio1099)                                                                                                      |
</div>
