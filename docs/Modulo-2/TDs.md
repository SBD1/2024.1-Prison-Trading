<center>

# Tabela de dados

</center>

---

> Este documento visa monitorar e registrar os dados inseridos em cada uma das tabelas. É importante destacar que esses
> dados poderão ser atualizados ao longo do jogo conforme necessário.


---

# Prisão

| id_prisao | nome_prisao |
|-----------|-------------|
| 01        | Basilio     |

---

# Região

| nome_regiao | prisao | descricao_regiao                                                                                    |
|-------------|--------|-----------------------------------------------------------------------------------------------------|
| celas       | 01     | Local onde estão as celas e solitárias dos prisioneiros.                                            |
| banheiros   | 01     | Local onde os prisioneiros se banham.                                                               |
| refeitorio  | 01     | Local onde os prisioneiros fazem suas refeições.                                                    |
| patio       | 01     | Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete/futsal e relaxar. |

---

# Lugar

| nome_lugar       | *regiao*   | descricao_lugar                                                                        |
|------------------|------------|----------------------------------------------------------------------------------------|
| solitariaOeste   | celas      | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas. |
| celaA            | celas      | Cela onde dormem os prisioneiros 1 e 2.                                                |
| celaB            | celas      | Cela onde dormem os prisioneiros 3 e 4.                                                |
| celaC            | celas      | Cela onde dormem os prisioneiros 5 e 6.                                                |
| celaD            | celas      | Cela onde dormem os prisioneiros 7 e 8.                                                |
| celaE            | celas      | Cela onde dormem os prisioneiros 9 e 10.                                               |
| celaF            | celas      | Cela onde dormem os prisioneiros 11 e 12.                                              |
| celaG            | celas      | Cela onde dormem o prisioneiro 13 e o prisioneiro 19.                                  |
| solitariaLeste   | celas      | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas. |
| banheiroA        | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroB        | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroC        | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroD        | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| mesaDireita      | refeitorio | Mesa onde a gangue 1 faz suas refeições.                                               |
| mesaEsquerda     | refeitorio | Mesa onde a gangue 2 faz suas refeições.                                               |
| bancos           | patio      | Bancos onde os prisioneiros podem sentar e conversar.                                  |
| academiaSimples  | patio      | Uma área com equipamentos simples de exercício.                                        |
| arquibancada     | patio      | Arquibancada onde os prisioneiros podem conversar e assistir os jogos.                 |
| quadraDesportiva | patio      | Quadra onde os prisioneiros jogam basquete/futsal para se distrair e se exercitar.     |

---

# Item

| id_item                     | tipo_item        |
|-----------------------------|------------------|
| 1[Chave_de_Fenda]           | 'fabricavel'     |
| 2[Pa]                       | 'fabricavel'     |
| 3[Martelo]                  | 'fabricavel'     |
| 4[Picareta]                 | 'fabricavel'     |
| 5[Lock_Pick]                | 'fabricavel'     |
| 6[Corda]                    | 'fabricavel'     |
| 7[Faca]                     | 'fabricavel'     |
| 8[Agulha]                   | 'fabricavel'     |
| 9[Soco_Ingles]              | 'fabricavel'     |
| 10[Faca_Curta]              | 'fabricavel'     |
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
| 28[agulha]                  | 'nao_fabricavel' |
| 29[Anti-inflamatorio]       | 'nao_fabricavel' |
| 30[Morfina]                 | 'nao_fabricavel' |
| 31[Bandagem]                | 'nao_fabricavel' |
| 32[pao_seco]                | 'nao_fabricavel' |
| 33[pao]                     | 'nao_fabricavel' |
| 34[queijo]                  | 'nao_fabricavel' |
| 35[carne]                   | 'nao_fabricavel' |
| 36[Peixe]                   | 'nao_fabricavel' |
| 37[Laranja]                 | 'nao_fabricavel' |

---

# Instancia_Item

| id | item                         | lugar      | fabricacao |
|----|------------------------------|------------|------------|
| 1  | 1 [Chave de Fenda]           | NULL       | NULL       |
| 2  | 2 [Pa]                       | NULL       | NULL       |
| 3  | 3 [Martelo]                  | NULL       | NULL       |
| 4  | 4 [Picareta]                 | NULL       | NULL       |
| 5  | 5 [Lock Pick]                | NULL       | NULL       |
| 6  | 6 [Corda]                    | NULL       | NULL       |
| 7  | 7 [Faca]                     | banheiroA  | NULL       |
| 8  | 8 [Agulha]                   | banheiroA  | NULL       |
| 9  | 9 [Soco Ingles]              | NULL       | NULL       |
| 10 | 10 [Faca Curta]              | NULL       | NULL       |
| 11 | 11 [Coquetel Molotov]        | NULL       | NULL       |
| 12 | 12 [Corda com Cerol]         | NULL       | NULL       |
| 13 | 13 [Garrafa Quebrada]        | NULL       | NULL       |
| 14 | 14 [Chave de Fenda]          | NULL       | NULL       |
| 15 | 15 [Sabao]                   | banheiro   | NULL       |
| 16 | 16 [pedra]                   | patio      | NULL       |
| 17 | 17 [graveto]                 | patio      | NULL       |
| 18 | 18 [linha]                   | enfermaria | NULL       |
| 19 | 19 [pedaço pequeno de metal] | NULL       | NULL       |
| 20 | 20 [vidro]                   | NULL       | NULL       |
| 21 | 21 [Agulha]                  | NULL       | NULL       |
| 22 | 22 [pedaço grande de metal]  | NULL       | NULL       |
| 23 | 23 [Alcool]                  | enfermaria | NULL       |
| 24 | 24 [tecido]                  | enfermaria | NULL       |
| 25 | 25 [garrafa de vidro]        | enfermaria | NULL       |
| 26 | 26 [plastico]                | NULL       | NULL       |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |
|    |                              |            |            |

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
| 8 [Agulha]            | 'arma'          |
| 9 [Soco Ingles]       | 'arma'          |
| 10 [Faca Curta]       | 'arma'          |
| 11 [Coquetel Molotov] | 'arma'          |
| 12 [Corda com Cerol]  | 'arma'          |
| 13 [Garrafa Quebrada] | 'arma'          |

---

TODO DOLOCAR NA ORDEM E ADICIONAR DO ANTI INFLAMATORIO ATE O FINAL NA TABELA ITENS, TBM CORRIGIR O ID, JA TEM O ID 1

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
| 28[agulha]                  | 'utilizavel'        |
| 29[Anti-inflamatorio]       | 'medicamento'       |
| 30[Morfina]                 | 'medicamento'       |
| 31[Bandagem]                | 'medicamento'       |
| 32[pao_seco]                | 'comida'            |
| 33[pao]                     | 'comida'            |
| 34[queijo]                  | 'comida'            |
| 35[carne]                   | 'comida'            |
| 36[Peixe]                   | 'comida'            |
| 37[Laranja]                 | 'comida'            |

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
| 8       | Agulha           | 1            | Ferramenta fina e pontiaguda, geralmente usada para costura.                 | 1         | False         |
| 9       | Soco Ingles      | 1            | Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo. | 2         | False         |
| 10      | Faca Curta       | 1            | Pequena faca com lâmina curta, fácil de esconder.                            | 2         | False         |
| 11      | Coquetel Molotov | 1            | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.        | 5         | False         |
| 12      | Corda com Cerol  | 1            | Corda revestida com vidro moído para causar cortes.                          | 3         | False         |
| 13      | Garrafa Quebrada | 1            | Garrafa de vidro quebrada, usada como arma cortante.                         | 3         | False         |

---

TODO CORRIGIR A ORDEM E ID

# Medicamento

| id_item | nome_item         | tamanho_item | descricao_item                                                                     | raridade_nao_fabricavel | cura_medicamento | medicamento_quantidade |
|---------|-------------------|--------------|------------------------------------------------------------------------------------|-------------------------|------------------|------------------------|
| 29       | anti-inflamatorio | 1            | Medicamento utilizado para reduzir a inflamação, dor e febre no corpo.             | 2                      | 3                | 5                      |
| 30       | Morfina           | 1            | Analgésico opiáceo potente utilizado para aliviar dores intensas.                  | 1                       | 10               | 2                      |
| 31       | Bandagem          | 1            | Material flexível utilizado para proporcionar suporte a áreas lesionadas do corpo. | 0                       | 2                | 5                      |

---

CORRIGIR O ID

# Comida

| id_item | nome_item | tamanho_item | descricao_item                                                                   | raridade_nao_fabricavel | comida_quantidade | cura_comida |
|---------|-----------|--------------|----------------------------------------------------------------------------------|-------------------------|-------------------|-------------|
| 32       | Pao seco  | 1            | um pão tão seco e duro, que parece que o proprio vandor amassou ele.             | 0                       | 1                 | 0           |
| 33       | Pao       | 1            | alimento básico feito a partir de farinha, água e fermento.                      | 0                       | 3                 | 1           |
| 34       | Queijo    | 1            | produto lácteo sólido feito a partir da coagulação do leite.                     | 0                       | 3                 | 1           |
| 35       | Carne     | 2            | é o tecido muscular de animais, como bovinos ou suínos, consumido como alimento. | 2                      | 1                 | 5           |
| 36       | Peixe     | 1            | tecido muscular de peixe, consumido como alimento.                               | 1                       | 2                 | 3           |
| 37       | Laranja   | 1            | fruta cítrica, suculenta e doce.                                                 | 0                       | 3                 | 1           |

  
---

ADICIONAR O NOME NA TABELA NOME

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
| 28                   |     agulha     | 1            | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.                                           | 5                     |

---

# Fabricacao

| id_fabricacao | *item_fabricavel*     | livro_fabricacao         |
|---------------|-----------------------|--------------------------|
| 1             | 1 [Chave de Fenda]    | 1 [Livro de Crafts EASY] |
| 2             | 2 [Pa]                | 1 [Livro de Crafts EASY] |
| 3             | 3 [Martelo]           | 1 [Livro de Crafts EASY] |
| 4             | 4 [Lock Pick]         | 1 [Livro de Crafts EASY] |
| 5             | 5 [Corda]             | 1 [Livro de Crafts EASY] |
| 6             | 6 [Agulha]            | 1 [Livro de Crafts EASY] |
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

| Data       | Versão | Descrição                                       | Autores                                               |
|------------|--------|-------------------------------------------------|-------------------------------------------------------|
| 26/07/2024 | `1.0`  | Criação do documento.                           | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 28/07/2024 | `1.1`  | Desenvolvimento de algumas tabelas e correções. | [João Antonio G.](https://github.com/joaoseisei)      |
| 28/07/2024 | `1.2`  | Desenvolvimento algumas tabelas.                | [Fernando Gabriel](https://github.com/show-dawn)      |
| 28/07/2024 | `1.3`  | Desenvolvimento algumas tabelas.                | [Julio Cesar](https://github.com/Julio1099)           |
| 29/07/2024 | `1.4`  | Completa a tabela [`Lugar`](#Lugar)             | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 29/07/2024 | `1.5`  | Ajustes tabela Pessoa                           | [Júlio Cesar](https://github.com/julio1099)           |
| 29/07/2024 | `1.6`  | Desenvolvimento algumas tabelas.                | [Fernando Gabriel](https://github.com/show-dawn)      |
| 02/08/2024 | `1.7`  | Correção tabela Pessoa.                         | [Júlio Cesar](https://github.com/Julio1099)           |

</div>
