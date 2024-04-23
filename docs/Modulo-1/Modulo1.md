<center>

# Módulo 1

</center>

---

## Apresentação

<iframe width="560" height="315" src="https://www.youtube.com/embed/s_UC6M6cYQE?si=KjkSU6Bg701QIavW" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---

## Cenário
> Prison Trade é um jogo de estratégia e simulação com foco em trocas como elemento central. Nele, você assume o papel de um prisioneiro em uma prisão isolada, cada uma com seus próprios desafios e obstáculos. O objetivo principal é escapar da prisão, mas ao invés de simplesmente encontrar uma saída, você precisa realizar trocas para obter os itens necessários e criar os planos de fuga.

---
## Modelo Entidade Relacionamento


> O modelo Entidade-Relacionamento tem como principal função, descrever itens, em outras palavras entidades, que são utilizadas para representar participantes de um cenário em um problema que deseja ser resolvido mediante utilização de um banco de dados.


## Entidades

- Pessoa
    - Policial
    - Prisioneiro
        - Jogador
- Item
- Lugar
- Gangue
- Negociação

---

## Atributos
- Pessoa: <ins>id_pessoa</ins>, nome, item(multivalorado), lugar, tipo
  - Policial: grau_corrupcao
  - Prisioneiro: antecedentes_criminais(multivalorado), gangue
    - Jogador: tempo_vida, <ins>r</ins>e<ins>s</ins>p<ins>e</ins>it<ins>o</ins>
- Item: <ins>nome</ins>, utilizavel, lugar
- Lugar: <ins>nome</ins>, nivel_seguranca
- Gangue: <ins>nome</ins>, lider, gangue_rival(multivalorada), prisioneiros(multivalorado)
- Negociaçao: data, lugar, itens (multivalorado)


## Relacionamento

- Pessoa - *Possui* - Item
  - Cardinalidade: N - 0-N
  - Papel: Possui - É posse

---

- Pessoa - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Item - *Está* - Lugar
  - Cardinalidade: 0-N - 1
  - Papel: Está - Acomodam

---

- Jogador - *Troca* - Pessoa
  - Cardinalidade: 1 - 1-N
  - Papel: Troca - Troca

---

- Negociação - *Envolve* - Item
  - Cardinalidade: 1-N - N
  - Papel: Envolve - Está Envolvido

---

- Negociação - *Realiza* - Lugar
  - Cardinalidade: 1-N - 1-N
  - Papel: É Realizado - São Realizadas

---

- Jogador - *Entra* - Gangue
  - Cardinalidade: 0-1 - 0-1
  - Papel: Entra - Possui

---

- Prisioneiro - *Está* - Gangue
  - Cardinalidade: N - 1  
  -  Papel: Está - Possui

---

- Gangue - *É liderada* - Prisioneiro
  - Cardinalidade: 1 - 1
  - Papel: É Liderada - Lidera

---

- Gangue - *Rivaliza* - Gangue
  - Cardinalidade: 1-N - 1-N
  - Papel: Rivaliza - É Rival

---

## Diagrama Entidade Relacionamento

> Um diagrama Entidade-Relacionamento (ER) é uma representação visual de entidades (objetos ou conceitos) e suas relações em um sistema de informação. Ele é usado principalmente para descrever a estrutura dos dados e como eles se relacionam entre si. Esses diagramas são úteis para visualizar e projetar a estrutura de um banco de dados de forma clara e compreensível.

<div align="center">
<div align="center"><img src= "https://raw.githubusercontent.com/SBD1/2024.1-Prison-Trading/Pages/docs/assets/DER.png"/></div>
</div>

---
<center>

# Histórico de versão

</center>

<div style="margin: 0 auto; width: fit-content;">

| Data       | Versão | Descrição                   | Autores                                                                                                                                                                                                 |
|:----------:|:------:|:---------------------------:| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 13/04/2024 | `1.0`  | Criação da primeira versão. | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |
| 20/04/2024 | `1.1`  | Criação da quarta versão.   | [Breno Alexandre](https://github.com/brenoalexandre0), [Fernando Gabriel](https://github.com/show-dawn), [João Antonio G.](https://github.com/joaoseisei),  [Julio Cesar](https://github.com/julio1099) |

</div>