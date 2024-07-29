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

| nome_regiao | prisao | descricao_regiao                                                                                     |
|-------------|--------|------------------------------------------------------------------------------------------------------|
| celas       | 01     | Local onde estão as celas e solitárias dos prisioneiros.                                             |
| banheiros   | 01     | Local onde os prisioneiros se banham.                                                                |
| refeitorio  | 01     | Local onde os prisioneiros fazem suas refeições.                                                     |
| patio       | 01     | Local onde os prisioneiros podem interagir entre si, se exercitar, jogar basquete/futsal e relaxar. |

---

# Lugar

| nome_lugar           | *regiao*   | descricao_lugar                                                                        |
|----------------------|------------|----------------------------------------------------------------------------------------|
| solitariaOeste       | celas      | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas. |
| celaA                | celas      | Cela onde dormem os prisioneiros 1 e 2.                                                |
| celaB                | celas      | Cela onde dormem os prisioneiros 3 e 4.                                                |
| celaC                | celas      | Cela onde dormem os prisioneiros 5 e 6.                                                |
| celaD                | celas      | Cela onde dormem os prisioneiros 7 e 8.                                                |
| celaE                | celas      | Cela onde dormem os prisioneiros 9 e 10.                                               |
| celaF                | celas      | Cela onde dormem os prisioneiros 11 e 12.                                              |
| celaG                | celas      | Cela onde dormem o prisioneiro 13 e o jogador.                                         |
| solitariaLeste       | celas      | Cela onde prisioneiros levadinhos são levados para ficarem segregados dos coleguinhas. |
| banheiroA            | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroB            | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroC            | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| banheiroD            | banheiros  | Banheiro onde os prisioneiros tomam banho.                                             |
| mesaDireita          | refeitorio | Mesa onde a gangue 1 faz suas refeições.                                               |
| mesaEsquerda         | refeitorio | Mesa onde a gangue 2 faz suas refeições.                                               |
| bancos               | patio      | Bancos onde os prisioneiros podem sentar e conversar.                                  |
| academiaSimples      | patio      | Uma área com equipamentos simples de exercício.                                        |
| arquibancada         | patio      | Arquibancada onde os prisioneiros podem conversar e assistir os jogos.                 |
| quadraDesportiva     | patio      | Quadra onde os prisioneiros jogam basquete/futsal para se distrair e se exercitar.     |

---

# Item

| nome_item        | tipo_item |
|------------------|-----------|
| Chave de Fenda   | 'fabr'    |
| Pa               | 'fabr'    |
| Martelo          | 'fabr'    |
| Picareta         | 'fabr'    |
| Lock Pick        | 'fabr'    |
| Corda            | 'fabr'    |
| Faca             | 'fabr'    |
| Agulha           | 'fabr'    |
| Soco Ingles      | 'fabr'    |
| Faca Curta       | 'fabr'    |
| Coquetel Molotov | 'fabr'    |
| Corda com Cerol  | 'fabr'    |
| Garrafa Quebrada | 'fabr'    |
| sabão            | 'nfabr'   |
| pedra               | 'nfabr'    |
| graveto          | 'nfabr'    |
| linha         | 'nfabr'    |
| pedaço pequeno de metal        | 'nfabr'   |
| vidro            | 'nfabr'    |
| pedaço grande de metal             | 'nfabr'    |
| alcool          | 'nfabr'    |
| tecido      | 'nfabr'    |
| garrada de vidro       | 'nfabr'    |
| plastico | 'nfabr'    |



---

# Instancia_Item

| nome_inst          | item             | lugar     | fabricacao |
|--------------------|------------------|-----------|------------|
| Chave de Fenda I   | Chave de Fenda   | NULL      | NULL       |
| Pa I               | Pa               | NULL      | NULL       |
| Martelo I          | Martelo          | NULL      | NULL       |
| Picareta I         | Picareta         | NULL      | NULL       |
| Lock Pick I        | Lock Pick        | NULL      | NULL       |
| Corda I            | Corda            | NULL      | NULL       |
| Faca I             | Faca             | banheiroA | NULL       |
| Agulha I           | Agulha           | banheiroA | NULL       |
| Soco Ingles I      | Soco Ingles      | NULL      | NULL       |
| Faca Curta I       | Faca Curta       | NULL      | NULL       |
| Coquetel Molotov I | Coquetel Molotov | NULL      | NULL       |
| Corda com Cerol I  | Corda com Cerol  | NULL      | NULL       |
| Garrafa Quebrada I | Garrafa Quebrada | NULL      | NULL       |
| Chave de Fenda I   | Chave de Fenda   | NULL      | NULL       |
| Sabao I               | Sabao               | banheiro      | NULL       |
| pedra I          | pedra         | patio      | NULL       |
| graveto I         | graveto         | patio      | NULL       |
| linha I        | linha        | enfermaria      | NULL       |
| pedaço pequeno de metal I            | pedaço pequeno de metal            | NULL      | NULL       |
| vidro             | vidro             | NULL | NULL       |
| Agulha I           | Agulha           | NULL | NULL       |
| pedaço grande de metal I      | pedaço grande de metal      | NULL      | NULL       |
| Alcool I | Alcool | enfermaria      | NULL       |
| tecido I | tecido  | enfermaria      | NULL       |
| garrafa de vidro I | Garrafa de vidro | enfermaria      | NULL       |
| plastico I   | plastico   | NULL      | NULL       |

---

# Item_Fabricavel

| nome_item        | tipo_fabricavel |
|------------------|-----------------|
| Chave de Fenda   | 'ferr'          |
| Pa               | 'ferr'          |
| Martelo          | 'ferr'          |
| Picareta         | 'ferr'          |
| Lock Pick        | 'ferr'          |
| Corda            | 'ferr'          |
| Faca             | 'arma'          |
| Agulha           | 'arma'          |
| Soco Ingles      | 'arma'          |
| Faca Curta       | 'arma'          |
| Coquetel Molotov | 'arma'          |
| Corda com Cerol  | 'arma'          |
| Garrafa Quebrada | 'arma'          |

---

# Ferramenta

| nome_item      | tamanho_item | descricao_item                                                                                    | utilidade_ferramenta                              |
|----------------|--------------|---------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Chave de Fenda | 1            | Ferramenta com ponta plana ou cruzada para apertar ou soltar parafusos.                           | Usada para desmontar objetos.                     |
| Pa             | 2            | Ferramenta com lâmina larga e plana para cavar e mover materiais.                                 | Ideal para escavar ou remover detritos.           |
| Martelo        | 2            | Ferramenta com cabeça pesada usada para bater pregos ou quebrar objetos.                          | Usado em construção e demolição.                  |
| Picareta       | 2            | Ferramenta com uma extremidade pontiaguda e outra achatada, usada para quebrar superfícies duras. | Ideal para mineração ou demolição.                |
| Lock Pick      | 1            | Ferramenta fina e estreita usada para destrancar fechaduras sem chave.                            | Utilizada para abrir fechaduras de forma furtiva. |
| Corda          | 1            | Cordão grosso feito de fibras entrelaçadas.                                                       | Usada para amarrar, puxar ou escalar.             |

---

# Arma

| nome_item        | tamanho_item | descricao_item                                                               | dano_arma | arma_equipada |
|------------------|--------------|------------------------------------------------------------------------------|-----------|---------------|
| Faca             | 2            | Lâmina afiada e curta usada para cortar ou perfurar.                         | 3         | False         |
| Agulha           | 1            | Ferramenta fina e pontiaguda, geralmente usada para costura.                 | 1         | False         |
| Soco Ingles      | 1            | Dispositivo de metal usado para reforçar os punhos em combate corpo a corpo. | 2         | False         |
| Faca Curta       | 1            | Pequena faca com lâmina curta, fácil de esconder.                            | 2         | False         |
| Coquetel Molotov | 1            | Garrafa cheia de líquido inflamável e um pavio, usada como explosivo.        | 5         | False         |
| Corda com Cerol  | 1            | Corda revestida com vidro moído para causar cortes.                          | 3         | False         |
| Garrafa Quebrada | 1            | Garrafa de vidro quebrada, usada como arma cortante.                         | 3         | False         |

---

# Fabricacao

| nome_fabri          | *item_fabricavel* | livro_fabricacoes    |
|---------------------|-------------------|----------------------|
| Chave de Fenda Ez   | Chave de Fenda    | Livro de Crafts EASY |
| Pa Ez               | Pa                | Livro de Crafts EASY |
| Martelo Ez          | Martelo           | Livro de Crafts EASY |
| Lock Pick Ez        | Lock Pick         | Livro de Crafts EASY |
| Corda Ez            | Corda             | Livro de Crafts EASY |
| Agulha Ez           | Agulha            | Livro de Crafts EASY |
| Faca Curta Ez       | Faca Curta        | Livro de Crafts EASY |
| Corda com Cerol Ez  | Corda com Cerol   | Livro de Crafts EASY |
| Garrafa Quebrada Ez | Garrafa Quebrada  | Livro de Crafts EASY |
| Picareta Hd         | Picareta          | Livro de Crafts HARD |
| Faca Hd             | Faca              | Livro de Crafts HARD |
| Soco Ingles Hd      | Soco Ingles       | Livro de Crafts HARD |
| Coquetel Molotov Hd | Coquetel Molotov  | Livro de Crafts HARD |

---

# Livro_Fabricacoes

| nome_livro_fabri     |
|----------------------|
| Livro de Crafts EASY |
| Livro de Crafts HARD |


---

## Pessoa

| IdPersonagem | cargo        | tipoP      |
|--------------|--------------|------------|
| 01           | Prisioneiro  | PJ         |
| 02           | Prisioneiro  | PNJ        |
| 03           | Prisioneiro  | PNJ        |
| 04           | Prisioneiro  | PNJ        |
| 05           | Prisioneiro  | PNJ        |
| 06           | Prisioneiro  | PNJ        |
| 07           | Prisioneiro  | PNJ        |
| 08           | Prisioneiro  | PNJ        |
| 09           | Prisioneiro  | PNJ        |
| 10           | Prisioneiro  | PNJ        |
| 11           | Prisioneiro  | PNJ        |
| 12           | Prisioneiro  | PNJ        |
| 13           | Prisioneiro  | PNJ        |
| 14           | Policial     | PNJ        |
| 15           | Policial     | PNJ        |
| 16           | Policial     | PNJ        |
| 17           | Policial     | PNJ        |
| 18           | Policial     | PNJ        |
| 19           | Informante   | PNJ        |

---

# Jogador

| **idPessoa** | **Nome** | **Habilidade de Briga** | **Vida** | **Força** | **Tempo de Vida** | **Gangue** | **Lugar** | **missao** |
|--------------|----------|-------------------------|----------|-----------|-------------------|------------|-----------|------------|
| 01           | Carimbo  | 2                       | 5        | 3         | 10                 | -          | -         |  -         |


----

# Prisioneiro

| **idPessoa** | **Nome**     | **Habilidade de Briga** | **Vida** | **Força** | **Gangue** | **Lugar** |
|--------------|--------------|-------------------------|----------|-----------|------------|-----------|
| 02           | Rivas        | 4                       | 9        | 7         | Palhaços   |           |
| 03           | Filomano     | 6                       | 7        | 4         | Polvos     |           |
| 04           | Fragas       | 5                       | 11       | 5         | Palhaços   |           |
| 05           | Glaucão      | 3                       | 6        | 8         | Polvos     |           |
| 06           | Ucraniano    | 7                       | 5        | 6         | Palhaços   |           |
| 07           | Rispomático  | 6                       | 12       | 6         | Polvos     |           |
| 08           | Manogaz      | 4                       | 8        | 5         | Palhaços   |           |
| 09           | Dado         | 5                       | 10       | 6         | Polvos     |           |
| 10           | Fabrilton    | 4                       | 7        | 5         | Palhaços   |           |
| 11           | Eneido       | 6                       | 6        | 6         | Polvos     |           |
| 12           | Carlos       | 5                       | 9        | 7         | Palhaços   |           |
| 13           | Silvio Serra | 6                       | 8        | 5         | Polvos     |           |



-----

# Policial

| **idPersonagem** | **Nome**              | **Corrupto** |
|------------------|-----------------------|--------------|
| 14               | Italo Dimetrio        | SIM            |
| 15               | Sargento Nascimento   | NÃO            |
| 16               | Capitão Mathias       | NÃO            |
| 17               | Capitão Brad          | SIM            |
| 18               | Lil Chico             | SIM            |


---

# Informante

| **idPersonagem** | **Nome** | **Dano Informante** | **Lugar**
|------------------|----------|-------------------------|-----------|
| 19               | Cubano    | 200                       | -          |

---

# Inventário

|                 |                  |             |           |            |            | 
| --------------- | ------------------|---------|-------|-------|-------|
| **idInventario**   | **Pessoa** |**inventário ocupado** | **tamanho inventário** | 
| 1  | -  | 0  | 5 |

---

<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão | Descrição                                       | Autores                                               |
|------------|--------|-------------------------------------------------|-------------------------------------------------------|
| 26/07/2024 | `1.0`  | Criação do documento.                           | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 28/07/2024 | `1.1`  | Desenvolvimento de algumas tabelas e correções. | [João Antonio G.](https://github.com/joaoseisei)      |
| 28/07/2024 | `1.2`  | Desenvolvimento algumas tabelas.                | [Fernando Gabriel](https://github.com/show-dawn)      |
| 28/07/2024 | `1.3`  | Desenvolvimento algumas tabelas.                | [Julio Cesar](https://github.com/Julio1099)           |
| 29/07/2024 | `1.4`  | Completa a tabela [`Lugar`](#Lugar)             | [Breno Alexandre](https://github.com/brenoalexandre0) |
| 29/07/2024 | `1.5`  | Ajustes tabela Pessoa             | [Júlio](https://github.com/julio1099) |

</div>
