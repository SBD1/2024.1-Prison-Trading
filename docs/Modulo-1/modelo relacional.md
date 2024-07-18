<center>

# Modelo Entidade-Relacionamento

</center>

---


> O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de um banco de dados.

## 1. Entidades

- **Prisao**
- **Regiao**
- **Lugar**
- **Pessoa**
- **Prisioneiro**
- **Policial**
- **Informante**
- **Jogador**
- **Inventário**
- **Instância_Item**
- **Item**
  - **Item_Fabricavel**
    - **Ferramenta**
    - **Arma**
  - **Item_Nao_Fabricavel**
    - **Comida**
    - **Medicamento**
    - **Utilizavel**
- **Fabricação**
- **Livro_Fabricações**
- **Missao**

## 2. Atributos

- **Prisao**: <ins>id_prisao</ins>, nome
- **Regiao**: <ins>nome_regiao</ins>, descricao_regiao, prisao
- **Lugar**: <ins>nome_lugar</ins>, descricao_lugar, regiao, lugar_anterior
- **Pessoa**: <ins>id_pessoa</ins>, nome_pessoa, tipo_pessoa, lugar
- **Prisioneiro**: habilidade_briga_prisioneiro, vida_prisioneiro, forca_prisioneiro, gangue_prisioneiro
- **Policial**: policial_corrupto
- **Informante**: dano_informante
- **Jogador**: habilidade_briga_jogador, vida_jogador, forca_jogador, respeito_jogador, tempo_vida_jogador, gangue_jogador, missao 
- **Inventário**: <ins>id_inventario</ins>, tamanho_inventario, inventario_ocupado, pessoa
- **Instância_Item**: <ins>nome_inst</ins>, item, lugar, inventario, fabricacao
- **Item**: <ins>nome_item</ins>, tipo_item, tamanho_item, descricao_item
  - **Item_Fabricavel**: tipo_fabricavel
    - **Ferramenta**: utilidade_ferramenta
    - **Arma**: dano_arma, arma_equipeada
  - **Item_Nao_Fabricavel**: raridade_nao_fabricavel, tipo_nao_fabricavel
    - **Comida**: quantidade_comida, qualidade_comida
    - **Medicamento**: cura_medicamento, qualidade_medicamento
    - **Utilizavel**: efeito_Utilizavel
- **Fabricação**: <ins>nome_fabri</ins>, item_fabricacao, livro_fabricacoes
- **Livro_Fabricações**: <ins>nome_livro_fabri</ins>
- **Missao**: <ins>id_missao</ins>, nome_missao, descricao_missao, lugar, item_nao_fab

## 3. Relacionamentos

**Prisao _Possui_ Regiao**

- Prisao possui nenhuma ou várias regiões (0,N)
- Regiao pertence a apenas uma única prisão (1,1)

**Regiao _Possui_ Lugar**

- Regiao possui um ou vários lugares (1,N)
- Lugar pertence a apenas uma única região (1,1)

**Lugar _Conecta_ Lugar**

- Lugar pode conectar a nenhum ou quatro outros lugares (1,4)
- Outro Lugar pode ser conectado por um ou quatro lugares (1,4)

**Missao _Está disponivel em_ Lugar**

- Missão está disponível em um ou vários lugares (1,N)
- Lugar possui nenhuma ou várias missões (0,N)

**Pessoa _Está_ em Lugar**

- Pessoa está em apenas um único lugar (1,1)
- Lugar acomoda nenhuma ou várias pessoas (0,N)

**Instância_Item _Está_ em Lugar**

- Instância_Item está em um único lugar (1,1)
- Lugar acomoda nenhuma ou várias pessoas (0,N)

**Pessoa _Possui_ Inventário**

- Pessoa possui apenas um único inventário (1,1)
- Inventário pertence a uma ou várias pessoas (1,N)

**Inventário _Possui_ Instância_Item**

- Inventário possui nenhuma ou várias instâncias de itens (0,N)
- Instância de Item pertence a apenas um único inventário (1,1)

**Instância_Item _Possui_ Item**

- Item pode estar em uma ou várias instâncias de itens (1,N)
- Instância de Item petence a apenas um único item (1,1)

**Instância_Item _É feita_ Fabricação**

- Fabricação é feita de uma ou várias instancias de itens (1,N)
- Instancia de item está em nenhuma ou várias fabricações (0,N)

**Fabricação _Resulta_ Item_Fabricavel**

- Fabricação resulta em apenas um item fabricado (1,1)
- Item Fabricável é resultado por apenas uma única fabricação (1,1)

**Livro_Fabricações _Possui_ Fabricação**

- Livro de Fabricações possui nenhuma ou várias fabricações (0,N)
- Fabricação pertence a apenas um único livro de fabricações (1,1)

**Jogador _Realiza_ Missao**

- Jogador realiza nenhuma ou várias missões (0,N)
- Missão é realizada por um ou vários jogadores (1,N)

**Missao _Droppa_ Item_Nao_Fabricavel**

- Missão droppa um item não fabricável (1,1)
- Item Não Fabricável é droppado por uma missão (1,1)


<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão | Descrição                   | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:---------------------------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10/04/2024 | `1.0`  | Criação da primeira versão. | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 10/04/2024 | `1.1`  | Segunda Versão.             | [Fernando Gabriel](https://github.com/show-dawn), [Julio Cesar](https://github.com/julio1099)                                                                                                           |
| 11/04/2024 | `1.2`  | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 13/04/2024 | `1.3`  | Criação da terceira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 20/04/2024 | `1.4`  | Criação da quarta versão.   | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 18/07/2024 | `1.5`  | Quinta Versão.             | [Julio Cesar](https://github.com/julio1099)                                     

</div>