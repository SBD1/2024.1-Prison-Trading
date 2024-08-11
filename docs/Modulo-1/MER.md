<center>

# Modelo Entidade-Relacionamento

</center>

---

<center>

# O que é?

</center>

> O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são
> utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de
> um banco de dados.

---

# Entidades

- **Prisao**
- **Regiao**
- **Lugar**
- **Pessoa**
    - **Prisioneiro**
    - **Policial**
    - **Informante**
    - **Jogador**
- **Inventario**
- **Instancia_Item**
- **Item**
    - **Item_Fabricavel**
        - **Ferramenta**
        - **Arma**
    - **Item_Nao_Fabricavel**
        - **Comida**
        - **Medicamento**
        - **Utilizavel**
- **Fabricacao**
- **Livro_Fabricacao**
- **Missao**

---

# Atributos

- **Prisao**: <ins>id</ins>, nome, descricao
- **Regiao**: <ins>id</ins>, <span style="text-decoration: underline; text-decoration-style: double;">nome</span>,
  descricao
- **Lugar**: <ins>id</ins>,  <span style="text-decoration: underline; text-decoration-style: double;">nome</span>
  descricao
- **Pessoa**: <ins>id</ins>, nome, tipo
    - **Prisioneiro**: habilidade_briga, vida, forca, gangue
    - **Policial**:  corrupto
    - **Informante**: dano
    - **Jogador**: habilidade_briga, vida, forca, tempo_vida, gangue, `nivel`(derivado)
- **Inventario**: <span style="text-decoration: underline; text-decoration-style: dotted;">id</span>,
  tamanho, `tamanho_ocupado`(derivado)
- **Instancia_Item**: <span style="text-decoration: underline; text-decoration-style: dotted;">id</span>
- **Item**: <ins>id</ins>, <span style="text-decoration: underline; text-decoration-style: double;">nome</span>, tipo,
  tamanho, descricao
    - **Item_Fabricavel**: tipo
        - **Ferramenta**: utilidade
        - **Arma**: dano
    - **Item_Nao_Fabricavel**: raridade, quantidade, tipo
        - **Comida**: recuperacao_vida
        - **Medicamento**: cura
        - **Utilizavel**: durabilidade
- **Fabricacao**: <span style="text-decoration: underline; text-decoration-style: dotted;">id</span>
- **Livro_Fabricacao**: <ins>id</ins> <span style="text-decoration: underline; text-decoration-style: double;">
  nome</span>
- **Missao**: <ins>id</ins>, nome, descricao

---

# Relacionamentos

**Prisao _Possui_ Regiao**

- Prisao possui uma ou várias regiões (1,N)
- Regiao pertence a apenas uma única prisão (1,1)

**Regiao _Possui_ Lugar**

- Regiao possui um ou vários lugares (1,N)
- Lugar pertence a apenas uma única região (1,1)

**Lugar _Conecta_ Lugar**

- Lugar pode conectar a um ou varios outros lugares (1,N)
- Outro Lugar pode ser conectado por um ou varios lugares (1,N)

**Missao _Está disponivel em_ Lugar**

- Missão está disponível em nenhum ou um lugar (0,1)
- Lugar possui nenhuma ou várias missões (0,N)

**Pessoa _Está_ em Lugar**

- Pessoa está em apenas um único lugar (1,1)
- Lugar acomoda nenhuma ou várias pessoas (0,N)

**Instancia_Item _Está_ em Lugar**

- Instância de Item está em um único lugar (1,1)
- Lugar acomoda nenhuma ou várias Instancias de itens (0,N)

**Pessoa _Possui_ Inventario**

- Pessoa possui apenas um único inventário (1,1)
- Inventário pertence a uma ou várias pessoas (1,N)

**Inventario _Possui_ Instancia_Item**

- Inventário possui nenhuma ou várias instâncias de itens (0,N)
- Instância de Item pertence a apenas um único inventário (1,1)

**Item _Possui_ Instancia_Item**

- Item possui uma ou várias instâncias de itens (1,N)
- Instância de Item petence a apenas um único item (1,1)

**Fabricacao _É feita_ Item**

- Fabricação é feita de uma ou vários itens (1,N)
- item está em nenhuma ou várias fabricações (0,N)

**Fabricacao _Resulta_ Item_Fabricavel**

- Fabricação resulta em apenas um item fabricado (1,1)
- Item Fabricável é resultado por apenas uma única fabricação (1,1)

**Livro_Fabricacao _Possui_ Fabricao**

- Livro de Fabricações possui nenhuma ou várias fabricações (0,N)
- Fabricação pertence a apenas um único livro de fabricações (1,1)

**Jogador _Realiza_ Missao**

- Jogador realiza nenhuma ou várias missões (0,N)
- Missão é realizada por um ou vários jogadores (1,N)

**Missao _Dropa_ Item_Nao_Fabricavel**

- Missão dropa apenas zero ou um item não fabricável (0,1)
- Item Não Fabricável é dropado por uma ou várias missões (1,N)

---
<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

|    Data    | Versão |               Descrição               | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:-------------------------------------:|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 10/04/2024 | `1.0`  |      Criação da primeira versão.      | [João Antonio G.](https://github.com/joaoseisei)                                                                                                                                                        |
| 10/04/2024 | `1.1`  |            Segunda Versão.            | [Fernando Gabriel](https://github.com/show-dawn), [Julio Cesar](https://github.com/julio1099)                                                                                                           |
| 11/04/2024 | `1.2`  |      Criação da terceira versão.      | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 13/04/2024 | `1.3`  |      Criação da terceira versão.      | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 20/04/2024 | `1.4`  |       Criação da quarta versão.       | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 18/07/2024 | `1.5`  |            Quinta Versão.             | [Julio Cesar](https://github.com/julio1099)                                                                                                                                                             |
| 06/08/2024 | `1.6`  |  Corrige as alterações do professor.  | [Fernando Gabriel](https://github.com/show-dawn),  [João Antonio G.](https://github.com/joaoseisei)                                                                                                     |
| 10/08/2024 | `1.7`  | Finaliza alterações de rotas de fuga. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |

</div>