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

| id | *item*                       | lugar                    | `regiao` | inventario | `pessoa` |
|----|:-----------------------------|--------------------------|----------|------------|----------|
| 1  | 1 [Chave de fenda]           | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 2  | 2 [Pa]                       | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 3  | 3 [Martelo]                  | 29 [Oficina B]           | 6        | NULL       | NULL     |
| 4  | 4 [Picareta]                 | 29 [Oficina B]           | 6        | NULL       | NULL     |
| 5  | 20 [Pedaco grande de metal]  | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 6  | 6 [Corda]                    | 29 [Oficina B]           | 6        | NULL       | NULL     |
| 7  | 7 [Faca]                     | 11 [Banheiro A]          | 2        | NULL       | NULL     |
| 8  | 8 [Adaga]                    | 11 [Banheiro A]          | 2        | NULL       | NULL     |
| 9  | 9 [Soco ingles]              | 8 [Cela G]               | 1        | NULL       | NULL     |
| 10 | 10 [Faca curta]              | 6 [Cela F]               | 1        | NULL       | NULL     |
| 11 | 11 [Coquetel molotov]        | 7 [Solitaria leste]      | 1        | NULL       | NULL     |
| 12 | 12 [Corda com cerol]         | 6 [Cela E]               | 1        | NULL       | NULL     |
| 13 | 13 [Garrafa quebrada]        | 27 [Corredor patio]      | 5        | NULL       | NULL     |
| 14 | 14 [Sabao]                   | 12 [Banheiro B]          | 2        | NULL       | NULL     |
| 15 | 15 [Pedra]                   | 26 [Area de lazer]       | 5        | NULL       | NULL     |
| 16 | 16 [Graveto]                 | 26 [Area de lazer]       | 5        | NULL       | NULL     |
| 17 | 17 [Linha]                   | 16 [Sala A]              | 3        | NULL       | NULL     |
| 18 | 18 [Pedaco pequeno de metal] | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 19 | 19 [Vidro]                   | 3 [Cela B]               | 1        | NULL       | NULL     |
| 20 | 20 [Pedaco grande de metal]  | 4 [Cela A]               | 1        | NULL       | NULL     |
| 21 | 21 [Alcool]                  | 16 [Sala B]              | 3        | NULL       | NULL     |
| 22 | 22 [Tecido]                  | 16 [Sala B]              | 3        | NULL       | NULL     |
| 23 | 23 [Garrafa de vidro]        | 16 [Sala B]              | 3        | NULL       | NULL     |
| 24 | 24 [Plastico]                | 19 [Corredor enfermaria] | 3        | NULL       | NULL     |
| 25 | 25 [Isqueiro]                | 4 [Cela C]               | 1        | NULL       | NULL     |
| 26 | 26 [Lanterna]                | 1 [Solitaria oeste]      | 1        | NULL       | NULL     |
| 27 | 27 [Cigarro]                 | 13 [Corredor patio]      | 5        | NULL       | NULL     |
| 28 | 28 [Anti inflamatorio]       | 17 [Enfermaria A]        | 3        | NULL       | NULL     |
| 29 | 29 [Morfina]                 | 18 [Enfermaria B]        | 3        | NULL       | NULL     |
| 30 | 30 [Bandagem]                | 19 [Enfermaria C]        | 3        | NULL       | NULL     |
| 31 | 31 [Pao seco]                | 20 [Mesa esquerda]       | 4        | NULL       | NULL     |
| 32 | 32 [Pao]                     | 20 [Mesa esquerda]       | 4        | NULL       | NULL     |
| 33 | 33 [Queijo]                  | 20 [Mesa esquerda]       | 4        | NULL       | NULL     |
| 34 | 34 [Carne]                   | 21 [Mesa direita]        | 4        | NULL       | NULL     |
| 35 | 35 [Peixe]                   | 21 [Mesa direita]        | 4        | NULL       | NULL     |
| 36 | 36 [Laranja]                 | 21 [Mesa direita]        | 4        | NULL       | NULL     |
| 37 | 14 [Sabao]                   | 11 [Banheiro A]          | 2        | NULL       | NULL     |
| 38 | 15 [Pedra]                   | 11 [Banheiro A]          | 2        | NULL       | NULL     |
| 39 | 16 [Graveto]                 | 8 [Cela G]               | 1        | NULL       | NULL     |
| 40 | 17 [Linha]                   | 8 [Cela G]               | 1        | NULL       | NULL     |
| 41 | 18 [Pedaco pequeno de metal] | 12 [Banheiro B]          | 2        | NULL       | NULL     |
| 42 | 19 [Vidro]                   | 12 [Banheiro B]          | 2        | NULL       | NULL     |
| 43 | 20 [Pedaco grande de metal]  | 19 [Corredor enfermaria] | 3        | NULL       | NULL     |
| 44 | 21 [Alcool]                  | 19 [Corredor enfermaria] | 3        | NULL       | NULL     |
| 45 | 22 [Tecido]                  | 6 [Cela E]               | 1        | NULL       | NULL     |
| 46 | 23 [Garrafa de vidro]        | 6 [Cela E]               | 1        | NULL       | NULL     |
| 47 | 24 [Plastico]                | 27 [Corredor patio]      | 5        | NULL       | NULL     |
| 48 | 25 [Isqueiro]                | 27 [Corredor patio]      | 5        | NULL       | NULL     |
| 49 | 26 [Lanterna]                | 16 [Sala A]              | 3        | NULL       | NULL     |
| 50 | 27 [Cigarro]                 | 16 [Sala A]              | 3        | NULL       | NULL     |
| 51 | 14 [Sabao]                   | 26 [Area de lazer]       | 5        | NULL       | NULL     |
| 52 | 15 [Pedra]                   | 26 [Area de lazer]       | 5        | NULL       | NULL     |
| 53 | 16 [Graveto]                 | 1 [Solitaria oeste]      | 1        | NULL       | NULL     |
| 54 | 17 [Linha]                   | 1 [Solitaria oeste]      | 1        | NULL       | NULL     |
| 55 | 18 [Pedaco pequeno de metal] | 3 [Cela B]               | 1        | NULL       | NULL     |
| 56 | 19 [Vidro]                   | 3 [Cela B]               | 1        | NULL       | NULL     |
| 57 | 20 [Pedaco grande de metal]  | 4 [Cela C]               | 1        | NULL       | NULL     |
| 58 | 21 [Alcool]                  | 4 [Cela C]               | 1        | NULL       | NULL     |
| 59 | 22 [Tecido]                  | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 60 | 23 [Garrafa de vidro]        | 28 [Oficina A]           | 6        | NULL       | NULL     |
| 61 | 1 [Chave de fenda]           | NULL                     | NULL     | 2          | 2        |
| 62 | 20 [Pedaco grande de metal]  | NULL                     | NULL     | 2          | 2        |
| 63 | 2 [Pa]                       | NULL                     | NULL     | 3          | 3        |
| 64 | 18 [Pedaco pequeno de metal] | NULL                     | NULL     | 3          | 3        |
| 65 | 10 [Faca curta]              | NULL                     | NULL     | 4          | 4        |
| 66 | 2 [Pa]                       | NULL                     | NULL     | 4          | 4        |
| 67 | 20 [Pedaco grande de metal]  | NULL                     | NULL     | 5          | 5        |
| 68 | 33 [Queijo]                  | NULL                     | NULL     | 5          | 5        |
| 69 | 3 [Martelo]                  | NULL                     | NULL     | 6          | 6        |
| 70 | 36 [Laranja]                 | NULL                     | NULL     | 6          | 6        |
| 71 | 17 [Linha]                   | NULL                     | NULL     | 7          | 7        |
| 72 | 12 [Corda com Cerol]         | NULL                     | NULL     | 7          | 7        |
| 73 | 10 [Faca curta]              | NULL                     | NULL     | 8          | 8        |
| 74 | 20 [Pedaco grande de metal]  | NULL                     | NULL     | 8          | 8        |
| 75 | 9 [Soco ingles]              | NULL                     | NULL     | 9          | 9        |
| 76 | 31 [Pao seco]                | NULL                     | NULL     | 9          | 9        |
| 77 | 27 [Cigarro]                 | NULL                     | NULL     | 10         | 10       |
| 78 | 5 [Lock pick]                | NULL                     | NULL     | 10         | 10       |
| 79 | 23 [Garrafa de vidro]        | NULL                     | NULL     | 11         | 11       |
| 80 | 21 [Alcool]                  | NULL                     | NULL     | 11         | 11       |
| 81 | 24 [Plastico]                | NULL                     | NULL     | 12         | 12       |
| 82 | 10 [Faca curta]              | NULL                     | NULL     | 12         | 12       |
| 83 | 16 [Graveto]                 | NULL                     | NULL     | 13         | 13       |
| 84 | 9 [Soco ingles]              | NULL                     | NULL     | 13         | 13       |
| 85 | 27 [Cigarro]                 | NULL                     | NULL     | 14         | 14       |
| 86 | 25 [Isqueiro]                | NULL                     | NULL     | 14         | 14       |
| 87 | 26 [Lanterna]                | NULL                     | NULL     | 15         | 15       |
| 88 | 28 [Anti inflamatorio]       | NULL                     | NULL     | 15         | 15       |
| 89 | 25 [Isqueiro]                | NULL                     | NULL     | 16         | 16       |
| 80 | 30 [Bandagem]                | NULL                     | NULL     | 16         | 16       |
| 91 | 23 [Garrafa de vidro]        | NULL                     | NULL     | 17         | 17       |
| 92 | 21 [Alcool]                  | NULL                     | NULL     | 17         | 17       |
| 93 | 23 [Garrafa de vidro]        | NULL                     | NULL     | 18         | 18       |
| 94 | 22 [Tecido]                  | NULL                     | NULL     | 18         | 18       |
| 95 | 11 [Coquetel Molotov]        | NULL                     | NULL     | 19         | 19       |
| 96 | 28 [Anti-inflamatorio]       | NULL                     | NULL     | 19         | 19       |
| 97 | 12 [Corda com cerol]         | NULL                     | NULL     | 20         | 20       |
| 98 | 20 [Pedaco grande de metal]  | NULL                     | NULL     | 20         | 20       |

---

# Tabela Item_Fabricavel

| nome                  | tipo         |
|-----------------------|--------------|
| 1 [Chave de fenda]    | 'ferramenta' |
| 2 [Pa]                | 'ferramenta' |
| 3 [Martelo]           | 'ferramenta' |
| 4 [Picareta]          | 'ferramenta' |
| 5 [Lock pick]         | 'ferramenta' |
| 6 [Corda]             | 'ferramenta' |
| 7 [Faca]              | 'arma'       |
| 8 [Adaga]             | 'arma'       |
| 9 [Soco ingles]       | 'arma'       |
| 10 [Faca curta]       | 'arma'       |
| 11 [Coquetel molotov] | 'arma'       |
| 12 [Corda com cerol]  | 'arma'       |
| 13 [Garrafa quebrada] | 'arma'       |

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

# Tabela Comida

| id  | nome     | tamanho | descricao                                                                        | raridade | quantidade | recuperacao_vida |
| --- | -------- | ------- | -------------------------------------------------------------------------------- | -------- | ---------- |------------------|
| 31  | Pao seco | 1       | um pão tão seco e duro, que parece que o proprio vandor amassou ele.             | 0        | 1          | 0                |
| 32  | Pao      | 1       | alimento básico feito a partir de farinha, água e fermento.                      | 0        | 3          | 1                |
| 33  | Queijo   | 1       | produto lácteo sólido feito a partir da coagulação do leite.                     | 0        | 3          | 1                |
| 34  | Carne    | 2       | é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento. | 2        | 1          | 5                |
| 35  | Peixe    | 1       | tecido muscular de peixe, consumido como alimento.                               | 1        | 2          | 3                |
| 36  | Laranja  | 1       | fruta cítrica, suculenta e doce.                                                 | 0        | 3          | 1                |

---

# Tabela Medicamento

| id  | nome              | tamanho | descricao                                                                          | raridade | quantidade | cura |
| --- | ----------------- | ------- | ---------------------------------------------------------------------------------- | -------- | ---------- | ---- |
| 28  | anti-inflamatorio | 1       | Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.             | 2        | 5          | 3    |
| 29  | Morfina           | 1       | Analgésico opiáceo potente utilizado para aliviar dores intensas.                  | 1        | 2          | 10   |
| 30  | Bandagem          | 1       | Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo. | 0        | 5          | 2    |
  
---

# Tabela Utilizavel

| id  | nome                    | tamanho | descricao_Efeito                                                                                                | raridade | quantidade | durabilidae |
| --- | ----------------------- | ------- | --------------------------------------------------------------------------------------------------------------- |----------| ---------- |-------------|
| 14  | Sabao                   | 1       | serve para remover sujeira e impurezas de superfícies e objetos, também é um material para fabricação de itens. | 0        | 1          | 1           |
| 15  | Pedra                   | 1       | A pedra serve para construção e também é um material para fabricação de itens.                                  | 0        | 3          | 1           |
| 16  | graveto                 | 1       | Produto de origem vegetal, é usado como material para fabricação de itens.                                      | 0        | 3          | 1           |
| 17  | linha                   | 1       | fio fino e flexível utilizado como material para fabricação de itens.                                           | 0        | 3          | 1           |
| 18  | pedaco pequeno de metal | 1       | Corda revestida com vidro moído para causar cortes.                                                             | 1        | 3          | 1           |
| 19  | vidro                   | 1       | utilizado como material para fabricação de cerol.                                                               | 0        | 1          | 1           |
| 20  | pedaco grande de metal  | 3       | Garrafa de vidro quebrada, usada como arma cortante.                                                            | 2        | 1          | 1           |
| 21  | alcool                  | 1       | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1        | 1          | 1           |
| 22  | tecido                  | 1       | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.                                           | 1        | 3          | 1           |
| 23  | garrada de vidro        | 2       | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1        | 1          | 1           |
| 24  | plastico                | 1       | Corda revestida com vidro moído para causar cortes.                                                             | 0        | 3          | 1           |
| 25  | Isqueiro                | 1       | Isqueiro é um dispositivo portátil utilizado para gerar fogo, podendo ser utilizado para queimar coisas.        | 1        | 1          | 1           |
| 26  | Lanterna                | 1       | Lanterna é um dispositivo portátil que emite luz.                                                               | 1        | 1          | 1           |
| 27  | cigarro                 | 1       | Moeda de troca do jogo, além de poder ser utilizado para acalmar.                                               | 1        | 10         | 1           |

---

# Tabela Fabricacao

| id | *item*                | livro                    |
|----|-----------------------|--------------------------|
| 1  | 1 [Chave de fenda]    | 1 [Livro de Crafts EASY] |
| 2  | 2 [Pa]                | 1 [Livro de Crafts EASY] |
| 3  | 3 [Martelo]           | 1 [Livro de Crafts EASY] |
| 4  | 4 [Lock pick]         | 1 [Livro de Crafts EASY] |
| 5  | 5 [Corda]             | 1 [Livro de Crafts EASY] |
| 6  | 6 [Adaga]             | 1 [Livro de Crafts EASY] |
| 7  | 7 [Faca curta]        | 1 [Livro de Crafts EASY] |
| 8  | 8 [Corda com cerol]   | 1 [Livro de Crafts EASY] |
| 9  | 9 [Garrafa quebrada]  | 1 [Livro de Crafts EASY] |
| 10 | 10 [Picareta]         | 2 [Livro de Crafts HARD] |
| 11 | 11 [Faca]             | 2 [Livro de Crafts HARD] |
| 12 | 12 [Soco ingles]      | 2 [Livro de Crafts HARD] |
| 13 | 13 [Coquetel molotov] | 2 [Livro de Crafts HARD] |

---

# Tabela Lista_Fabricacao

| fabricacao            | `item_fabricavel`     | item                         |
|-----------------------|-----------------------|:-----------------------------|
| 1 [Chave de fenda]    | 1 [Chave de fenda]    | 18 [Pedaco pequeno de metal] |
| 1 [Chave de fenda]    | 1 [Chave de fenda]    | 24 [Plastico]                |
| 2 [Pa]                | 2 [Pa]                | 16 [Graveto]                 |
| 2 [Pa]                | 2 [Pa]                | 20 [Pedaco grande de metal]  |
| 2 [Pa]                | 2 [Pa]                | 17 [Linha]                   |
| 3 [Martelo]           | 3 [Martelo]           | 15 [Pedra]                   |
| 3 [Martelo]           | 3 [Martelo]           | 16 [Graveto]                 |
| 4 [Picareta]          | 4 [Picareta]          | 20 [Pedaco grande de metal]  |
| 4 [Picareta]          | 4 [Picareta]          | 16 [Graveto]                 |
| 4 [Picareta]          | 4 [Picareta]          | 22 [Tecido]                  |
| 5 [Lock pick]         | 5 [Lock pick]         | 16 [Graveto]                 |
| 5 [Lock pick]         | 5 [Lock pick]         | 18 [Pedaco pequeno de metal] |
| 6 [Corda]             | 6 [Corda]             | 24 [Plastico]                |
| 7 [Faca]              | 7 [Faca]              | 20 [Pedaco grande de metal]  |
| 7 [Faca]              | 7 [Faca]              | 22 [Tecido]                  |
| 8 [Adaga]             | 8 [Adaga]             | 18 [Pedaco pequeno de metal] |
| 9 [Soco ingles]       | 9 [Soco ingles]       | 14 [Sabao]                   |
| 9 [Soco ingles]       | 9 [Soco ingles]       | 22 [Tecido]                  |
| 10 [Faca curta]       | 10 [Faca curta]       | 18 [Pedaco pequeno de metal] |
| 10 [Faca curta]       | 10 [Faca curta]       | 22 [Tecido]                  |
| 11 [Coquetel molotov] | 11 [Coquetel molotov] | 23 [Garrafa de vidro]        |
| 11 [Coquetel molotov] | 11 [Coquetel molotov] | 21 [Alcool]                  |
| 11 [Coquetel molotov] | 11 [Coquetel molotov] | 22 [Tecido]                  |
| 12 [Corda com cerol]  | 12 [Corda com cerol]  | 6 [Corda]                    |
| 12 [Corda com cerol]  | 12 [Corda com cerol]  | 19 [Vidro]                   |
| 13 [Garrafa quebrada] | 13 [Garrafa quebrada] | 23 [Garrafa de vidro]        |

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

| id | nome       | prisao      | descricao                                                                                           |
|----|------------|-------------|-----------------------------------------------------------------------------------------------------|
| 1  | celas      | 1 [Basilio] | Local onde estão as celas e solitárias dos prisioneiros.                                            |
| 2  | banheiros  | 1 [Basilio] | Local onde os prisioneiros se banham.                                                               |
| 3  | enfermaria | 1 [Basilio] | Local onde os prisioneiros podem se tratar/curar.                                                   |
| 4  | refeitorio | 1 [Basilio] | Local onde os prisioneiros fazem suas refeições.                                                    |
| 5  | patio      | 1 [Basilio] | Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete/futsal e relaxar. |
| 6  | oficinas   | 1 [Basilio] | Local onde os prisioneiros trabalham e ganham um pouco de dinheiro.                                 |

---

# Tabela Lugar

| id | nome                | *regiao*       | descricao                                                                                |
|----|---------------------|----------------|------------------------------------------------------------------------------------------|
| 1  | solitaria Oeste     | 1 [celas]      | Cela para os prisioneiros levadinhos. Na parede direita há uma mancha de cimento fresco. |
| 2  | cela A              | 1 [celas]      | Cela onde dormem os prisioneiros 1 e 2.                                                  |
| 3  | cela B              | 1 [celas]      | Cela onde dormem os prisioneiros 3 e 4.                                                  |
| 4  | cela C              | 1 [celas]      | Cela onde dormem os prisioneiros 5 e 6.                                                  |
| 5  | cela D              | 1 [celas]      | Cela onde dormem os prisioneiros 7 e 8.                                                  |
| 6  | cela E              | 1 [celas]      | Cela onde dormem os prisioneiros 9 e 10.                                                 |
| 7  | cela F              | 1 [celas]      | Cela onde dormem os prisioneiros 11 e 12.                                                |
| 8  | cela G              | 1 [celas]      | Cela onde dormem o prisioneiro 13 e o jogador.                                           |
| 9  | solitaria Leste     | 1 [celas]      | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas.   |
| 10 | corredor Celas      | 1 [celas]      | Corredor para se deslocar entre as celas e as solitárias.                                |
| 11 | banheiro A          | 2 [banheiros]  | Banheiro onde os prisioneiros tomam banho.                                               |
| 12 | banheiro B          | 2 [banheiros]  | Banheiro onde os prisioneiros tomam banho.                                               |
| 13 | banheiro C          | 2 [banheiros]  | Banheiro onde os prisioneiros tomam banho.                                               |
| 14 | banheiro D          | 2 [banheiros]  | Banheiro onde os prisioneiros tomam banho.                                               |
| 15 | corredor Banheiros  | 2 [banheiros]  | Corredor para se deslocar entre os banheiros.                                            |
| 16 | sala A              | 3 [enfermaria] | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 17 | sala B              | 3 [enfermaria] | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 18 | sala C              | 3 [enfermaria] | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 19 | corredor Enfermaria | 3 [enfermaria] | Corredor para se deslocar entre as salas da enfermaria.                                  |
| 20 | mesa Esquerda       | 4 [refeitorio] | Mesa onde a gangue 1 faz suas refeições.                                                 |
| 21 | mesa Direita        | 4 [refeitorio] | Mesa onde a gangue 2 faz suas refeições.                                                 |
| 22 | corredor Refeitorio | 4 [refeitorio] | Corredor para se deslocar entre as mesas do refeitório.                                  |
| 23 | academia Simples    | 5 [patio]      | Uma área com equipamentos simples de exercício.                                          |
| 24 | quadra De Basquete  | 5 [patio]      | Quadra onde os prisioneiros jogam basquete/futsal para se distrair e se exercitar.       |
| 25 | arquibancada        | 5 [patio]      | Arquibancada onde os prisioneiros podem conversar e assistir os jogos.                   |
| 26 | area De Lazer       | 5 [patio]      | Bancos onde os prisioneiros podem sentar e conversar.                                    |
| 27 | corredor Patio      | 5 [patio]      | Corredor para se deslocar entre as áreas do pátio e as oficinas.                         |
| 28 | oficina A           | 6 [oficinas]   | Oficina de marcenaria onde os prisioneiros trabalham.                                    |
| 29 | oficina B           | 6 [oficinas]   | Oficina de impressão de placas de carro onde os prisioneiros trabalham.                  |

---

# Tabela Lugar_Origem_Destino

| lugar_origem             | `regiao_origem` | lugar_destino            | `regiao_destino` |
|--------------------------|-----------------|--------------------------|------------------|
| 1 [solitaria Oeste]      | 1 [celas]       | 2 [cela A]               | 1 [celas]        |
| 1 [solitaria Oeste]      | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 2 [cela A]               | 1 [celas]       | 1 [solitaria Oeste]      | 1 [celas]        |
| 2 [cela A]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 3 [cela B]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 4 [cela C]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 5 [cela D]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 6 [cela E]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 7 [cela F]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 8 [cela G]               | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 9 [solitaria Leste]      | 1 [celas]       | 10 [corredor Celas]      | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 1 [solitaria Oeste]      | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 2 [cela A]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 3 [cela B]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 4 [cela C]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 5 [cela D]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 6 [cela E]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 7 [cela F]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 8 [cela G]               | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 9 [solitaria Leste]      | 1 [celas]        |
| 10 [corredor Celas]      | 1 [celas]       | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 11 [banheiro A]          | 2 [banheiros]   | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 12 [banheiro B]          | 2 [banheiros]   | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 13 [banheiro C]          | 2 [banheiros]   | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 14 [banheiro D]          | 2 [banheiros]   | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 10 [corredor Celas]      | 1 [celas]        |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 11 [banheiro A]          | 2 [banheiros]    |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 12 [banheiro B]          | 2 [banheiros]    |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 13 [banheiro C]          | 2 [banheiros]    |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 14 [banheiro D]          | 2 [banheiros]    |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 19 [corredor Enfermaria] | 3 [enfermaria]   |
| 15 [corredor Banheiros]  | 2 [banheiros]   | 22 [corredor Refeitorio] | 4 [refeitorio]   |
| 16 [sala A]              | 3 [enfermaria]  | 17 [sala B]              | 3 [enfermaria]   |
| 16 [sala A]              | 3 [enfermaria]  | 19 [corredor Enfermaria] | 3 [enfermaria]   |
| 17 [sala B]              | 3 [enfermaria]  | 16 [sala A]              | 3 [enfermaria]   |
| 17 [sala B]              | 3 [enfermaria]  | 18 [sala C]              | 3 [enfermaria]   |
| 17 [sala B]              | 3 [enfermaria]  | 19 [corredor Enfermaria] | 3 [enfermaria]   |
| 18 [sala C]              | 3 [enfermaria]  | 17 [sala B]              | 3 [enfermaria]   |
| 18 [sala C]              | 3 [enfermaria]  | 19 [corredor Enfermaria] | 3 [enfermaria]   |
| 19 [corredor Enfermaria] | 3 [enfermaria]  | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 19 [corredor Enfermaria] | 3 [enfermaria]  | 16 [sala A]              | 3 [enfermaria]   |
| 19 [corredor Enfermaria] | 3 [enfermaria]  | 17 [sala B]              | 3 [enfermaria]   |
| 19 [corredor Enfermaria] | 3 [enfermaria]  | 18 [sala C]              | 3 [enfermaria]   |
| 20 [mesa Esquerda]       | 4 [refeitorio]  | 22 [corredor Refeitorio] | 4 [refeitorio]   |
| 21 [mesa Direita]        | 4 [refeitorio]  | 22 [corredor Refeitorio] | 4 [refeitorio]   |
| 22 [corredor Refeitorio] | 4 [refeitorio]  | 15 [corredor Banheiros]  | 2 [banheiros]    |
| 22 [corredor Refeitorio] | 4 [refeitorio]  | 20 [mesa Esquerda]       | 4 [refeitorio]   |
| 22 [corredor Refeitorio] | 4 [refeitorio]  | 21 [mesa Direita]        | 4 [refeitorio]   |
| 22 [corredor Refeitorio] | 4 [refeitorio]  | 27 [corredor Patio ]     | 5 [patio]        |
| 23 [academia Simples]    | 5 [patio]       | 24 [quadra De Basquete]  | 5 [patio]        |
| 23 [academia Simples]    | 5 [patio]       | 27 [corredor Patio ]     | 5 [patio]        |
| 24 [quadra De Basquete]  | 5 [patio]       | 23 [academia Simples]    | 5 [patio]        |
| 24 [quadra De Basquete]  | 5 [patio]       | 25 [arquibancada]        | 5 [patio]        |
| 24 [quadra De Basquete]  | 5 [patio]       | 27 [corredor Patio ]     | 5 [patio]        |
| 25 [arquibancada]        | 5 [patio]       | 24 [quadra De Basquete]  | 5 [patio]        |
| 25 [arquibancada]        | 5 [patio]       | 26 [area De Lazer]       | 5 [patio]        |
| 25 [arquibancada]        | 5 [patio]       | 27 [corredor Patio ]     | 5 [patio]        |
| 26 [area De Lazer]       | 5 [patio]       | 25 [arquibancada]        | 5 [patio]        |
| 26 [area De Lazer]       | 5 [patio]       | 27 [corredor Patio ]     | 5 [patio]        |
| 27 [corredor Patio ]     | 5 [patio]       | 22 [corredor Refeitorio] | 4 [refeitorio]   |
| 27 [corredor Patio ]     | 5 [patio]       | 23 [academia Simples]    | 5 [patio]        |
| 27 [corredor Patio ]     | 5 [patio]       | 24 [quadra De Basquete]  | 5 [patio]        |
| 27 [corredor Patio ]     | 5 [patio]       | 25 [arquibancada]        | 5 [patio]        |
| 27 [corredor Patio ]     | 5 [patio]       | 26 [area De Lazer]       | 5 [patio]        |
| 27 [corredor Patio ]     | 5 [patio]       | 28 [oficina A]           | 6 [oficinas]     |
| 27 [corredor Patio ]     | 5 [patio]       | 29 [oficina B]           | 6 [oficinas]     |
| 28 [oficina A]           | 6 [oficinas]    | 27 [corredor Patio ]     | 5 [patio]        |
| 29 [oficina B]           | 6 [oficinas]    | 27 [corredor Patio ]     | 5 [patio]        |

---

# Tabela Pessoa

| id | tipo          |
|----|---------------|
| 1  | 'jogador'     |
| 2  | 'prisioneiro' |
| 3  | 'prisioneiro' |
| 4  | 'prisioneiro' |
| 5  | 'prisioneiro' |
| 6  | 'prisioneiro' |
| 7  | 'prisioneiro' |
| 8  | 'prisioneiro' |
| 9  | 'prisioneiro' |
| 10 | 'prisioneiro' |
| 11 | 'prisioneiro' |
| 12 | 'prisioneiro' |
| 13 | 'prisioneiro' |
| 14 | 'policial'    |
| 15 | 'policial'    |
| 16 | 'policial'    |
| 17 | 'policial'    |
| 18 | 'policial'    |
| 19 | 'informante'  |
| 20 | 'informante'  |

---

# Tabela Inventario

| id | *pessoa* | inventario_ocupado | tamanho |
|----|----------|--------------------|---------|
| 1  | 1        | 0                  | 5       |
| 2  | 2        | 4                  | 5       |
| 3  | 3        | 3                  | 5       |
| 4  | 4        | 3                  | 5       |
| 5  | 5        | 4                  | 5       |
| 6  | 6        | 3                  | 5       |
| 7  | 7        | 2                  | 5       |
| 8  | 8        | 3                  | 5       |
| 9  | 9        | 2                  | 5       |
| 10 | 10       | 2                  | 5       |
| 11 | 11       | 3                  | 5       |
| 12 | 12       | 2                  | 5       |
| 13 | 13       | 2                  | 5       |
| 14 | 14       | 2                  | 5       |
| 15 | 15       | 2                  | 5       |
| 16 | 16       | 2                  | 5       |
| 17 | 17       | 3                  | 5       |
| 18 | 18       | 3                  | 5       |
| 19 | 19       | 2                  | 5       |
| 20 | 20       | 4                  | 5       |

----

# Tabela Prisioneiro

| id | nome         | habilidade_briga | vida | força | gangue     | lugar                 | `regiao`       |
|----|--------------|------------------|------|-------|------------|-----------------------|----------------|
| 2  | Rivas        | 4                | 9    | 7     | 'Palhacos' | 24 [quadraDeBasquete] | 5 [patio]      |
| 3  | Filomano     | 6                | 7    | 4     | 'Polvos'   | 3 [cela B]            | 1 [celas]      |
| 4  | Fragas       | 5                | 11   | 5     | 'Palhacos' | 11 [banheiro A]       | 2 [banheiros]  |
| 5  | Glaucão      | 3                | 6    | 8     | 'Polvos'   | 20 [mesa Esquerda]    | 4 [refeitorio] |
| 6  | Ucraniano    | 7                | 5    | 6     | 'Palhacos' | 4 [cela C]            | 1 [celas]      |
| 7  | Rispomático  | 6                | 12   | 6     | 'Polvos'   | 23 [academia Simples] | 5 [patio]      |
| 8  | Manogaz      | 4                | 8    | 5     | 'Palhacos' | 8 [cela G]            | 1 [celas]      |
| 9  | Dado         | 5                | 10   | 6     | 'Polvos'   | 12 [banheiro B]       | 2 [banheiros]  |
| 10 | Fabrilton    | 4                | 7    | 5     | 'Palhacos' | 21 [mesa Direita]     | 4 [refeitorio] |
| 11 | Eneido       | 6                | 6    | 6     | 'Polvos'   | 1 [solitaria Oeste]   | 1 [celas]      |
| 12 | Carlos       | 5                | 9    | 7     | 'Palhacos' | 25 [arquibancada]     | 5 [patio]      |
| 13 | Silvio Serra | 6                | 8    | 5     | 'Polvos'   | 6 [cela E]            | 1 [celas]      |


-----

# Tabela Policial

| id | nome                | corrupto | lugar                   | `regiao`       |
|----|---------------------|----------|-------------------------|----------------|
| 14 | Italo Dimetrio      | true     | 1 [solitaria Oeste]     | 1 [celas]      |
| 15 | Sargento Nascimento | false    | 21 [mesa Direita]       | 4 [refeitorio] |
| 16 | Capitão Mathias     | false    | 24 [quadra De Basquete] | 5 [patio]      |
| 17 | Capitão Brad        | true     | 9 [solitaria Leste]     | 1 [celas]      |
| 18 | Lil Chico           | true     | 25 [arquibancada]       | 5 [patio]      |


---

# Tabela Informante

| id | nome    | dano_infomante | lugar           | `regiao`       |
|----|---------|----------------|-----------------|----------------|
| 19 | Cubano  | 200            | 13 [banheiro C] | 2 [banheiros]  |
| 20 | Chileno | 200            | 16 [sala A]     | 3 [enfermaria] |


---

# Tabela Jogador

| id | nome    | habilidade_briga | vida | força | tempo_vida | gangue | missao | lugar      | `regiao`  |
|----|---------|------------------|------|-------|------------|--------|--------|------------|-----------|
| 1  | Carimbo | 2                | 5    | 3     | 10         | null   | null   | 2 [cela A] | 1 [celas] |

---

# Tabela Missao

| id | item                   | nome                      | descricao                                                                  | lugar                   | regiao    |
|----|------------------------|---------------------------|----------------------------------------------------------------------------|-------------------------|-----------|
| 1  | chave oficina A        | Fuja da solitaria oeste   | Escape da cela de isolamento leste sem ser pego.                           | 1 [solitaria Oeste]     | 1 [celas] |
| 2  | chave oficina B        | Fuja da solitaria leste   | Escape da cela de isolamento oeste sem ser pego.                           | 9 [solitaria Leste]     | 1 [celas] |
| 3  | BANDAGEM               | Observar  cela            | Observe e memorize os detalhes da cela para planejar uma fuga.             | 5 [cela D]              | 1 [celas] |
| 4  | FACA PEQUENA           | Escolher gangue           | Escolha a gangue com a qual se aliar na prisão.                            | NULL                    | NULL      |
| 5  | NULL                   | explorar o mapa           | Explore os locais no mapa da prisão, para um melhor entendimento do mesmo. | NULL                    | NULL      |
| 6  | CARNE                  | Brigue com alguém         | Inicie e participe de uma briga com outro prisioneiro.                     | NULL                    | NULL      |
| 7  | REMEDIO                | Vença uma briga           | Vença uma briga                                                            | NULL                    | NULL      |
| 8  | NULL                   | Fuja da prisão            | Fuja da prisão                                                             | NULL                    | NULL      |
| 9  | pedaco grande de metal | encontre o informante     | encontre o informante                                                      | NULL                    | NULL      |
| 10 | Isqueiro               | vença um jogo de basquete | vença um jogo de basquete                                                  | 24 [quadra De Basquete] | 5 [patio] |
| 11 | CARNE                  | Fique maromba             | Va na academia                                                             | 23 [academia Simples]   | 5 [patio] |


---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão |                                                                        Descrição                                                                         | Autores                                               |
|------------|--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------:|-------------------------------------------------------|
| 26/07/2024 | `1.0`  |                                                                  Criação do documento.                                                                   | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 28/07/2024 | `1.1`  |                                                     Desenvolvimento de algumas tabelas e correções.                                                      | [João Antonio G.](https://github.com/joaoseisei)      |
| 28/07/2024 | `1.2`  |                                                             Desenvolvimento algumas tabelas.                                                             | [Fernando Gabriel](https://github.com/show-dawn)      |
| 28/07/2024 | `1.3`  |                                                             Desenvolvimento algumas tabelas.                                                             | [Julio Cesar](https://github.com/Julio1099)           |
| 29/07/2024 | `1.4`  |                                                           Completa a tabela [`Lugar`](#Lugar)                                                            | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 29/07/2024 | `1.5`  |                                                                  Ajustes tabela Pessoa                                                                   | [Júlio Cesar](https://github.com/julio1099)           |
| 29/07/2024 | `1.6`  |                                                             Desenvolvimento algumas tabelas.                                                             | [Fernando Gabriel](https://github.com/show-dawn)      |
| 02/08/2024 | `1.7`  |                                                                 Correção tabela Pessoa.                                                                  | [Júlio Cesar](https://github.com/Julio1099)           |
| 04/08/2024 | `1.8`  |                                                                   Adiciona os crafts.                                                                    | [João Antonio G.](https://github.com/joaoseisei)      |
| 04/08/2024 | `1.9`  |           Corrige as tabelas [`Prisao`](#Prisao), [`Regiao`](#Regiao) e [`Lugar`](#Lugar), e cria a tabela [`Lugar_Anterior`](#Lugar_Anterior)           | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 05/08/2024 | `2.0`  |                                                            Adiciona missao e formata tabelas.                                                            | [Fernando Gabriel](https://github.com/show-dawn)      |
| 06/08/2024 | `2.1`  |                                                   Corrige a tabela [`Lugar_Proximo`](#Lugar_Proximo).                                                    | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 06/08/2024 | `2.2`  |                                                     Popula instancia de item e lista de fabricacao.                                                      | [João Antonio G.](https://github.com/joaoseisei)      |
| 06/08/2024 | `2.3`  |                               Termina de corrigir a tabela [`Tabela-Lugar_Origem_Destino`](#Tabela-Lugar_Origem_Destino).                                | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 07/08/2024 | `2.4`  |                                             Adiciona chaves compostas em lista_fabricacao e instancia_item.                                              | [João Antonio G.](https://github.com/joaoseisei)      |
| 09/08/2024 | `2.5`  | Correção das tabelas [`Tabela-Regiao`](#Tabela-Regiao), [`Tabela-Lugar`](#Tabela-Lugar) e [`Tabela-Lugar_Origem_Destino`](#Tabela-Lugar_Origem_Destino). | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 10/08/2024 | `2.6`  |                                                                     Adiciona regiao.                                                                     |  [João Antonio G.](https://github.com/joaoseisei)                                                     |

</div>
