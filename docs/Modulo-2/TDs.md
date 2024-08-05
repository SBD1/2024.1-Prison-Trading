<center>

# Tabela de dados

</center>

---

> Este documento visa monitorar e registrar os dados inseridos em cada uma das tabelas. É importante destacar que esses
> dados poderão ser atualizados ao longo do jogo conforme necessário.


---

# Prisao

| id_prisao | nome_prisao |
|-----------|-------------|
| 1         | Basilio     |

---

# Regiao

| id_regiao | nome_regiao | prisao | descricao_regiao                                                                                    |
|-----------|-------------|--------|-----------------------------------------------------------------------------------------------------|
| 1         | celas       | 1      | Local onde estão as celas e solitárias dos prisioneiros.                                            |
| 2         | banheiros   | 1      | Local onde os prisioneiros se banham.                                                               |
| 3         | enfermaria  | 1      | Local onde os prisioneiros podem se tratar/curar.                                                   |
| 4         | refeitorio  | 1      | Local onde os prisioneiros fazem suas refeições.                                                    |
| 5         | patio       | 1      | Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete/futsal e relaxar. |
| 6         | oficinas    | 1      | Local onde os prisioneiros trabalham e ganham um pouco de dinheiro.                                 |

---

# Lugar

| id_lugar | nome_lugar         | *regiao*   | descricao_lugar                                                                          |
|----------|--------------------|------------|------------------------------------------------------------------------------------------|
| 1        | solitariaOeste     | 1          | Cela para os prisioneiros levadinhos. Na parede direita há uma mancha de cimento fresco. |
| 2        | celaA              | 1          | Cela onde dormem os prisioneiros 1 e 2.                                                  |
| 3        | celaB              | 1          | Cela onde dormem os prisioneiros 3 e 4.                                                  |
| 4        | celaC              | 1          | Cela onde dormem os prisioneiros 5 e 6.                                                  |
| 5        | celaD              | 1          | Cela onde dormem os prisioneiros 7 e 8.                                                  |
| 6        | celaE              | 1          | Cela onde dormem os prisioneiros 9 e 10.                                                 |
| 7        | celaF              | 1          | Cela onde dormem os prisioneiros 11 e 12.                                                |
| 8        | celaG              | 1          | Cela onde dormem o prisioneiro 13 e o jogador.                                           |
| 9        | solitariaLeste     | 1          | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas.   |
| 10       | corredorCelas      | 1          | Corredor para se deslocar entre as celas e as solitárias.                                |
| 11       | banheiroA          | 2          | Banheiro onde os prisioneiros tomam banho.                                               |
| 12       | banheiroB          | 2          | Banheiro onde os prisioneiros tomam banho.                                               |
| 13       | banheiroC          | 2          | Banheiro onde os prisioneiros tomam banho.                                               |
| 14       | banheiroD          | 2          | Banheiro onde os prisioneiros tomam banho.                                               |
| 15       | corredorBanheiros  | 2          | Corredor para se deslocar entre os banheiros.                                            |
| 16       | salaA              | 3          | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 17       | salaB              | 3          | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 18       | salaC              | 3          | Sala com uma maca e armário com remédios e kits de primeiro-socorro.                     |
| 19       | corredorEnfermaria | 3          | Corredor para se deslocar entre as salas da enfermaria.                                  |
| 20       | mesaEsquerda       | 4          | Mesa onde a gangue 1 faz suas refeições.                                                 |
| 21       | mesaDireita        | 4          | Mesa onde a gangue 2 faz suas refeições.                                                 |
| 22       | corredorRefeitorio | 4          | Corredor para se deslocar entre as mesas do refeitório.                                  |
| 23       | academiaSimples    | 5          | Uma área com equipamentos simples de exercício.                                          |
| 24       | quadraDeBasquete   | 5          | Quadra onde os prisioneiros jogam basquete/futsal para se distrair e se exercitar.       |
| 25       | arquibancada       | 5          | Arquibancada onde os prisioneiros podem conversar e assistir os jogos.                   |
| 26       | areaDeLazer        | 5          | Bancos onde os prisioneiros podem sentar e conversar.                                    |
| 27       | corredorPatio      | 5          | Corredor para se deslocar entre as áreas do pátio e as oficinas.                         |
| 28       | oficinaA           | 6          | Oficina de marcenaria onde os prisioneiros trabalham.                                    |
| 29       | oficinaB           | 6          | Oficina de impressão de placas de carro onde os prisioneiros trabalham.                  |

---

# Lugar_Anterior

| id_lugar | id_lugar_anterior |
|----------|-------------------|
| 1        | 2                 |
| 1        | 10                |
| 2        | 1                 |
| 2        | 10                |
| 3        | 10                |
| 4        | 10                |
| 5        | 10                |
| 6        | 10                |
| 7        | 10                |
| 8        | 10                |
| 9        | 10                |
| 10       | 1                 |
| 10       | 2                 |
| 10       | 3                 |
| 10       | 4                 |
| 10       | 5                 |
| 10       | 6                 |
| 10       | 7                 |
| 10       | 8                 |
| 10       | 9                 |
| 10       | 15                |
| 11       | 15                |
| 12       | 15                |
| 13       | 15                |
| 14       | 15                |
| 15       | 10                |
| 15       | 11                |
| 15       | 12                |
| 15       | 13                |
| 15       | 14                |
| 15       | 19                |
| 15       | 22                |
| 16       | 17                |
| 16       | 19                |
| 17       | 16                |
| 17       | 18                |
| 17       | 19                |
| 18       | 17                |
| 18       | 19                |
| 19       | 15                |
| 19       | 16                |
| 19       | 17                |
| 19       | 18                |
| 20       | 22                |
| 21       | 22                |
| 22       | 15                |
| 22       | 20                |
| 22       | 21                |
| 22       | 27                |
| 23       | 24                |
| 23       | 27                |
| 24       | 23                |
| 24       | 25                |
| 24       | 27                |
| 25       | 24                |
| 25       | 26                |
| 25       | 27                |
| 26       | 25                |
| 26       | 27                |
| 27       | 22                |
| 27       | 23                |
| 27       | 24                |
| 27       | 25                |
| 27       | 26                |
| 27       | 28                |
| 27       | 29                |
| 28       | 27                |
| 29       | 27                |

---

# Item

| id_item                     | tipo_item        |
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
| 11[Coquetel_Molotov]        | 'fabricavel'     |
| 12[Corda_com_Cerol]         | 'fabricavel'     |
| 13[Garrafa_Quebrada]        | 'fabricavel'     |
| 14[sabao]                   | 'nao_fabricavel' |
| 15[pedra]                   | 'nao_fabricavel' |
| 16[graveto]                 | 'nao_fabricavel' |
| 17[linha]                   | 'nao_fabricavel' |
| 18[pedaco_pequeno_de_metal] | 'nao_fabricavel' |
| 19[vidro]                   | 'nao_fabricavel' |
| 20[pedaco_grande_de_metal]  | 'nao_fabricavel' |
| 21[alcool]                  | 'nao_fabricavel' |
| 22[tecido]                  | 'nao_fabricavel' |
| 23[garrada_de_vidro]        | 'nao_fabricavel' |
| 24[plastico]                | 'nao_fabricavel' |
| 25[Isqueiro]                | 'nao_fabricavel' |
| 26[lanterna]                | 'nao_fabricavel' |
| 27[cigarro]                 | 'nao_fabricavel' |
| 28[Anti-inflamatorio]       | 'nao_fabricavel' |
| 29[Morfina]                 | 'nao_fabricavel' |
| 30[Bandagem]                | 'nao_fabricavel' |
| 31[pao_seco]                | 'nao_fabricavel' |
| 32[pao]                     | 'nao_fabricavel' |
| 33[queijo]                  | 'nao_fabricavel' |
| 34[carne]                   | 'nao_fabricavel' |
| 35[Peixe]                   | 'nao_fabricavel' |
| 36[Laranja]                 | 'nao_fabricavel' |

---

# Instancia_Item

| id | item                         | lugar         | fabricacao            |
|----|:-----------------------------|---------------|-----------------------|
| 1  | 1 [Chave de fenda]           | OficinaA      | NULL                  |
| 2  | 2 [Pa]                       | OficinaA      | NULL                  |
| 3  | 3 [Martelo]                  | OficinaB      | NULL                  |
| 4  | 4 [Picareta]                 | OficinaB      | NULL                  |
| 5  | 5 [Lock pick]                | OficinaA      | NULL                  |
| 6  | 6 [Corda]                    | OficinaB      | NULL                  |
| 7  | 7 [Faca]                     | banheiroA     | NULL                  |
| 8  | 8 [Adaga]                    | banheiroA     | NULL                  |
| 9  | 9 [Soco ingles]              | CelaG         | NULL                  |
| 10 | 10 [Faca curta]              | CelaF         | NULL                  |
| 11 | 11 [Coquetel molotov]        | SolitariaB    | NULL                  |
| 12 | 12 [Corda com Cerol]         | CelaE         | NULL                  |
| 13 | 13 [Garrafa quebrada]        | CorredorPatio | NULL                  |
| 14 | 14 [Sabao]                   | banheiro      | NULL                  |
| 15 | 15 [Pedra]                   | patio         | NULL                  |
| 16 | 16 [Graveto]                 | patio         | NULL                  |
| 17 | 17 [Linha]                   | EnfermariaA   | NULL                  |
| 18 | 18 [Pedaco pequeno de metal] | oficinaA      | NULL                  |
| 19 | 19 [Vidro]                   | CelaB         | NULL                  |
| 20 | 20 [Pedaco grande de metal]  | CelaA         | NULL                  |
| 21 | 21 [Alcool]                  | enfermaria    | NULL                  |
| 22 | 22 [Tecido]                  | enfermaria    | NULL                  |
| 23 | 23 [Garrafa de vidro]        | enfermaria    | NULL                  |
| 24 | 24 [Plastico]                | CorredorEnfer | NULL                  |
| 25 | 25 [Isqueiro]                | CelaC         | NULL                  |
| 26 | 26 [Lanterna]                | SolitariaA    | NULL                  |
| 27 | 27 [Cigarro]                 | CorredorPatio | NULL                  |
| 28 | 28 [Anti inflamatorio]       | EnfermariaA   | NULL                  |
| 29 | 29 [Morfina]                 | EnfermariaB   | NULL                  |
| 30 | 30 [Bandagem]                | EnfermariaC   | NULL                  |
| 31 | 31 [Pao seco]                | RefeiEsq      | NULL                  | 
| 32 | 32 [Pao]                     | RefeiEsq      | NULL                  |
| 33 | 33 [Queijo]                  | RefeiEsq      | NULL                  |
| 34 | 34 [Carne]                   | RefeiDir      | NULL                  |
| 35 | 35 [Peixe]                   | RefeiDir      | NULL                  |
| 36 | 36 [Laranja]                 | RefeiDir      | NULL                  |
| 37 | 18 [Pedaco pequeno de metal] | NULL          | 1 [Chave de fenda]    |
| 38 | 24 [Plastico]                | NULL          | 1 [Chave de fenda]    |
| 39 | 16 [Graveto]                 | NULL          | 2 [Pa]                |
| 40 | 20 [Pedaco grande de metal]  | NULL          | 2 [Pa]                |
| 41 | 17 [Linha]                   | NULL          | 2 [Pa]                |
| 42 | 15 [Pedra]                   | NULL          | 3 [Martelo]           |
| 43 | 16 [Graveto]                 | NULL          | 3 [Martelo]           |
| 44 | 20 [Pedaco grande de metal]  | NULL          | 4 [Picareta]          |
| 45 | 16 [Graveto]                 | NULL          | 4 [Picareta]          |
| 46 | 22 [Tecido]                  | NULL          | 4 [Picareta]          |
| 47 | 16 [Graveto]                 | NULL          | 5 [Lock Pick]         |
| 48 | 18 [Pedaco pequeno de metal] | NULL          | 5 [Lock Pick]         |
| 49 | 24 [Plastico]                | NULL          | 6 [Corda]             |
| 50 | 20 [Pedaco grande de metal]  | NULL          | 7 [Faca]              |
| 51 | 22 [Tecido]                  | NULL          | 7 [Faca]              |
| 52 | 18 [Pedaco pequeno de metal] | NULL          | 8 [Adaga]             |
| 53 | 14 [Sabao]                   | NULL          | 9 [Soco Ingles]       |
| 54 | 22 [Tecido]                  | NULL          | 9 [Soco Ingles]       |
| 55 | 18 [Pedaco pequeno de metal] | NULL          | 10 [Faca Curta]       |
| 56 | 22 [Tecido]                  | NULL          | 10 [Faca Curta]       |
| 57 | 23 [Garrafa de vidro]        | NULL          | 11 [Coquetel Molotov] |
| 58 | 21 [Alcool]                  | NULL          | 11 [Coquetel Molotov] |
| 59 | 22 [Tecido]                  | NULL          | 11 [Coquetel Molotov] |
| 60 | 6 [Corda]                    | NULL          | 12 [Corda com Cerol]  |
| 61 | 19 [Vidro]                   | NULL          | 12 [Corda com Cerol]  |
| 62 | 23 [Garrafa de vidro]        | NULL          | 13 [Garrafa Quebrada] |

---

# Item_Fabricavel

| nome_item             | tipo_fabricavel |
|-----------------------|-----------------|
| 1 [Chave de Fenda]    | 'ferramenta'    |
| 2 [Pa]                | 'ferramenta'    |
| 3 [Martelo]           | 'ferramenta'    |
| 4 [Picareta]          | 'ferramenta'    |
| 5 [Lock Pick]         | 'ferramenta'    |
| 6 [Corda]             | 'ferramenta'    |
| 7 [Faca]              | 'arma'          |
| 8 [Adaga]             | 'arma'          |
| 9 [Soco Ingles]       | 'arma'          |
| 10 [Faca Curta]       | 'arma'          |
| 11 [Coquetel Molotov] | 'arma'          |
| 12 [Corda com Cerol]  | 'arma'          |
| 13 [Garrafa Quebrada] | 'arma'          |

---

# Item_nao_Fabricavel

| id_item                     | tipo_nao_fabricavel |
|-----------------------------|---------------------|
| 14[sabao]                   | 'utilizavel'        |
| 15[pedra]                   | 'utilizavel'        |
| 16[graveto]                 | 'utilizavel'        |
| 17[linha]                   | 'utilizavel'        |
| 18[pedaco_pequeno_de_metal] | 'utilizavel'        |
| 19[vidro]                   | 'utilizavel'        |
| 20[pedaco_grande_de_metal]  | 'utilizavel'        |
| 21[alcool]                  | 'utilizavel'        |
| 22[tecido]                  | 'utilizavel'        |
| 23[garrada_de_vidro]        | 'utilizavel'        |
| 24[plastico]                | 'utilizavel'        |
| 25[Isqueiro]                | 'utilizavel'        |
| 26[lanterna]                | 'utilizavel'        |
| 27[cigarro]                 | 'utilizavel'        |
| 28[Anti-inflamatorio]       | 'medicamento'       |
| 29[Morfina]                 | 'medicamento'       |
| 30[Bandagem]                | 'medicamento'       |
| 31[pao_seco]                | 'comida'            |
| 32[pao]                     | 'comida'            |
| 33[queijo]                  | 'comida'            |
| 34[carne]                   | 'comida'            |
| 35[Peixe]                   | 'comida'            |
| 36[Laranja]                 | 'comida'            |

---

# Ferramenta

| id_item | nome_item      | tamanho_item | descricao_item                                                                                    | utilidade_ferramenta                              |
|---------|----------------|--------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| 1       | Chave de Fenda | 1            | Ferramenta com ponta plana ou cruzada para apertar ou soltar parafusos.                           | Usada para desmontar objetos.                     |
| 2       | Pa             | 2            | Ferramenta com lâmina larga e plana para cavar e mover materiais.                                 | Ideal para escavar ou remover detritos.           |
| 3       | Martelo        | 2            | Ferramenta com cabeça pesada usada para bater pregos ou quebrar objetos.                          | Usado em construção e demolição.                  |
| 4       | Picareta       | 2            | Ferramenta com uma extremidade pontiaguda e outra achatada, usada para quebrar superfícies duras. | Ideal para mineração ou demolição.                |
| 5       | Lock Pick      | 1            | Ferramenta fina e estreita usada para destrancar fechaduras sem chave.                            | Utilizada para abrir fechaduras de forma furtiva. |
| 6       | Corda          | 1            | Cordão grosso feito de fibras entrelaçadas.                                                       | Usada para amarrar, puxar ou escalar.             |

---

# Arma

| id_item | nome_item        | tamanho_item | descricao_item                                                               | dano_arma | arma_equipada |
|---------|------------------|--------------|------------------------------------------------------------------------------|-----------|---------------|
| 7       | Faca             | 2            | Lâmina afiada e curta usada para cortar ou perfurar.                         | 3         | False         |
| 8       | Adaga            | 1            | Ferramenta fina e pontiaguda.                                                | 1         | False         |
| 9       | Soco Ingles      | 1            | Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo. | 2         | False         |
| 10      | Faca Curta       | 1            | Pequena faca com lâmina curta, fácil de esconder.                            | 2         | False         |
| 11      | Coquetel Molotov | 1            | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.        | 5         | False         |
| 12      | Corda com Cerol  | 1            | Corda revestida com vidro moído para causar cortes.                          | 3         | False         |
| 13      | Garrafa Quebrada | 1            | Garrafa de vidro quebrada, usada como arma cortante.                         | 3         | False         |

---

# Medicamento

| id_item | nome_item         | tamanho_item | descricao_item                                                                     | raridade_nao_fabricavel | cura_medicamento | medicamento_quantidade |
|---------|-------------------|--------------|------------------------------------------------------------------------------------|-------------------------|------------------|------------------------|
| 28       | anti-inflamatorio | 1            | Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.             | 2                      | 3                | 5                      |
| 29       | Morfina           | 1            | Analgésico opiáceo potente utilizado para aliviar dores intensas.                  | 1                       | 10               | 2                      |
| 30       | Bandagem          | 1            | Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo. | 0                       | 2                | 5                      |

---

# Comida

| id_item | nome_item | tamanho_item | descricao_item                                                                   | raridade_nao_fabricavel | comida_quantidade | cura_comida |
|---------|-----------|--------------|----------------------------------------------------------------------------------|-------------------------|-------------------|-------------|
| 31       | Pao seco  | 1            | um pão tão seco e duro, que parece que o proprio vandor amassou ele.             | 0                       | 1                 | 0           |
| 32       | Pao       | 1            | alimento básico feito a partir de farinha, água e fermento.                      | 0                       | 3                 | 1           |
| 33       | Queijo    | 1            | produto lácteo sólido feito a partir da coagulação do leite.                     | 0                       | 3                 | 1           |
| 34       | Carne     | 2            | é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento. | 2                      | 1                 | 5           |
| 35       | Peixe     | 1            | tecido muscular de peixe, consumido como alimento.                               | 1                       | 2                 | 3           |
| 36       | Laranja   | 1            | fruta cítrica, suculenta e doce.                                                 | 0                       | 3                 | 1           |

  
---

# Utilizavel

| id_item                     | nome_item | tamanho_item | descricao_Efeito_item                                                                                           | quantidade_utilizavel |
|-----------------------------|-----------|--------------|-----------------------------------------------------------------------------------------------------------------|-----------------------| 
| 14                   |     Sabao      | 1            | serve para remover sujeira e impurezas de superfícies e objetos, também é um material para fabricação de itens. | 1                     | 
| 15                   |     Pedra      | 1            | A pedra serve para construção e também é um material para fabricação de itens.                                  | 3                     |
| 16                   |     graveto    | 1            | Produto de origem vegetal, é usado como material para fabricação de itens.                                      | 3                     | 
| 17                   |     linha      | 1            | fio fino e flexível utilizado como material para fabricação de itens.                                           | 3                     |
| 18            |pedaco_pequeno_de_metal| 1            | Corda revestida com vidro moído para causar cortes.                                                             | 3                     |
| 19                   |     vidro      | 1            | utilizado como material para fabricação de cerol.                                                               | 1                     |
| 20             |pedaco_grande_de_metal| 3            | Garrafa de vidro quebrada, usada como arma cortante.                                                            | 1                     | 
| 21                   |     alcool     | 1            | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1                     |
| 22                   |     tecido     | 1            | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.                                           | 3                     |
| 23                   |garrada_de_vidro| 2            | utilizado como material para fabricação de coctel molotov e garrafa quebrada.                                   | 1                     |
| 24                   |     plastico   | 1            | Corda revestida com vidro moído para causar cortes.                                                             | 3                     |
| 25                   |     Isqueiro   | 1            | Isqueiro é um dispositivo portátil utilizado para gerar fogo, podendo ser utilizado para queimar coisas.        | 1                     |
| 26                   |     Lanterna   | 1            | Lanterna é um dispositivo portátil que emite luz.                                                               | 1                     |
| 27                   |     cigarro    | 1            | Moeda de troca do jogo, além de poder ser utilizado para acalmar.                                               | 10                    |

---

# Fabricacao

| id_fabricacao | *item_fabricavel*     | livro_fabricacao         |
|---------------|-----------------------|--------------------------|
| 1             | 1 [Chave de Fenda]    | 1 [Livro de Crafts EASY] |
| 2             | 2 [Pa]                | 1 [Livro de Crafts EASY] |
| 3             | 3 [Martelo]           | 1 [Livro de Crafts EASY] |
| 4             | 4 [Lock Pick]         | 1 [Livro de Crafts EASY] |
| 5             | 5 [Corda]             | 1 [Livro de Crafts EASY] |
| 6             | 6 [Adaga]            | 1 [Livro de Crafts EASY] |
| 7             | 7 [Faca Curta]        | 1 [Livro de Crafts EASY] |
| 8             | 8 [Corda com Cerol]   | 1 [Livro de Crafts EASY] |
| 9             | 9 [Garrafa Quebrada]  | 1 [Livro de Crafts EASY] |
| 10            | 10 [Picareta]         | 2 [Livro de Crafts HARD] |
| 11            | 11 [Faca]             | 2 [Livro de Crafts HARD] |
| 12            | 12 [Soco Ingles]      | 2 [Livro de Crafts HARD] |
| 13            | 13 [Coquetel Molotov] | 2 [Livro de Crafts HARD] |

---

# Livro_Fabricacao

| id_livro_fabricacao | nome_livro_fabricacao |
|---------------------|-----------------------|
| 1                   | Livro de Crafts EASY  |
| 2                   | Livro de Crafts HARD  |

---

## Pessoa

| IdPersonagem | tipo_pessoa   | 
|--------------|---------------|
| 1            | 'Prisioneiro' |
| 2            | 'Prisioneiro' |
| 3            | 'Prisioneiro' |
| 4            | 'Prisioneiro' |
| 5            | 'Prisioneiro' |
| 6            | 'Prisioneiro' |
| 7            | 'Prisioneiro' |
| 8            | 'Prisioneiro' |
| 9            | 'Prisioneiro' |
| 10           | 'Prisioneiro' |
| 11           | 'Prisioneiro' |
| 12           | 'Prisioneiro' |
| 13           | 'Prisioneiro' |
| 14           | 'Policial'    |
| 15           | 'Policial'    |
| 16           | 'Policial'    |
| 17           | 'Policial'    |
| 18           | 'Policial'    |
| 19           | 'Informante'  |

---

# Jogador

| **id_pessoa** | **nome_pessoa** | **habilidade_briga_jogador** | **vida_jogador** | **força_jogador** | **tempo_vida_jogador** | **gangue_jogador** | **lugar** | **missao** |
|---------------|-----------------|------------------------------|------------------|-------------------|------------------------|--------------------|-----------|------------|
| 01            | Carimbo         | 2                            | 5                | 3                 | 10                     | null               | celaA     | null       |

----

# Prisioneiro

| **id_pessoa** | **nome_pessoa** | **habilidade_briga_prisioneiro** | **vida_prisioneiro** | **força_prisioneiro** | **gangue_prisioneiro** | **lugar**        |
|---------------|-----------------|----------------------------------|----------------------|-----------------------|------------------------|------------------|
| 2             | Rivas           | 4                                | 9                    | 7                     | 'Palhacos'             | quadraDesportiva |
| 3             | Filomano        | 6                                | 7                    | 4                     | 'Polvos'               | celaB            |
| 4             | Fragas          | 5                                | 11                   | 5                     | 'Palhacos'             | banheiroA        |
| 5             | Glaucão         | 3                                | 6                    | 8                     | 'Polvos'               | mesaEsquerda     |
| 6             | Ucraniano       | 7                                | 5                    | 6                     | 'Palhacos'             | celaC            |
| 7             | Rispomático     | 6                                | 12                   | 6                     | 'Polvos'               | academiaSimples  |
| 8             | Manogaz         | 4                                | 8                    | 5                     | 'Palhacos'             | celaG            |
| 9             | Dado            | 5                                | 10                   | 6                     | 'Polvos'               | banheiroB        |
| 10            | Fabrilton       | 4                                | 7                    | 5                     | 'Palhacos'             | mesaDireita      |
| 11            | Eneido          | 6                                | 6                    | 6                     | 'Polvos'               | solitariaOeste   |
| 12            | Carlos          | 5                                | 9                    | 7                     | 'Palhacos'             | arquibancada     |
| 13            | Silvio Serra    | 6                                | 8                    | 5                     | 'Polvos'               | celaE            |

-----

# Policial

| **id_pessoa** | **nome_pessoa**     | **lugar**        | **policial_corrupto** |
|---------------|---------------------|------------------|-----------------------|
| 14            | Italo Dimetrio      | solitariaOeste   | true                  |
| 15            | Sargento Nascimento | mesaDireita      | false                 |
| 16            | Capitão Mathias     | quadraDesportiva | false                 |
| 17            | Capitão Brad        | solitariaLeste   | true                  |
| 18            | Lil Chico           | arquibancada     | true                  |

---

# Informante

| **id_pessoa** | **nome_pessoa** | **dano_infomante** | **lugar** |
|---------------|-----------------|--------------------|-----------|
| 19            | Cubano          | 200                | banheiroC |

---

# Inventário

|                   |            |                        |                        |            |            | 
|-------------------|------------|------------------------|------------------------|------------|------------|
| **id_inventario** | **pessoa** | **inventario_ocupado** | **tamanho_inventario** |
| 1                 | 1          | 0                      | 5                      |
| 2                 | 2          | 0                      | 5                      |
| 3                 | 3          | 0                      | 5                      |
| 4                 | 4          | 0                      | 5                      |
| 5                 | 5          | 0                      | 5                      |
| 6                 | 6          | 0                      | 5                      |
| 7                 | 7          | 0                      | 5                      |
| 8                 | 8          | 0                      | 5                      |
| 9                 | 9          | 0                      | 5                      |
| 10                | 10         | 0                      | 5                      |
| 11                | 11         | 0                      | 5                      |
| 12                | 12         | 0                      | 5                      |
| 13                | 13         | 0                      | 5                      |
| 14                | 14         | 0                      | 5                      |
| 15                | 15         | 0                      | 5                      |
| 16                | 16         | 0                      | 5                      |
| 17                | 17         | 0                      | 5                      |
| 18                | 18         | 0                      | 5                      |
| 19                | 19         | 0                      | 5                      |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão | Descrição                                                                                                                            | Autores                                               |
|------------|--------|--------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| 26/07/2024 | `1.0`  | Criação do documento.                                                                                                                | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 28/07/2024 | `1.1`  | Desenvolvimento de algumas tabelas e correções.                                                                                      | [João Antonio G.](https://github.com/joaoseisei)      |
| 28/07/2024 | `1.2`  | Desenvolvimento algumas tabelas.                                                                                                     | [Fernando Gabriel](https://github.com/show-dawn)      |
| 28/07/2024 | `1.3`  | Desenvolvimento algumas tabelas.                                                                                                     | [Julio Cesar](https://github.com/Julio1099)           |
| 29/07/2024 | `1.4`  | Completa a tabela [`Lugar`](#Lugar)                                                                                                  | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 29/07/2024 | `1.5`  | Ajustes tabela Pessoa                                                                                                                | [Júlio Cesar](https://github.com/julio1099)           |
| 29/07/2024 | `1.6`  | Desenvolvimento algumas tabelas.                                                                                                     | [Fernando Gabriel](https://github.com/show-dawn)      |
| 02/08/2024 | `1.7`  | Correção tabela Pessoa.                                                                                                              | [Júlio Cesar](https://github.com/Julio1099)           |
| 04/08/2024 | `1.8`  | Adiciona os crafts.                                                                                                                  | [João Antonio G.](https://github.com/joaoseisei)      |
| 26/07/2024 | `1.9`  | Corrige as tabelas [`Prisao`](#Prisao), [`Regiao`](#Regiao) e [`Lugar`](#Lugar), e cria a tabela [`Lugar_Anterior`](#Lugar_Anterior) | [Breno Alexandre](https://github.com/brenoalexandre0) |

</div>
