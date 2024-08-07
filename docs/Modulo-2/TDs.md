<center>

# Tabela de dados

</center>

---

<center>

# O que é?

</center>

> Este documento visa monitorar e registrar os dados inseridos em cada uma das tabelas. É importante destacar que esses
> dados poderão ser atualizados ao longo do jogo conforme necessário.

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

| id                          | tipo             |
|-----------------------------|------------------|
| 1[Chave de fenda]           | 'fabricavel'     |
| 2[Pa]                       | 'fabricavel'     |
| 3[Martelo]                  | 'fabricavel'     |
| 4[Picareta]                 | 'fabricavel'     |
| 5[Lock pick]                | 'fabricavel'     |
| 6[Corda]                    | 'fabricavel'     |
| 7[Faca]                     | 'fabricavel'     |
| 8[Adaga]                    | 'fabricavel'     |
| 9[Soco ingles]              | 'fabricavel'     |
| 10[Faca curta]              | 'fabricavel'     |
| 11[Coquetel Molotov]        | 'fabricavel'     |
| 12[Corda com Cerol]         | 'fabricavel'     |
| 13[Garrafa quebrada]        | 'fabricavel'     |
| 14[Sabao]                   | 'nao fabricavel' |
| 15[Pedra]                   | 'nao fabricavel' |
| 16[Graveto]                 | 'nao fabricavel' |
| 17[Linha]                   | 'nao fabricavel' |
| 18[Pedaco pequeno de metal] | 'nao fabricavel' |
| 19[Vidro]                   | 'nao fabricavel' |
| 20[Pedaco grande de metal]  | 'nao fabricavel' |
| 21[Alcool]                  | 'nao fabricavel' |
| 22[Tecido]                  | 'nao fabricavel' |
| 23[Garrada de vidro]        | 'nao fabricavel' |
| 24[Plastico]                | 'nao fabricavel' |
| 25[Isqueiro]                | 'nao fabricavel' |
| 26[Lanterna]                | 'nao fabricavel' |
| 27[Cigarro]                 | 'nao fabricavel' |
| 28[Anti-inflamatorio]       | 'nao fabricavel' |
| 29[Morfina]                 | 'nao fabricavel' |
| 30[Bandagem]                | 'nao fabricavel' |
| 31[Pao seco]                | 'nao fabricavel' |
| 32[Pao]                     | 'nao fabricavel' |
| 33[Queijo]                  | 'nao fabricavel' |
| 34[Carne]                   | 'nao fabricavel' |
| 35[Peixe]                   | 'nao fabricavel' |
| 36[Laranja]                 | 'nao fabricavel' |

---

# Tabela Instancia_Item

| id | *item*                       | lugar                    | inventario |
|----|:-----------------------------|--------------------------|------------|
| 1  | 1 [Chave de fenda]           | 28 [Oficina A]           | NULL       |
| 2  | 2 [Pa]                       | 28 [Oficina A]           | NULL       |
| 3  | 3 [Martelo]                  | 29 [Oficina B]           | NULL       |
| 4  | 4 [Picareta]                 | 29 [Oficina B]           | NULL       |
| 5  | 5 [Lock pick]                | 28 [Oficina A]           | NULL       |
| 6  | 6 [Corda]                    | 29 [Oficina B]           | NULL       |
| 7  | 7 [Faca]                     | 11 [Banheiro A]          | NULL       |
| 8  | 8 [Adaga]                    | 11 [Banheiro A]          | NULL       |
| 9  | 9 [Soco ingles]              | 8 [Cela G]               | NULL       |
| 10 | 10 [Faca curta]              | 6 [Cela F]               | NULL       |
| 11 | 11 [Coquetel molotov]        | 7 [Solitaria leste]      | NULL       |
| 12 | 12 [Corda com Cerol]         | 6 [Cela E]               | NULL       |
| 13 | 13 [Garrafa quebrada]        | 27 [Corredor patio]      | NULL       |
| 14 | 14 [Sabao]                   | 12 [Banheiro B]          | NULL       |
| 15 | 15 [Pedra]                   | 26 [Area de lazer]       | NULL       |
| 16 | 16 [Graveto]                 | 26 [Area de lazer]       | NULL       |
| 17 | 17 [Linha]                   | 16 [Sala A]              | NULL       |
| 18 | 18 [Pedaco pequeno de metal] | 28 [Oficina A]           | NULL       |
| 19 | 19 [Vidro]                   | 3 [Cela B]               | NULL       |
| 20 | 20 [Pedaco grande de metal]  | 4 [Cela A]               | NULL       |
| 21 | 21 [Alcool]                  | 16 [Sala B]              | NULL       |
| 22 | 22 [Tecido]                  | 16 [Sala B]              | NULL       |
| 23 | 23 [Garrafa de vidro]        | 16 [Sala B]              | NULL       |
| 24 | 24 [Plastico]                | 19 [Corredor enfermaria] | NULL       |
| 25 | 25 [Isqueiro]                | 4 [Cela C]               | NULL       |
| 26 | 26 [Lanterna]                | 1 [Solitaria oeste]      | NULL       |
| 27 | 27 [Cigarro]                 | 13 [Corredor patio]      | NULL       |
| 28 | 28 [Anti inflamatorio]       | 17 [Enfermaria A]        | NULL       |
| 29 | 29 [Morfina]                 | 18 [Enfermaria B]        | NULL       |
| 30 | 30 [Bandagem]                | 19 [Enfermaria C]        | NULL       |
| 31 | 31 [Pao seco]                | 20 [Mesa esquerda]       | NULL       |
| 32 | 32 [Pao]                     | 20 [Mesa esquerda]       | NULL       |
| 33 | 33 [Queijo]                  | 20 [Mesa esquerda]       | NULL       |
| 34 | 34 [Carne]                   | 21 [Mesa direita]        | NULL       |
| 35 | 35 [Peixe]                   | 21 [Mesa direita]        | NULL       |
| 36 | 36 [Laranja]                 | 21 [Mesa direita]        | NULL       |
| 37 | 14 [Sabao]                   | 11 [Banheiro A]          | NULL       |
| 38 | 15 [Pedra]                   | 11 [Banheiro A]          | NULL       |
| 39 | 16 [Graveto]                 | 8 [Cela G]               | NULL       |
| 40 | 17 [Linha]                   | 8 [Cela G]               | NULL       |
| 41 | 18 [Pedaco pequeno de metal] | 12 [Banheiro B]          | NULL       |
| 42 | 19 [Vidro]                   | 12 [Banheiro B]          | NULL       |
| 43 | 20 [Pedaco grande de metal]  | 19 [Corredor enfermaria] | NULL       |
| 44 | 21 [Alcool]                  | 19 [Corredor enfermaria] | NULL       |
| 45 | 22 [Tecido]                  | 6 [Cela E]               | NULL       |
| 46 | 23 [Garrafa de vidro]        | 6 [Cela E]               | NULL       |
| 47 | 24 [Plastico]                | 27 [Corredor patio]      | NULL       |
| 48 | 25 [Isqueiro]                | 27 [Corredor patio]      | NULL       |
| 49 | 26 [Lanterna]                | 16 [Sala A]              | NULL       |
| 50 | 27 [Cigarro]                 | 16 [Sala A]              | NULL       |
| 51 | 14 [Sabao]                   | 26 [Area de lazer]       | NULL       |
| 52 | 15 [Pedra]                   | 26 [Area de lazer]       | NULL       |
| 53 | 16 [Graveto]                 | 1 [Solitaria oeste]      | NULL       |
| 54 | 17 [Linha]                   | 1 [Solitaria oeste]      | NULL       |
| 55 | 18 [Pedaco pequeno de metal] | 3 [Cela B]               | NULL       |
| 56 | 19 [Vidro]                   | 3 [Cela B]               | NULL       |
| 57 | 20 [Pedaco grande de metal]  | 4 [Cela C]               | NULL       |
| 58 | 21 [Alcool]                  | 4 [Cela C]               | NULL       |
| 59 | 22 [Tecido]                  | 28 [Oficina A]           | NULL       |
| 60 | 23 [Garrafa de vidro]        | 28 [Oficina A]           | NULL       |
| 61 | 1 [Chave de fenda]           | NULL                     | 2          |
| 62 | 20 [Pedaco grande de metal]  | NULL                     | 2          |
| 63 | 2 [Pa]                       | NULL                     | 3          |
| 64 | 18 [Pedaco pequeno de metal] | NULL                     | 3          |
| 65 | 10[Faca curta]               | NULL                     | 4          |
| 66 | 2 [Pa]                       | NULL                     | 4          |
| 67 | 20 [Pedaco grande de metal]  | NULL                     | 5          |
| 68 | 33 [Queijo]                  | NULL                     | 5          |
| 69 | 3 [Martelo]                  | NULL                     | 6          |
| 70 | 36 [Laranja]                 | NULL                     | 6          |
| 71 | 17 [Linha]                   | NULL                     | 7          |
| 72 | 12 [Corda com Cerol]         | NULL                     | 7          |
| 73 | 10 [Faca curta]              | NULL                     | 8          |
| 74 | 4 [Picareta]                 | NULL                     | 8          |
| 75 | 9 [Soco ingles]              | NULL                     | 9          |
| 76 | 31 [Pao seco]                | NULL                     | 9          |
| 77 | 27 [Cigarro]                 | NULL                     | 10         |
| 78 | 5 [Lock pick]                | NULL                     | 10         |
| 79 | 23 [Garrafa de vidro]        | NULL                     | 11         |
| 80 | 21 [Alcool]                  | NULL                     | 11         |
| 81 | 24 [Plastico]                | NULL                     | 12         |
| 82 | 10 [Faca curta]              | NULL                     | 12         |
| 83 | 16 [Graveto]                 | NULL                     | 13         |
| 84 | 9 [Soco ingles]              | NULL                     | 13         |
| 85 | 27 [Cigarro]                 | NULL                     | 14         | 
| 86 | 25 [Isqueiro]                | NULL                     | 14         |
| 87 | 26 [Lanterna]                | NULL                     | 15         |
| 88 | 28 [Anti-inflamatorio]       | NULL                     | 15         |
| 89 | 25 [Isqueiro]                | NULL                     | 16         |
| 80 | 30 [Bandagem]                | NULL                     | 16         |
| 91 | 23 [Garrafa de vidro]        | NULL                     | 17         |
| 92 | 21 [Alcool]                  | NULL                     | 17         |
| 93 | 23 [Garrafa de vidro]        | NULL                     | 18         |
| 94 | 22 [Tecido]                  | NULL                     | 18         | 
| 95 | 11 [Coquetel Molotov]        | NULL                     | 19         | 
| 96 | 28 [Anti-inflamatorio]       | NULL                     | 19         |
| 97 | 12 [Corda com Cerol]         | NULL                     | 20         |
| 98 | 20 [Pedaco grande de metal]  | NULL                     | 20         |


---

# Tabela Item_Fabricavel

| nome                  | tipo         |
|-----------------------|--------------|
| 1 [Chave de Fenda]    | 'ferramenta' |
| 2 [Pa]                | 'ferramenta' |
| 3 [Martelo]           | 'ferramenta' |
| 4 [Picareta]          | 'ferramenta' |
| 5 [Lock Pick]         | 'ferramenta' |
| 6 [Corda]             | 'ferramenta' |
| 7 [Faca]              | 'arma'       |
| 8 [Adaga]             | 'arma'       |
| 9 [Soco Ingles]       | 'arma'       |
| 10 [Faca Curta]       | 'arma'       |
| 11 [Coquetel Molotov] | 'arma'       |
| 12 [Corda com Cerol]  | 'arma'       |
| 13 [Garrafa Quebrada] | 'arma'       |

---

# Tabela Item_nao_Fabricavel

| id                          | tipo          |
|-----------------------------|---------------|
| 14[sabao]                   | 'utilizavel'  |
| 15[pedra]                   | 'utilizavel'  |
| 16[graveto]                 | 'utilizavel'  |
| 17[linha]                   | 'utilizavel'  |
| 18[pedaco pequeno de metal] | 'utilizavel'  |
| 19[vidro]                   | 'utilizavel'  |
| 20[pedaco grande de metal]  | 'utilizavel'  |
| 21[alcool]                  | 'utilizavel'  |
| 22[tecido]                  | 'utilizavel'  |
| 23[garrada de vidro]        | 'utilizavel'  |
| 24[plastico]                | 'utilizavel'  |
| 25[Isqueiro]                | 'utilizavel'  |
| 26[lanterna]                | 'utilizavel'  |
| 27[cigarro]                 | 'utilizavel'  |
| 28[Anti-inflamatorio]       | 'medicamento' |
| 29[Morfina]                 | 'medicamento' |
| 30[Bandagem]                | 'medicamento' |
| 31[pao seco]                | 'comida'      |
| 32[pao]                     | 'comida'      |
| 33[queijo]                  | 'comida'      |
| 34[carne]                   | 'comida'      |
| 35[Peixe]                   | 'comida'      |
| 36[Laranja]                 | 'comida'      |

---

# Tabela Ferramenta

| id | nome           | tamanho | descricao                                                                                         | utilidade                                         |
|----|----------------|---------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 1  | Chave de Fenda | 1       | Ferramenta com ponta plana ou cruzada para apertar ou soltar parafusos.                           | Usada para desmontar objetos.                     |
| 2  | Pa             | 2       | Ferramenta com lâmina larga e plana para cavar e mover materiais.                                 | Ideal para escavar ou remover detritos.           |
| 3  | Martelo        | 2       | Ferramenta com cabeça pesada usada para bater pregos ou quebrar objetos.                          | Usado em construção e demolição.                  |
| 4  | Picareta       | 2       | Ferramenta com uma extremidade pontiaguda e outra achatada, usada para quebrar superfícies duras. | Ideal para mineração ou demolição.                |
| 5  | Lock Pick      | 1       | Ferramenta fina e estreita usada para destrancar fechaduras sem chave.                            | Utilizada para abrir fechaduras de forma furtiva. |
| 6  | Corda          | 1       | Cordão grosso feito de fibras entrelaçadas.                                                       | Usada para amarrar, puxar ou escalar.             |

---

# Tabela Arma

| id | nome             | tamanho | descricao                                                                    | dano |
|----|------------------|---------|------------------------------------------------------------------------------|------|
| 7  | Faca             | 2       | Lâmina afiada e curta usada para cortar ou perfurar.                         | 3    |
| 8  | Adaga            | 1       | Ferramenta fina e pontiaguda.                                                | 1    |
| 9  | Soco Ingles      | 1       | Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo. | 2    |
| 10 | Faca Curta       | 1       | Pequena faca com lâmina curta, fácil de esconder.                            | 2    |
| 11 | Coquetel Molotov | 1       | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.        | 5    |
| 12 | Corda com Cerol  | 1       | Corda revestida com vidro moído para causar cortes.                          | 3    |
| 13 | Garrafa Quebrada | 1       | Garrafa de vidro quebrada, usada como arma cortante.                         | 3    |

---

# Tabela Medicamento

| id | nome              | tamanho | descricao                                                                          | raridade | cura_medicamento | medicamento_quantidade |
|----|-------------------|---------|------------------------------------------------------------------------------------|----------|------------------|------------------------|
| 28 | anti-inflamatorio | 1       | Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.             | 2        | 3                | 5                      |
| 29 | Morfina           | 1       | Analgésico opiáceo potente utilizado para aliviar dores intensas.                  | 1        | 10               | 2                      |
| 30 | Bandagem          | 1       | Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo. | 0        | 2                | 5                      |

---

# Tabela Comida

| id | nome     | tamanho | descricao                                                                        | raridade | comida_quantidade | cura |
|----|----------|---------|----------------------------------------------------------------------------------|----------|-------------------|------|
| 31 | Pao seco | 1       | um pão tão seco e duro, que parece que o proprio vandor amassou ele.             | 0        | 1                 | 0    |
| 32 | Pao      | 1       | alimento básico feito a partir de farinha, água e fermento.                      | 0        | 3                 | 1    |
| 33 | Queijo   | 1       | produto lácteo sólido feito a partir da coagulação do leite.                     | 0        | 3                 | 1    |
| 34 | Carne    | 2       | é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento. | 2        | 1                 | 5    |
| 35 | Peixe    | 1       | tecido muscular de peixe, consumido como alimento.                               | 1        | 2                 | 3    |
| 36 | Laranja  | 1       | fruta cítrica, suculenta e doce.                                                 | 0        | 3                 | 1    |

  
---

# Tabela Utilizavel

| id | nome                    | tamanho | descricao_Efeito                                                                                                | quantidade |
|----|-------------------------|---------|-----------------------------------------------------------------------------------------------------------------|------------|
| 14 | Sabao                   | 1       | serve para remover sujeira e impurezas de superfícies e objetos, também é um material para fabricação de itens. | 1          |
| 15 | Pedra                   | 1       | A pedra serve para construção e também é um material para fabricação de itens.                                  | 3          |
| 16 | graveto                 | 1       | Produto de origem vegetal, é usado como material para fabricação de itens.                                      | 3          |
| 17 | linha                   | 1       | fio fino e flexível utilizado como material para fabricação de itens.                                           | 3          |
| 18 | pedaco pequeno de metal | 1       | Corda revestida com vidro moído para causar cortes.                                                             | 3          |
| 19 | vidro                   | 1       | utilizado como material para fabricação de cerol.                                                               | 1          |
| 20 | pedaco grande de metal  | 3       | Garrafa de vidro quebrada, usada como arma cortante.                                                            | 1          |
| 21 | alcool                  | 1       | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1          |
| 22 | tecido                  | 1       | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.                                           | 3          |
| 23 | garrada de vidro        | 2       | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1          |
| 24 | plastico                | 1       | Corda revestida com vidro moído para causar cortes.                                                             | 3          |
| 25 | Isqueiro                | 1       | Isqueiro é um dispositivo portátil utilizado para gerar fogo, podendo ser utilizado para queimar coisas.        | 1          |
| 26 | Lanterna                | 1       | Lanterna é um dispositivo portátil que emite luz.                                                               | 1          |
| 27 | cigarro                 | 1       | Moeda de troca do jogo, além de poder ser utilizado para acalmar.                                               | 10         |

---

# Tabela Fabricacao

| id | *item*                | livro                    |
|----|-----------------------|--------------------------|
| 1  | 1 [Chave de Fenda]    | 1 [Livro de Crafts EASY] |
| 2  | 2 [Pa]                | 1 [Livro de Crafts EASY] |
| 3  | 3 [Martelo]           | 1 [Livro de Crafts EASY] |
| 4  | 4 [Lock Pick]         | 1 [Livro de Crafts EASY] |
| 5  | 5 [Corda]             | 1 [Livro de Crafts EASY] |
| 6  | 6 [Adaga]             | 1 [Livro de Crafts EASY] |
| 7  | 7 [Faca Curta]        | 1 [Livro de Crafts EASY] |
| 8  | 8 [Corda com Cerol]   | 1 [Livro de Crafts EASY] |
| 9  | 9 [Garrafa Quebrada]  | 1 [Livro de Crafts EASY] |
| 10 | 10 [Picareta]         | 2 [Livro de Crafts HARD] |
| 11 | 11 [Faca]             | 2 [Livro de Crafts HARD] |
| 12 | 12 [Soco Ingles]      | 2 [Livro de Crafts HARD] |
| 13 | 13 [Coquetel Molotov] | 2 [Livro de Crafts HARD] |

---

# Tabela Lista_Fabricacao

| fabricacao            | item                         |
|-----------------------|:-----------------------------|
| 1 [Chave de fenda]    | 18 [Pedaco pequeno de metal] |
| 1 [Chave de fenda]    | 24 [Plastico]                |
| 2 [Pa]                | 16 [Graveto]                 |
| 2 [Pa]                | 20 [Pedaco grande de metal]  |
| 2 [Pa]                | 17 [Linha]                   |
| 3 [Martelo]           | 15 [Pedra]                   |
| 3 [Martelo]           | 16 [Graveto]                 |
| 4 [Picareta]          | 20 [Pedaco grande de metal]  |
| 4 [Picareta]          | 16 [Graveto]                 |
| 4 [Picareta]          | 22 [Tecido]                  |
| 5 [Lock Pick]         | 16 [Graveto]                 |
| 5 [Lock Pick]         | 18 [Pedaco pequeno de metal] |
| 6 [Corda]             | 24 [Plastico]                |
| 7 [Faca]              | 20 [Pedaco grande de metal]  |
| 7 [Faca]              | 22 [Tecido]                  |
| 8 [Adaga]             | 18 [Pedaco pequeno de metal] |
| 9 [Soco Ingles]       | 14 [Sabao]                   |
| 9 [Soco Ingles]       | 22 [Tecido]                  |
| 10 [Faca Curta]       | 18 [Pedaco pequeno de metal] |
| 10 [Faca Curta]       | 22 [Tecido]                  |
| 11 [Coquetel Molotov] | 23 [Garrafa de vidro]        |
| 11 [Coquetel Molotov] | 21 [Alcool]                  |
| 11 [Coquetel Molotov] | 22 [Tecido]                  |
| 12 [Corda com Cerol]  | 6 [Corda]                    |
| 12 [Corda com Cerol]  | 19 [Vidro]                   |
| 13 [Garrafa Quebrada] | 23 [Garrafa de vidro]        |

---

# Tabela Livro_Fabricacao

| id | nome                 |
|----|----------------------|
| 1  | Livro de Crafts EASY |
| 2  | Livro de Crafts HARD |

---

# Tabela Prisao

| id | nome    |
|----|---------|
| 1  | Basilio |

---

# Tabela Regiao

| id | nome       | prisao | descricao                                                                                           |
|----|------------|--------|-----------------------------------------------------------------------------------------------------|
| 1  | celas      | 1      | Local onde estão as celas e solitárias dos prisioneiros.                                            |
| 2  | banheiros  | 1      | Local onde os prisioneiros se banham.                                                               |
| 3  | enfermaria | 1      | Local onde os prisioneiros podem se tratar/curar.                                                   |
| 4  | refeitorio | 1      | Local onde os prisioneiros fazem suas refeições.                                                    |
| 5  | patio      | 1      | Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete/futsal e relaxar. |
| 6  | oficinas   | 1      | Local onde os prisioneiros trabalham e ganham um pouco de dinheiro.                                 |

---

# Tabela Lugar

| id | nome                | *regiao* | descricao                                                                                |
|----|---------------------|----------|------------------------------------------------------------------------------------------|
| 1  | solitaria Oeste     | 1        | Cela para os prisioneiros levadinhos. Na parede direita há uma mancha de cimento fresco. |
| 2  | cela A              | 1        | Cela onde dormem os prisioneiros 1 e 2.                                                  |
| 3  | cela B              | 1        | Cela onde dormem os prisioneiros 3 e 4.                                                  |
| 4  | cela C              | 1        | Cela onde dormem os prisioneiros 5 e 6.                                                  |
| 5  | cela D              | 1        | Cela onde dormem os prisioneiros 7 e 8.                                                  |
| 6  | cela E              | 1        | Cela onde dormem os prisioneiros 9 e 10.                                                 |
| 7  | cela F              | 1        | Cela onde dormem os prisioneiros 11 e 12.                                                |
| 8  | cela G              | 1        | Cela onde dormem o prisioneiro 13 e o jogador.                                           |
| 9  | solitaria Leste     | 1        | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas.   |
| 10 | corredor Celas      | 1        | Corredor para se deslocar entre as celas e as solitárias.                                |
| 11 | banheiro A          | 2        | Banheiro onde os prisioneiros tomam banho.                                               |
| 12 | banheiro B          | 2        | Banheiro onde os prisioneiros tomam banho.                                               |
| 13 | banheiro C          | 2        | Banheiro onde os prisioneiros tomam banho.                                               |
| 14 | banheiro D          | 2        | Banheiro onde os prisioneiros tomam banho.                                               |
| 15 | corredor Banheiros  | 2        | Corredor para se deslocar entre os banheiros.                                            |
| 16 | sala A              | 3        | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 17 | sala B              | 3        | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 18 | sala C              | 3        | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 19 | corredor Enfermaria | 3        | Corredor para se deslocar entre as salas da enfermaria.                                  |
| 20 | mesa Esquerda       | 4        | Mesa onde a gangue 1 faz suas refeições.                                                 |
| 21 | mesa Direita        | 4        | Mesa onde a gangue 2 faz suas refeições.                                                 |
| 22 | corredor Refeitorio | 4        | Corredor para se deslocar entre as mesas do refeitório.                                  |
| 23 | academia Simples    | 5        | Uma área com equipamentos simples de exercício.                                          |
| 24 | quadra De Basquete  | 5        | Quadra onde os prisioneiros jogam basquete/futsal para se distrair e se exercitar.       |
| 25 | arquibancada        | 5        | Arquibancada onde os prisioneiros podem conversar e assistir os jogos.                   |
| 26 | area De Lazer       | 5        | Bancos onde os prisioneiros podem sentar e conversar.                                    |
| 27 | corredor Patio      | 5        | Corredor para se deslocar entre as áreas do pátio e as oficinas.                         |
| 28 | oficina A           | 6        | Oficina de marcenaria onde os prisioneiros trabalham.                                    |
| 29 | oficina B           | 6        | Oficina de impressão de placas de carro onde os prisioneiros trabalham.                  |

---

# Tabela Lugar_Origem_Destino

| lugar_origem             | lugar_destino            |
|--------------------------|--------------------------|
| 1 [solitaria Oeste]      | 2 [cela A]               |
| 1 [solitaria Oeste]      | 10 [corredor Celas]      |
| 2 [cela A]               | 1 [solitaria Oeste]      |
| 2 [cela A]               | 10 [corredor Celas]      |
| 3 [cela B]               | 10 [corredor Celas]      |
| 4 [cela C]               | 10 [corredor Celas]      |
| 5 [cela D]               | 10 [corredor Celas]      |
| 6 [cela E]               | 10 [corredor Celas]      |
| 7 [cela F]               | 10 [corredor Celas]      |
| 8 [cela G]               | 10 [corredor Celas]      |
| 9 [solitaria Leste]      | 10 [corredor Celas]      |
| 10 [corredor Celas]      | 1 [solitaria Oeste]      |
| 10 [corredor Celas]      | 2 [cela A]               |
| 10 [corredor Celas]      | 3 [cela B]               |
| 10 [corredor Celas]      | 4 [cela C]               |
| 10 [corredor Celas]      | 5 [cela D]               |
| 10 [corredor Celas]      | 6 [cela E]               |
| 10 [corredor Celas]      | 7 [cela F]               |
| 10 [corredor Celas]      | 8 [cela G]               |
| 10 [corredor Celas]      | 9 [solitaria Leste]      |
| 10 [corredor Celas]      | 15 [corredor Banheiros]  |
| 11 [banheiro A]          | 15 [corredor Banheiros]  |
| 12 [banheiro B]          | 15 [corredor Banheiros]  |
| 13 [banheiro C]          | 15 [corredor Banheiros]  |
| 14 [banheiro D]          | 15 [corredor Banheiros]  |
| 15 [corredor Banheiros]  | 10 [corredor Celas]      |
| 15 [corredor Banheiros]  | 11 [banheiro A]          |
| 15 [corredor Banheiros]  | 12 [banheiro B]          |
| 15 [corredor Banheiros]  | 13 [banheiro C]          |
| 15 [corredor Banheiros]  | 14 [banheiro D]          |
| 15 [corredor Banheiros]  | 19 [corredor Enfermaria] |
| 15 [corredor Banheiros]  | 22 [corredor Refeitorio] |
| 16 [sala A]              | 17 [sala B]              |
| 16 [sala A]              | 19 [corredor Enfermaria] |
| 17 [sala B]              | 16 [sala A]              |
| 17 [sala B]              | 18 [sala C]              |
| 17 [sala B]              | 19 [corredor Enfermaria] |
| 18 [sala C]              | 17 [sala B]              |
| 18 [sala C]              | 19 [corredor Enfermaria] |
| 19 [corredor Enfermaria] | 15 [corredor Banheiros]  |
| 19 [corredor Enfermaria] | 16 [sala A]              |
| 19 [corredor Enfermaria] | 17 [sala B]              |
| 19 [corredor Enfermaria] | 18 [sala C]              |
| 20 [mesa Esquerda]       | 22 [corredor Refeitorio] |
| 21 [mesa Direita]        | 22 [corredor Refeitorio] |
| 22 [corredor Refeitorio] | 15 [corredor Banheiros]  |
| 22 [corredor Refeitorio] | 20 [mesa Esquerda]       |
| 22 [corredor Refeitorio] | 21 [mesa Direita]        |
| 22 [corredor Refeitorio] | 27 [corredor Patio ]     |
| 23 [academia Simples]    | 24 [quadra De Basquete]  |
| 23 [academia Simples]    | 27 [corredor Patio ]     |
| 24 [quadra De Basquete]  | 23 [academia Simples]    |
| 24 [quadra De Basquete]  | 25 [arquibancada]        |
| 24 [quadra De Basquete]  | 27 [corredor Patio ]     |
| 25 [arquibancada]        | 24 [quadra De Basquete]  |
| 25 [arquibancada]        | 26 [area De Lazer]       |
| 25 [arquibancada]        | 27 [corredor Patio ]     |
| 26 [area De Lazer]       | 25 [arquibancada]        |
| 26 [area De Lazer]       | 27 [corredor Patio ]     |
| 27 [corredor Patio ]     | 22 [corredor Refeitorio] |
| 27 [corredor Patio ]     | 23 [academia Simples]    |
| 27 [corredor Patio ]     | 24 [quadra De Basquete]  |
| 27 [corredor Patio ]     | 25 [arquibancada]        |
| 27 [corredor Patio ]     | 26 [area De Lazer]       |
| 27 [corredor Patio ]     | 28 [oficina A]           |
| 27 [corredor Patio ]     | 29 [oficina B]           |
| 28 [oficina A]           | 27 [corredor Patio ]     |
| 29 [oficina B]           | 27 [corredor Patio ]     |

---

# Tabela Pessoa

| Id | tipo          |
|----|---------------|
| 1  | 'Jogador'     |
| 2  | 'Prisioneiro' |
| 3  | 'Prisioneiro' |
| 4  | 'Prisioneiro' |
| 5  | 'Prisioneiro' |
| 6  | 'Prisioneiro' |
| 7  | 'Prisioneiro' |
| 8  | 'Prisioneiro' |
| 9  | 'Prisioneiro' |
| 10 | 'Prisioneiro' |
| 11 | 'Prisioneiro' |
| 12 | 'Prisioneiro' |
| 13 | 'Prisioneiro' |
| 14 | 'Policial'    |
| 15 | 'Policial'    |
| 16 | 'Policial'    |
| 17 | 'Policial'    |
| 18 | 'Policial'    |
| 19 | 'Informante'  |
| 20 | 'Informante'  |

---

# Tabela Inventario

| id | *pessoa* | inventario_ocupado | tamanho |
|----|----------|--------------------|---------|
| 1  | 1        | 0                  | 5       |
| 2  | 2        | 0                  | 5       |
| 3  | 3        | 0                  | 5       |
| 4  | 4        | 0                  | 5       |
| 5  | 5        | 0                  | 5       |
| 6  | 6        | 0                  | 5       |
| 7  | 7        | 0                  | 5       |
| 8  | 8        | 0                  | 5       |
| 9  | 9        | 0                  | 5       |
| 10 | 10       | 0                  | 5       |
| 11 | 11       | 0                  | 5       |
| 12 | 12       | 0                  | 5       |
| 13 | 13       | 0                  | 5       |
| 14 | 14       | 0                  | 5       |
| 15 | 15       | 0                  | 5       |
| 16 | 16       | 0                  | 5       |
| 17 | 17       | 0                  | 5       |
| 18 | 18       | 0                  | 5       |
| 19 | 19       | 0                  | 5       |
| 20 | 20       | 0                  | 5       |

----

# Tabela Prisioneiro

| id | nome         | habilidade_briga | vida | força | gangue     | lugar            |
|----|--------------|------------------|------|-------|------------|------------------|
| 2  | Rivas        | 4                | 9    | 7     | 'Palhacos' | quadraDesportiva |
| 3  | Filomano     | 6                | 7    | 4     | 'Polvos'   | celaB            |
| 4  | Fragas       | 5                | 11   | 5     | 'Palhacos' | banheiroA        |
| 5  | Glaucão      | 3                | 6    | 8     | 'Polvos'   | mesaEsquerda     |
| 6  | Ucraniano    | 7                | 5    | 6     | 'Palhacos' | celaC            |
| 7  | Rispomático  | 6                | 12   | 6     | 'Polvos'   | academiaSimples  |
| 8  | Manogaz      | 4                | 8    | 5     | 'Palhacos' | celaG            |
| 9  | Dado         | 5                | 10   | 6     | 'Polvos'   | banheiroB        |
| 10 | Fabrilton    | 4                | 7    | 5     | 'Palhacos' | mesaDireita      |
| 11 | Eneido       | 6                | 6    | 6     | 'Polvos'   | solitariaOeste   |
| 12 | Carlos       | 5                | 9    | 7     | 'Palhacos' | arquibancada     |
| 13 | Silvio Serra | 6                | 8    | 5     | 'Polvos'   | celaE            |

-----

# Tabela Policial

| id | nome                | lugar            | corrupto |
|----|---------------------|------------------|----------|
| 14 | Italo Dimetrio      | solitariaOeste   | true     |
| 15 | Sargento Nascimento | mesaDireita      | false    |
| 16 | Capitão Mathias     | quadraDesportiva | false    |
| 17 | Capitão Brad        | solitariaLeste   | true     |
| 18 | Lil Chico           | arquibancada     | true     |

---

# Tabela Informante

| id | nome    | dano_infomante | lugar        |
|----|---------|----------------|--------------|
| 19 | Cubano  | 200            | banheiroC    |
| 20 | Chileno | 200            | Enfermaria A |

---

# Tabela Jogador

| id | nome    | habilidade_briga | vida | força | tempo_vida | gangue | lugar | missao |
|----|---------|------------------|------|-------|------------|--------|-------|--------|
| 01 | Carimbo | 2                | 5    | 3     | 10         | null   | celaA | null   |

---

# Tabela Missao

| id | item                   | lugar | nome                      | descricao                                                                  |
|----|------------------------|-------|---------------------------|----------------------------------------------------------------------------|
| 1  | chave oficina A        | 1     | Fuja da solitaria oeste   | Escape da cela de isolamento leste sem ser pego.                           |
| 2  | chave oficina B        | 9     | Fuja da solitaria leste   | Escape da cela de isolamento oeste sem ser pego.                           |
| 3  | BANDAGEM               | 5     | Observar  cela            | Observe e memorize os detalhes da cela para planejar uma fuga.             |
| 4  | FACA PEQUENA           | NULL  | Escolher gangue           | Escolha a gangue com a qual se aliar na prisão.                            |
| 5  | NULL                   | NULL  | explorar o mapa           | Explore os locais no mapa da prisão, para um melhor entendimento do mesmo. |
| 6  | CARNE                  | NULL  | Brigue com alguém         | Inicie e participe de uma briga com outro prisioneiro.                     |
| 7  | REMEDIO                | NULL  | Vença uma briga           | Vença uma briga                                                            |
| 8  | NULL                   | NULL  | Fuja da prisão            | Fuja da prisão                                                             |
| 9  | pedaco grande de metal | NULL  | encontre o informante     | encontre o informante                                                      |
| 10 | Isqueiro               | 24    | vença um jogo de basquete | vença um jogo de basquete                                                  |
| 11 | CARNE                  | 23    | Fique maromba             | Va na academia                                                             |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão |                                                              Descrição                                                               | Autores                                               |
|------------|--------|:------------------------------------------------------------------------------------------------------------------------------------:|-------------------------------------------------------|
| 26/07/2024 | `1.0`  |                                                        Criação do documento.                                                         | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 28/07/2024 | `1.1`  |                                           Desenvolvimento de algumas tabelas e correções.                                            | [João Antonio G.](https://github.com/joaoseisei)      |
| 28/07/2024 | `1.2`  |                                                   Desenvolvimento algumas tabelas.                                                   | [Fernando Gabriel](https://github.com/show-dawn)      |
| 28/07/2024 | `1.3`  |                                                   Desenvolvimento algumas tabelas.                                                   | [Julio Cesar](https://github.com/Julio1099)           |
| 29/07/2024 | `1.4`  |                                                 Completa a tabela [`Lugar`](#Lugar)                                                  | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 29/07/2024 | `1.5`  |                                                        Ajustes tabela Pessoa                                                         | [Júlio Cesar](https://github.com/julio1099)           |
| 29/07/2024 | `1.6`  |                                                   Desenvolvimento algumas tabelas.                                                   | [Fernando Gabriel](https://github.com/show-dawn)      |
| 02/08/2024 | `1.7`  |                                                       Correção tabela Pessoa.                                                        | [Júlio Cesar](https://github.com/Julio1099)           |
| 04/08/2024 | `1.8`  |                                                         Adiciona os crafts.                                                          | [João Antonio G.](https://github.com/joaoseisei)      |
| 04/08/2024 | `1.9`  | Corrige as tabelas [`Prisao`](#Prisao), [`Regiao`](#Regiao) e [`Lugar`](#Lugar), e cria a tabela [`Lugar_Anterior`](#Lugar_Anterior) | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 05/08/2024 | `2.0`  |                                                  Adiciona missao e formata tabelas.                                                  | [Fernando Gabriel](https://github.com/show-dawn)      |
| 06/08/2024 | `2.1`  |                                         Corrige a tabela [`Lugar_Proximo`](#Lugar_Proximo).                                          | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 06/08/2024 | `2.2`  |                                           Popula instancia de item e lista de fabricacao.                                            | [João Antonio G.](https://github.com/joaoseisei)      |
| 06/08/2024 | `2.3`  |                                     Termina de corrigir a tabela [`Lugar_Proximo`](#Lugar_Proximo).                                  | [Breno Alexandre](https://github.com/brenoalexandre0) |

</div>
